import requests
from bs4 import BeautifulSoup
from itertools import cycle
import re
import csv
import threading
from threading import Thread
from queue import Queue

global percents, good_proxy, pool


class Worker(Thread):
    """ Thread executing tasks from a given tasks queue """
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as e:
                # An exception happened in this thread
                print(e)
            finally:
                # Mark this task as done, whether an exception happened or not
                self.tasks.task_done()


class ThreadPool:
    """ Pool of threads consuming tasks from a queue """
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, args, kwargs):
        """ Add a task to the queue """
        self.tasks.put((func, args, kwargs))

    def wait_completion(self):
        """ Wait for completion of all the tasks in the queue """
        self.tasks.join()


def thread(my_func):
    global pool

    def wrapper(*args, **kwargs):
        pool.add_task(my_func, args, kwargs)

    return wrapper


def second_thread(my_func):

    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
        my_thread.start()
        print(threading.active_count())

    return wrapper


def write_csv(data):
    with open('computers.csv', 'a', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'],
                          data['price'],
                          data['description'],
                          data['url']))


def get_proxy():
    url = 'https://www.proxynova.com/proxy-server-list/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    all_tr = soup.find('tbody').find_all('tr')

    local_proxies = []
    for tr in all_tr:
        try:
            proxy_ip = re.findall(r'\d+\.\d+\.\d+\.\d+', tr.find('abbr').get('title'))[0]
            proxy_port = tr.find_all('td')[1].text.strip()
            proxy = proxy_ip + ":" + proxy_port
            local_proxies.append(proxy)
        except:
            pass
    return local_proxies


def get_html(url):
    r = requests.get(url)

    return r.text


def get_html_proxy(url, signal):
    global good_proxy, proxies, r
    try:
        r = requests.get(url, proxies={"http": good_proxy, "https": good_proxy})
        soup = BeautifulSoup(r.text, 'lxml')
        title = soup.find('title')
        while title.text == "Доступ временно заблокирован":
            raise NameError

        return r.text
    except NameError:
        signal.emit("Сайт заблокировал ваш IP адрес, будем искать прокси, парсер будет работать медленнее")
        proxies = get_proxy()
        signal.emit("Поиск прокси...")
        for proxy in proxies:
            try:
                r = requests.get(url, proxies={"http": proxy, "https": proxy})
                if r:
                    soup = BeautifulSoup(r.text, 'lxml')
                    title = soup.find('title')
                    if title.text == "Доступ временно заблокирован":
                        signal.emit("Сайт заблокировал этот прокси - " + proxy + ", будем искать новый прокси")
                        proxies.remove(proxy)
                        continue
                    signal.emit("Прокси найден:" + proxy)
                    good_proxy = proxy
                    break
            except Exception as e:
                signal.emit("Не удалось подключиться к прокси, ищем дальше...")
                proxies.remove(proxy)
        return r.text
    except ConnectionError as e:
        print(e)
        return r.text
    except Exception:
        signal.emit("Сайт заблокировал этот прокси - "+good_proxy+", будем искать новый прокси")
        if len(proxies) == 0:
            proxies = get_proxy()

        signal.emit("Поиск прокси...")
        for proxy in proxies:
            try:
                r = requests.get(url, proxies={"http": proxy, "https": proxy})
                if r:
                    signal.emit("Прокси найден:" + proxy)
                    good_proxy = proxy
                    break
            except:
                signal.emit("Не удалось подключиться к прокси, ищем дальше...")
                proxies.remove(proxy)
        return r.text


def get_full_descr(url, ads_len, signal, status_bar_signal):
    global percents
    try:
        html = get_html(url)
        soup = BeautifulSoup(html, 'lxml')
        good_page_test = soup.find('div', class_='item-view-header').find_all('h1')
    except:
        html = get_html_proxy(url, signal)
        soup = BeautifulSoup(html, 'lxml')
        full_descr_p = soup.find('div', class_='item-description-text').find_all('p')
    else:
        full_descr_p = soup.find('div', class_='item-description-text').find_all('p')
    finally:
        full_descr = ""
        for p in full_descr_p:
            full_descr += p.text

    percents = percents + (100 / ads_len)
    status_bar_signal.emit(int(percents))
    return full_descr


@thread
def get_ad_data(ad, ads_len, signal, status_bar_signal):
    try:
        title = ad.find('h3').text.strip()
    except:
        title = ''
    try:
        url = 'https://www.avito.ru' + ad.find('h3').find('a').get('href')
    except:
        url = ''
    try:
        price = ad.find('div', class_='about').text.strip()
    except:
        price = ''
    try:
        full_descr = get_full_descr(url, ads_len, signal, status_bar_signal)
    except:
        full_descr = ''

    data = {'title': title,
            'price': price,
            'description': full_descr,
            'url': url}

    write_csv(data)


def get_page_data(html, signal, status_bar_signal):
    global percents
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item')
    ads_len = len(ads)
    percents = 0
    for ad in ads:
        get_ad_data(ad, ads_len, signal, status_bar_signal)


@second_thread
def start_computers_parser(signal, status_bar_signal, request_target_gui):
    global pool
    pool = ThreadPool(10)

    base_url = 'https://www.avito.ru/tomsk/nastolnye_kompyutery?'
    base_part = 'p='
    date_filter = '&s=104'
    price_max = '&pmax=6000'
    price_min = '&pmin=0'
    request_target = '&q=' + request_target_gui

    # try:
    #     total_pages = get_total_pages(get_html(url))
    # except:
    #     total_pages = get_total_pages(get_html_proxy(url))

    for i in range(1, 2):
        status_bar_signal.emit(0)
        url_gen = base_url + base_part + str(i) + date_filter + price_max + price_min
        try:
            html = get_html(url_gen)
            get_page_data(html, signal, status_bar_signal)
        except:
            html = get_html_proxy(url_gen, signal)
            get_page_data(html, signal, status_bar_signal)

        pool.wait_completion()

        status_bar_signal.emit(100)
    signal.emit("Парсинг завершен")

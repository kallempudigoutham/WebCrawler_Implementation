import threading
from queue import Queue
from general import *
from domain import *
from spider import Spider

PROJECT_NAME = 'The_manit'
HOME_PAGE = 'http://www.manit.ac.in/'
DOMAIN_NAME = get_sub_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THEREADS = 4
queue = Queue()

Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)

import pymysql
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import config
driver = webdriver.Chrome(ChromeDriverManager().install())

conn = pymysql.connect(
    host=config.db_hostname,
    user=config.db_username,
    password=config.db_password,
    db=config.db_name
)
cursor = conn.cursor(pymysql.cursors.DictCursor)

def search_menu_list(name):
    url = "https://www.siksinhot.com"
    driver.get(url + "/search?keywords=" + name)
    time.sleep(5)

    elems = driver.page_source
    soup = BeautifulSoup(elems, 'html.parser')
    
    element = soup.select('.cont > a')
    if not element:
        return

    href = element[0].attrs['href']
    
    conn = pymysql.connect(
        host=config.db_hostname,
        user=config.db_username,
        password=config.db_password,
        db=config.db_name
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    driver.get(url + href)
    time.sleep(20)
    elems = driver.page_source
    soup = BeautifulSoup(elems, 'html.parser')
    categories = soup.select('.menu_ul > li')
    for category in categories:
        menu = category.find('span', attrs={'class': 'tit'})
        print(menu.contents[0])
        sql = "INSERT INTO menu (cafe_id, cafe_name, menu) VALUES (%s, %s, %s)"
        cursor.execute(sql,(id, name, menu.contents[0]))
    conn.commit()
    conn.close()

def get_cafe_list():
    sql = '\
            SELECT name FROM cafe\
          '
    cursor.execute(sql)
    data_list = cursor.fetchall()
    name_list = list((data_list[i]['id'],data_list[i]['name']) for i in range(len(data_list)))
    conn.commit()
    conn.close()

    # TODO menu 테이블에 insert
    for name in name_list:
        print("================================")
        print(name)
        print("================================")
        search_menu_list(name)


get_cafe_list()
driver.quit()
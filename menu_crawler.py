import pymysql
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import config


# 크롬 드라이버 매니저
driver = webdriver.Chrome(ChromeDriverManager().install())


# 데이터베이스 연결
conn = pymysql.connect(
    host=config.db_hostname,
    user=config.db_username,
    password=config.db_password,
    db=config.db_name
)
cursor = conn.cursor(pymysql.cursors.DictCursor)

"""카페 이름을 파라미터로 하여 식신 사이트를 크롤링합니다.
카페의 메뉴와 가격 정보를 가지고 와서 menu 테이블에 삽입합니다."""
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
        
        # 메뉴 테이블에 카페 메뉴와 가격을 삽입
        sql = "INSERT INTO menu (cafe_id, cafe_name, menu) VALUES (%s, %s, %s)"
        cursor.execute(sql,(id, name, menu.contents[0]))
    conn.commit()
    conn.close()


"""데이터베이스 카페 테이블에서 카페 이름을 모두 가지고 온 뒤, 
각 이름을 인자로 하여 search_menu_list 함수를 호출합니다."""
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
from urllib.parse import urlparse
import json
import requests
import pymysql
import config

rds_host = "rds-instance-endpoint"
name = config.db_username
password = config.db_password
db_name = config.db_name

# 카공 지수 높은 순으로 sort
def lambda_handler(event, context):

    latitude = event['latitude']
    longitude = event['longitude']
    data = []
    for page in range(1, 4):
        url = 'https://dapi.kakao.com/v2/local/search/category.json'
        params = {'category_group_code': 'CE7', 'x': str(
            longitude), 'y': str(latitude), 'radius': 100, 'page': str(page)}
        result = requests.get(url, params=params, headers={
                              'Authorization': 'KakaoAK '}).json()
        for value in result['documents']:
            tmp = (value['id'], value['place_name'], value['x'], value['y'])
            if tmp not in data:
                data.append(tmp)

    if not data:
        return {
            'success': 'false',
        }
    else:
        cagong_db = pymysql.connect(
            user=name,
            passwd=password,
            host=rds_host,
            db=db_name,
            charset='utf8'
        )
        cursor = cagong_db.cursor(pymysql.cursors.DictCursor)
        for i in range(len(data)):
            sql = "SELECT AVG(star) FROM review WHERE cafe_id = %s"
            cursor.execute(sql, (int(data[i][0])))
            rows = cursor.fetchall()
            if not rows[0]['AVG(star)']:
                data[i] += (-1,)
            else:
                data[i] += (rows[0]['AVG(star)'],)

        data.sort(reverse=True, key=lambda x: x[4])

        for i in range(len(data)):
            if data[i][4] == -1.0:
                data[i] = list(data[i])
                data[i][4] = "false"
                data[i] = tuple(data[i])

        return_data = []
        for d in data:
            return_data.append(
                {'id': d[0], 'place_name': d[1], 'latitude': d[3], 'longitude': d[2], 'star_average': d[4]})
        return {
            'sucess': 'true',
            'data': return_data
        }

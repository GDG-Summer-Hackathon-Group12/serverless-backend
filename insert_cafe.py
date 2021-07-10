import json
import pymysql
import requests
import decimal
import rds_config


# 까페 정보 데이터베이스에 insert 
def lambda_handler(event, context):
    rds_host  = "rds-instance-endpoint"
    name = rds_config.db_username
    password = rds_config.db_password
    db_name = rds_config.db_name

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
            tmp = (value['id'], value['place_name'], value['x'], value['y'], value['phone'],
                   value['address_name'], value['road_address_name'], value['place_url'])
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
        for d in data:
            try:
                sql = "INSERT INTO cafe (id, `name`, latitude, longitude, phone, `address`, road_address, place_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (int(d[0]), d[1], decimal.Decimal(
                    d[3]), decimal.Decimal(d[2]), d[4], d[5], d[6], d[7]))
            except:
                pass
        cagong_db.commit()
        cagong_db.close()

        # TODO implement
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }

import pymysql
import config
from urllib import parse

# db setting
hostname = config.db_hostname
username = config.db_username
password = config.db_password
db_name = config.db_name

def lambda_handler(event, context):

    cafe_id = event['params']['path']['cafe-id']

    conn = pymysql.connect(
        host=hostname,
        user=username,
        password=password,
        db=db_name
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    sql = '\
            SELECT c.id, c.name, count(r.id) as cnt_review, \
                   ROUND(AVG(r.star), 2) as avg_star, ROUND(AVG(r.noise), 1) as avg_noise, ROUND(AVG(r.light), 1) as avg_light, ROUND(AVG(r.chair), 1) as avg_chair \
            FROM cafe as c \
            LEFT JOIN review as r ON c.id = r.cafe_id \
            WHERE c.id = ' + str(cafe_id)

    cursor.execute(sql)
    data = cursor.fetchall()

    if not data[0]['name']:
        return {
            "success": False,
            "message": "카페 정보가 존재하지 않습니다."
        }

    # 대표 이미지 url 조회
    sql = ' \
            SELECT image_url as thumbnail \
            FROM image  \
            WHERE cafe_id = %s \
            ORDER BY id DESC LIMIT 1'

    cursor.execute(sql, cafe_id)
    thumbnail = cursor.fetchone()
    if not thumbnail:
        data[0]['thumbnail'] = config.default_image_url
    else:
        thumbnail_name = parse.quote(thumbnail.get('thumbnail').split(config.s3_base_url)[1])
        data[0]['thumbnail'] = config.s3_base_url + thumbnail_name 

    conn.commit()
    conn.close()

    return {
        "success": True,
        "data": data[0]
    }
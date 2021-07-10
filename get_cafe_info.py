import pymysql
import config

def lambda_handler(event, context):

    cafe_id = event['params']['path']['cafe-id']

    # db setting
    hostname = config.db_hostname
    username = config.db_username
    password = config.db_password
    db_name = config.db_name

    conn = pymysql.connect(
        host=hostname,
        user=username,
        password=password,
        db=db_name
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # TODO customer 쿼리 수정
    sql = 'SELECT  c.id, c.name, c.phone, c.address, c.latitude, c.longitude, \
                   ROUND(AVG(r.star), 2) as avg_star, \
                   ROUND(AVG(r.noise), 1) as avg_noise, ROUND(AVG(r.light), 1) as avg_light, ROUND(AVG(r.chair), 1) as avg_chair,\
                   ROUND(AVG(r.consent), 0) as avg_consent, ROUND(AVG(r.wifi), 0) as avg_wifi,  \
                   (SELECT customer \
                    FROM review \
                    GROUP BY customer \
                    HAVING count(*) = (SELECT max(custom_count) \
    			    FROM (SELECT customer, count(*) as custom_count \
    					 FROM review \
    					 GROUP BY customer) as result)) as customer \
                    FROM cafe as c \
                    LEFT JOIN review as r ON c.id = r.cafe_id \
                            WHERE c.id =' + str(cafe_id)

    cursor.execute(sql)
    data = cursor.fetchall()

    cafe_list = list(data[0].values())

    # 카페 정보 없는 경우 
    # TODO 코드 수정 필요
    if cafe_list[0:len(data[0]) - 1] == [None]*(len(data[0]) - 1):
        return {
            "success": False,
            "message": "카페 정보가 존재하지 않습니다."
        }

    # 대표 리뷰 조회
    sql = ' \
           SELECT detail, count(*) \
           FROM review \
           WHERE `cafe_id` = %s AND detail IS NOT NULL \
           ORDER BY id DESC LIMIT 1'

    cursor.execute(sql, cafe_id)

    review = cursor.fetchone()
    if not review:
        data[0]['review'] = None
    else:
        data[0]['review'] = review.get('detail')

    conn.commit()
    conn.close()

    return {
        "success": True,
        "data": data[0]
    }
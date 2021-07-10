import pymysql
import config

def lambda_handler(event, context):

    # db setting
    try:
        conn = pymysql.connect(
            host=config.db_hostname,
            user=config.db_username,
            password=config.db_password,
            db=config.db_name
        )
    except pymysql.MySQLError as e:
        return {
            "success": False,
            "message": "Database Error"
        }
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cafe_id = event['params']['path']['cafe-id']

    # 이미지 리스트 조회
    sql = '\
            SELECT image_url \
            FROM image \
            WHERE `cafe_id` = ' + str(cafe_id)

    cursor.execute(sql)
    imageList = cursor.fetchall()
    if not len(imageList):
        return {
            "success": False,
            "message": "이미지 존재하지 않습니다."
        }

    data = list(imageList[i]['image_url'] for i in range(len(imageList)))

    conn.commit()
    conn.close()

    return {
        "success": True,
        "data": data
    }
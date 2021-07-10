import pymysql
import config

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

    # 이미지 리스트 조회
    sql = ' \
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
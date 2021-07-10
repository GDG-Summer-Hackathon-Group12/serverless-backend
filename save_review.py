import pymysql
import config

def lambda_handler(event, context):

    # db setting
    conn = pymysql.connect(
        host=config.db_hostname,
        user=config.db_username,
        password=config.db_password,
        db=config.db_name
    )

    cafe_id = event['params']['path']['cafe-id']
    body = event['body-json']

    cursor = conn.cursor()
    print(event)

    data = []
    data.append(cafe_id)
    if 'star' not in body:
        return {
            "success": False,
            "message": "별점 입력해주세요."
        }

    data.append(body['star'])
    data.append(body.get('consent'))
    data.append(body.get('chair'))
    data.append(body.get('noise'))
    data.append(body.get('light'))
    data.append(body.get('wifi'))
    data.append(body.get('customer'))
    data.append(body.get('detail'))

    print(data)
    print(body['imageList'])

    # review 테이블 삽입
    sql = 'INSERT INTO \
           review (`cafe_id`, `star`, `consent`, `chair`, `noise`, `light`, `wifi`, `customer`, `detail`)  \
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(sql, data)

    review_id = cursor.lastrowid

    # image 테이블 삽입
    sql = 'INSERT INTO image (`cafe_id`, `review_id`, `image_url`) VALUES ("' + \
        str(cafe_id) + '", "' + str(review_id) + '", %s)'
    cursor.executemany(sql, body['imageList'])

    conn.commit()
    conn.close()

    return {
        "success": True
    }

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

    sql = ' \
       SELECT menu, price \
       FROM menu \
       WHERE `cafe_id` = ' + str(cafe_id)

    cursor.execute(sql)
    menu_list = cursor.fetchall()
    if not len(menu_list):
        return {
            "success": False,
            "message": "메뉴 정보가 존재하지 않습니다."
        }
    # data = list(list(menu_list[i].values()) for i in range(len(menu_list)))

    conn.commit()
    conn.close()

    return {
        "success": True,
        "data": menu_list
    }

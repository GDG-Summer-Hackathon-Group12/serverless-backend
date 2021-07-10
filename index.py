from urllib.parse import urlparse
import json
import requests
import boto3


"""웹앱에서 지도가 나오면 중심 좌표 반경 100m의 카페 정보를 반환하는 람다 함수.
해당 람다 함수가 save_cafe.py 람다 함수를 호출하여 카페 정보를 데이터베이스에 INSERT한다."""
def lambda_handler(event, context):
    latitude = event['latitude']
    longitude = event['longitude']

    # save_cafe.py 람다 함수를 호출
    payload = {'latitude': latitude, 'longitude': longitude}
    lan = boto3.client(service_name='lambda', region_name="ap-northeast-2")
    lan.invoke(FunctionName="insert_cafe", InvocationType='Event',
               Payload=json.dumps(payload))

    
    data = []
    
    # 카카오 REST API로 카페 정보를 가지고 옴.
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
    
    # 데이터가 없다면 json형식으로 false를 반환하고, 데이터가 있으면 데이터를 반환한다.
    if not data:
        return {
            'success': False,
        }
    else:
        return_data = []
        for d in data:
            return_data.append({'id': d[0], 'place_name': d[1], 'latitude': d[3], 'longitude': d[2],
                                'phone': d[4], 'address_name': d[5], 'road_address_name': d[6], 'place_url': d[7]})
        return {
            'success': True,
            'data': return_data
        }

from urllib.parse import urlparse
import json
import requests
import boto3

# 시작 화면
def lambda_handler(event, context):
    latitude = event['latitude']
    longitude = event['longitude']

    payload = {'latitude': latitude, 'longitude': longitude}
    lan = boto3.client(service_name='lambda', region_name="ap-northeast-2")
    lan.invoke(FunctionName="insert_cafe", InvocationType='Event',
               Payload=json.dumps(payload))

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
        return_data = []
        for d in data:
            return_data.append({'id': d[0], 'place_name': d[1], 'latitude': d[3], 'longitude': d[2],
                                'phone': d[4], 'address_name': d[5], 'road_address_name': d[6], 'place_url': d[7]})
        return {
            'success': 'true',
            'data': return_data
        }

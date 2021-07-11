<h1 align="center">Welcome to cagong👋</h1>

<p align="center">
<img width="700" src="./assets/main.png" />
</p>

<br><br>

## ❓ What is cagong?

> 카공족이란? <br> 카페에서 커피나 간식 등을 구매하고 장시간 머무르며 공부하는 사람들을 말합니다.

**요즘 날씨도 더워지면서 카페에 공부하러오는 카공족들이 늘어나고 있습니다. 카공족들을 위해 동네나 학교 주변 카페에서 공부했던 사람들의 후기나 여담을 올리는 커뮤니티 만들어 봅시다!**

<br><br>

## 📌 Architecture

<p align="center">
<img src="./assets/kagong_diagram.png" />
</p>

<br><br>

## 📂 DB Modeling

<p align="center">
<img src="./assets/db_modeling.png" />
</p>

<br><br>

## 🚩 API 명세


<details>
<summary><b>[GET]  지도에서 카페들의 정보 조회 (인효)<b></summary>
<div markdown="1">       

<br>

100m 반경에 있는 카페 목록의 위도, 경도, 카페 이름을 반환합니다. <br>

<img width="300" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/83fad212-048e-4e92-9ee6-1b1849e7d9e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T012223Z&X-Amz-Expires=86400&X-Amz-Signature=54723ac59f5dd37a643ac6223e3ac0645a95b2d862c7b88a61e05f673114ba92&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" />

```
[GET] /cafes?latitude=x&longitude=x
```

- **Response Body**

    ```json
    {
        "sucess": "true",
        "data": [
            {
                "id": "806447073",
                "place_name": "투썸플레이스 이대역점",
                "latitude": "37.5572360514845",
                "longitude": "126.94569812655"
            },
            {
                "id": "1866064248",
                "place_name": "카페봄봄 이화여대점",
                "latitude": "37.55722067043155",
                "longitude": "126.94555893119713"
            },
            {
                "id": "19622085",
                "place_name": "공차 이대점",
                "latitude": "37.5569764014276",
                "longitude": "126.945345206914"
            },
            {
                "id": "438330961",
                "place_name": "흑화당 이대점",
                "latitude": "37.5571243278597",
                "longitude": "126.945698207623"
            },
            {
                "id": "13127567",
                "place_name": "카페쥬디",
                "latitude": "37.5572832629733",
                "longitude": "126.946485798103"
            },
            {
                "id": "1595131797",
                "place_name": "커피베이 이대역점",
                "latitude": "37.55650794784634",
                "longitude": "126.945485885993"
            },
            {
                "id": "10368507",
                "place_name": "라바짜 이대점",
                "latitude": "37.5574344119916",
                "longitude": "126.946005822281"
            },
            {
                "id": "213867029",
                "place_name": "다인전통찻집",
                "latitude": "37.556443159523",
                "longitude": "126.945667012953"
            },
            {
                "id": "23040316",
                "place_name": "바카라",
                "latitude": "37.55606405286577",
                "longitude": "126.9461324344883"
            },
            {
                "id": "17811924",
                "place_name": "이지웨이 이대점",
                "latitude": "37.5572252103555",
                "longitude": "126.945634755837"
            }
        ]
    }
    ```

</div>
</details>

<details>
<summary><b>[GET] 카공지수로 정렬된 카페 리스트 조회 (인효)<b></summary>
<div markdown="1">   

<br>
새로운 페이지나 지도 옆에 슬라이드로 평점이 높은 까페 순으로 위도, 경도, 카페 이름 반환합니다. <br><br>

<img width="300" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b3223d6c-0d6f-4d29-a4b6-4b878bcb6400/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T012725Z&X-Amz-Expires=86400&X-Amz-Signature=d44d401fd6900f79e7c218cbbf2d660b190d20dd0052cde3a65161f5fedf4276&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" />

```
[GET] /cafes/sorted?latitude=12345678901234&longitude=12345678901234
```

- **Response Body**

    ```json
    {
        "sucess": "true",
        "data": [
            {
                "id": "806447073",
                "place_name": "투썸플레이스 이대역점",
                "latitude": "37.5572360514845",
                "longitude": "126.94569812655",
                "avg_star": 3.227272727272727
            },
            {
                "id": "1866064248",
                "place_name": "카페봄봄 이화여대점",
                "latitude": "37.55722067043155",
                "longitude": "126.94555893119713",
                "avg_star": "false"
            },
            {
                "id": "19622085",
                "place_name": "공차 이대점",
                "latitude": "37.5569764014276",
                "longitude": "126.945345206914",
                "avg_star": "false"
            },
            {
                "id": "438330961",
                "place_name": "흑화당 이대점",
                "latitude": "37.5571243278597",
                "longitude": "126.945698207623",
                "avg_star": "false"
            },
            {
                "id": "13127567",
                "place_name": "카페쥬디",
                "latitude": "37.5572832629733",
                "longitude": "126.946485798103",
                "avg_star": "false"
            },
            {
                "id": "1595131797",
                "place_name": "커피베이 이대역점",
                "latitude": "37.55650794784634",
                "longitude": "126.945485885993",
                "avg_star": "false"
            },
            {
                "id": "10368507",
                "place_name": "라바짜 이대점",
                "latitude": "37.5574344119916",
                "longitude": "126.946005822281",
                "avg_star": "false"
            },
            {
                "id": "213867029",
                "place_name": "다인전통찻집",
                "latitude": "37.556443159523",
                "longitude": "126.945667012953",
                "avg_star": "false"
            },
            {
                "id": "23040316",
                "place_name": "바카라",
                "latitude": "37.55606405286577",
                "longitude": "126.9461324344883",
                "avg_star": "false"
            },
            {
                "id": "17811924",
                "place_name": "이지웨이 이대점",
                "latitude": "37.5572252103555",
                "longitude": "126.945634755837",
                "avg_star": "false"
            }
        ]
    }
    ```

</div>
</details>



<details>
<summary><b>[GET] 카페 메인 정보 조회 (아영)<b></summary>
<div markdown="1">   

<br>
해당 카페의 메인 정보를 조회합니다. <br><br>

<img width="300" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5013dd11-114f-48b6-a1a3-c17193efab45/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T012900Z&X-Amz-Expires=86400&X-Amz-Signature=401ba0a2b54580aa2a6405c08037e00f0dcd92e392e37202259c636f33e56b59&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" />

```
[GET] /cafes/{cafe-id}
```

- Response Body
    - 성공 1

        ```json
        // 21446374
        {
            "success": true,
            "data": {
                "id": 21446374,
                "name": "Take 10Cafe",
                "cnt_review": 21,
                "avg_star": 2.93,
                "avg_noise": 2.6,
                "avg_light": 2.3,
                "avg_chair": 1.9,
                "thumbnail": "https://~.png"
            }
        }
        ```

    - 성공 2

        ```json
        // 8119644
        {
            "success": true,
            "data": {
                "id": 8119644,
                "name": "프린세스다이어리",
                "cnt_review": 0,
                "avg_star": null,
                "avg_noise": null,
                "avg_light": null,
                "avg_chair": null,
                "thumbnail": "https://~.png"
            }
        }
        ```

    - 실패

        ```json
        {
            "success": false,
            "message": "카페 정보가 존재하지 않습니다."
        }
        ```

</div>
</details>


<details>
<summary><b>[GET] 카페 상세 정보 조회 (아영)<b></summary>
<div markdown="1">   

<br>
카페의 상세 정보를 조회합니다. (첫 번째 탭)<br>

<img width="300" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/211b7922-6808-4d00-b44b-c6403f9a5a23/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T013130Z&X-Amz-Expires=86400&X-Amz-Signature=04ec03a6e550666ccdfe51fc5a3381d70fac6ac3284c6885ebaae6c053c8a98c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" />

```json
[GET] /cafes/{cafe-id}/info
```

- **Response Body**
    - **성공**

        ```json
        {
            "success": true,
            "data": {
                "id": 21446374,
                "name": "Take 10Cafe",
                "phone": null,
                "address": null,
                "latitude": 37.55764294352850,
                "longitude": 126.94492370288400,
                "avg_star": 2.85,
                "avg_noise": 2.6,
                "avg_light": 2.3,
                "avg_chair": 1.7,
                "avg_consent": 1,
                "avg_wifi": 2,
                "customer": 1,
                "review": "요호"
            }
        }
        ```

    - **성공 (카페 정보만 있는 경우)**

        ```json
        // 8119644
        {
            "success": true,
            "data": {
                "id": 8119644,
                "name": "프린세스다이어리",
                "phone": "012002",
                "address": "서울특별시 서대문구",
                "latitude": 37.55796784146020,
                "longitude": 126.94609145201600,
                "avg_star": null,
                "avg_noise": null,
                "avg_light": null,
                "avg_chair": null,
                "avg_consent": null,
                "avg_wifi": null,
                "customer": 2,
                "review": null
            }
        }
        ```

    - **실패 (카페 정보 자체가 DB에 없는 경우)**

        ```json
        {
            "success": false,
            "message": "카페 정보가 존재하지 않습니다."
        }
        ```

</div>
</details>


<details>
<summary><b>[GET] 카페 리뷰 목록 조회 (인효)<b></summary>
<div markdown="1">   

<br>
해당 카페의 리뷰 목록을 조회합니다. (두 번째 탭)<br>

<img width="300" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/eee6c260-d923-4733-a4ae-f75a4bea5bca/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T013444Z&X-Amz-Expires=86400&X-Amz-Signature=868ffa816565304d5c17c715f4e306432408d24d2c346532789546b0da63425e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" />

```json
[GET] /cafes/{cafe-id}/reviews 
```

- **Response Body**

    ```json
    {
      "success": "true",
      "data": [
        {
          "star": 1,
          "detail": "요호"
        },
        {
          "star": 4.5,
          "detail": "성공이다"
        },
        {
          "star": 3.5,
          "detail": "다 좋지만 화장실이 별로다"
        },
        {
          "star": 2.5,
          "detail": "포스트맨 테스트"
        },
        {
          "star": 2.5,
          "detail": "포스트맨 테스트"
        },
        {
          "star": 2.5,
          "detail": "포스트맨 테스트"
        },
        {
          "star": 3.5,
          "detail": "다 좋지만 화장실이 별로다"
        },
        {
          "star": 3.5,
          "detail": "다 좋지만 화장실이 별로다"
        },
        {
          "star": 3.5,
          "detail": "다 좋지만 화장실이 별로다"
        },
        {
          "star": 4,
          "detail": "요호"
        },
        {
          "star": 4,
          "detail": "요호"
        },
        {
          "star": 3.5,
          "detail": "요호"
        },
        {
          "star": 1,
          "detail": "요호"
        }
      ]
    }
    ```
</div>
</details>



<details>
<summary><b>[GET] 카페 이미지 목록 조회 (아영)<b></summary>
<div markdown="1">   

<br>
해당 카페의 이미지들을 조회합니다. (세 번째 탭)<br>

<img width="300" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d73cfb28-e59a-43ac-beb7-52e74e335879/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T013524Z&X-Amz-Expires=86400&X-Amz-Signature=06fc2076c602760d423416763ca3de188e9027a9e825a0ccb1b68250366c0b03&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" />

```
[GET] /cafes/{cafe-id}/images
```

- **Response Body**
    - **성공**

        ```json
        {
            "success": true,
            "data": [
                "https://~.jpeg",
                "https://~.jpeg",
                "https://~.jpeg",
                "https://~.jpeg",
                "https://~.jpeg",
                "https://~.jpeg."
            ]
        }
        ```

    - **실패**

        ```json
        {
            "success": false,
            "message": "이미지 존재하지 않습니다."
        }
        ```

</div>
</details>



<details>
<summary><b>[GET] 카페 메뉴 조회 (아영)<b></summary>
<div markdown="1">  

<br>
해당 카페의 메뉴를 조회합니다. (네 번째 탭)<br>

<img width="300" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d8af312a-7c7b-4bc9-b5a7-6596e8604815/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T013603Z&X-Amz-Expires=86400&X-Amz-Signature=2f4239cf3de97274802dca97c1b42d6f65d9d126ed5b3d1ae9296d5cfd89f909&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" />

```
[GET] /cafes/{cafe-id}/menus
```

- **Response Body**
    - **성공**

        ```json
        {
            "success": true,
            "data": [
                {
                    "menu": "돈코츠라멘",
                    "price": 6000
                },
                {
                    "menu": "카라귀라멘",
                    "price": 6000
                },
                {
                    "menu": "쯔케면",
                    "price": 6000
                },
                {
                    "menu": "쿠로 라멘",
                    "price": 6000
                },
                {
                    "menu": "안카케 야끼라멘",
                    "price": 6000
                }
            ]
        }
        ```

    - 실패

        ```json
        {
            "success": false,
            "message": "메뉴 정보가 존재하지 않습니다."
        }
        ```

</div>
</details>


<details>
<summary><b>[POST] 이미지 리스트 업로드 (아영) <b></summary>
<div markdown="1">   

<br>

리뷰 작성할 때, 이미지를 첨부하는 경우 API를 호출합니다. <br>
이미지 url 리스트를 받아 `리뷰 작성 API` 를 호출할 때 Request Body에 담습니다. <br>

<img width="300" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/97de5d3b-26b0-4dac-b569-176d2dc4aa4e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T013638Z&X-Amz-Expires=86400&X-Amz-Signature=f4887f1977b5ceb23e3318d4761eb6264c362ef9a46aaf14c4191fcdd334d896&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" />

<br>

```json
[POST] /images
```

- **Request Header**

    ```json
    {
        "Content-Type": "multipart/form-data"
    }
    ```

- **Request Body**

    ```json
    form-data file로 전송 
    key는 file로 설정
    ```

    예시

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a5c59705-0fd2-4347-bb50-e36b18bc6e28/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a5c59705-0fd2-4347-bb50-e36b18bc6e28/Untitled.png)

- **Response Body**

    이미지 url 리스트를 반환합니다.

    ```json
    {
        "success": true,
        "data": [
            "https://~.png",
            "https://~.png"
        ]
    }
    ```

</div>
</details>


<details>
<summary><b>[POST] 리뷰 작성 (아영)<b></summary>
<div markdown="1">   

<br>

id가 `{cafe-id}`인 카페의 카공 후기를 작성합니다.<br>

<img width="300" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/32bd8d2b-187a-4b85-9c37-4aa19f26c132/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T013716Z&X-Amz-Expires=86400&X-Amz-Signature=9d84047d3f0c0f0dcdbc13d51d67296e44b0ffaa67478c0a4621f71e2869c6a8&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" />

<br>

```
[POST] /cafes/{cafe-id}/reviews
```

- **Request Body**

    ```json
    {
    		"star": 3.5,
        "consent": 2,
    		"chair": 3,
    		"noise": 3,
    		"light": 2,
    		"wifi": 2,
    		"customer": 1,
    		"detail": "최고",
        "imageList": [
            "https://~.jpeg"  
        ]   
    }
    ```

- **Response Body**
    - **성공**

        ```json
        {
            "success": true
        }
        ```

    - **실패 (별점 없는 경우)**

        ```json
        {
            "success": false,
            "message": "별점 입력해주세요."
        }
        ```

</div>
</details>

<br><br>

## 📝 License

Copyright © 2021 [GDG-Summer-Hackathon-Group12](https://github.com/GDG-Summer-Hackathon-Group12).<br/>
This project is [MIT](https://github.com/GDG-Summer-Hackathon-Group12/serverless-backend/blob/main/LICENSE) licensed.
***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
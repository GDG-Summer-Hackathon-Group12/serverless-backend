<h1 align="center">Welcome to cagong๐</h1>

<p align="center">
<img width="700" src="./assets/main.png" />
</p>

<br><br>

## โ What is cagong?

> ์นด๊ณต์กฑ์ด๋? <br> ์นดํ์์ ์ปคํผ๋ ๊ฐ์ ๋ฑ์ ๊ตฌ๋งคํ๊ณ  ์ฅ์๊ฐ ๋จธ๋ฌด๋ฅด๋ฉฐ ๊ณต๋ถํ๋ ์ฌ๋๋ค์ ๋งํฉ๋๋ค.

**์์ฆ ๋ ์จ๋ ๋์์ง๋ฉด์ ์นดํ์ ๊ณต๋ถํ๋ฌ์ค๋ ์นด๊ณต์กฑ๋ค์ด ๋์ด๋๊ณ  ์์ต๋๋ค. ์นด๊ณต์กฑ๋ค์ ์ํด ๋๋ค๋ ํ๊ต ์ฃผ๋ณ ์นดํ์์ ๊ณต๋ถํ๋ ์ฌ๋๋ค์ ํ๊ธฐ๋ ์ฌ๋ด์ ์ฌ๋ฆฌ๋ ์ปค๋ฎค๋ํฐ ๋ง๋ค์ด ๋ด์๋ค!**

<br><br>

## ๐ Architecture

<p align="center">
<img src="./assets/kagong_diagram.png" />
</p>

<br><br>

## ๐ DB Modeling

<p align="center">
<img src="./assets/db_modeling.png" />
</p>

<br><br>

## ๐ฉ API ๋ช์ธ


<details>
<summary><b>[GET]  ์ง๋์์ ์นดํ๋ค์ ์ ๋ณด ์กฐํ (์ธํจ)<b></summary>
<div markdown="1">       

<br>

100m ๋ฐ๊ฒฝ์ ์๋ ์นดํ ๋ชฉ๋ก์ ์๋, ๊ฒฝ๋, ์นดํ ์ด๋ฆ์ ๋ฐํํฉ๋๋ค. <br>

<img width="300" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/83fad212-048e-4e92-9ee6-1b1849e7d9e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T012223Z&X-Amz-Expires=86400&X-Amz-Signature=54723ac59f5dd37a643ac6223e3ac0645a95b2d862c7b88a61e05f673114ba92&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" />

```
[GET] /cafes?latitude=x&longitude=x
```

- **Response Body**

    ```json
    {
        "success": true,
        "data": [
            {
                "id": "806447073",
                "place_name": "ํฌ์ธํ๋ ์ด์ค ์ด๋์ญ์ ",
                "latitude": "37.5572360514845",
                "longitude": "126.94569812655",
                "phone": "02-312-8014",
                "address_name": "์์ธ ์๋๋ฌธ๊ตฌ ๋ํ๋ 40-4",
                "road_address_name": "์์ธ ์๋๋ฌธ๊ตฌ ์ดํ์ฌ๋๊ธธ 7",
                "place_url": "http://place.map.kakao.com/806447073"
            },
            {
                "id": "1866064248",
                "place_name": "์นดํ๋ด๋ด ์ดํ์ฌ๋์ ",
                "latitude": "37.55722067043155",
                "longitude": "126.94555893119713",
                "phone": "070-8881-1224",
                "address_name": "์์ธ ์๋๋ฌธ๊ตฌ ๋ํ๋ 40-9",
                "road_address_name": "์์ธ ์๋๋ฌธ๊ตฌ ์ดํ์ฌ๋๊ธธ 7",
                "place_url": "http://place.map.kakao.com/1866064248"
            },
            {
                "id": "19622085",
                "place_name": "๊ณต์ฐจ ์ด๋์ ",
                "latitude": "37.5569764014276",
                "longitude": "126.945345206914",
                "phone": "070-4230-7514",
                "address_name": "์์ธ ์๋๋ฌธ๊ตฌ ๋ํ๋ 40-20",
                "road_address_name": "์์ธ ์๋๋ฌธ๊ตฌ ์ ์ด๋ก 173-2",
                "place_url": "http://place.map.kakao.com/19622085"
            },
            {
                "id": "438330961",
                "place_name": "ํํ๋น ์ด๋์ ",
                "latitude": "37.5571243278597",
                "longitude": "126.945698207623",
                "phone": "02-365-9997",
                "address_name": "์์ธ ์๋๋ฌธ๊ตฌ ๋ํ๋ 40-6",
                "road_address_name": "์์ธ ์๋๋ฌธ๊ตฌ ์ดํ์ฌ๋๊ธธ 1",
                "place_url": "http://place.map.kakao.com/438330961"
            },
            {
                "id": "13127567",
                "place_name": "์นดํ์ฅฌ๋",
                "latitude": "37.5572832629733",
                "longitude": "126.946485798103",
                "phone": "070-4254-3296",
                "address_name": "์์ธ ์๋๋ฌธ๊ตฌ ๋ํ๋ 45-41",
                "road_address_name": "์์ธ ์๋๋ฌธ๊ตฌ ์ดํ์ฌ๋2๊ธธ 10",
                "place_url": "http://place.map.kakao.com/13127567"
            },
            {
                "id": "1595131797",
                "place_name": "์ปคํผ๋ฒ ์ด ์ด๋์ญ์ ",
                "latitude": "37.55650794784634",
                "longitude": "126.945485885993",
                "phone": "02-706-8029",
                "address_name": "์์ธ ๋งํฌ๊ตฌ ๋ํฅ๋ 12-6",
                "road_address_name": "์์ธ ๋งํฌ๊ตฌ ์ ์ด๋ก 180",
                "place_url": "http://place.map.kakao.com/1595131797"
            },
            {
                "id": "10368507",
                "place_name": "๋ผ๋ฐ์ง ์ด๋์ ",
                "latitude": "37.5574344119916",
                "longitude": "126.946005822281",
                "phone": "02-312-5544",
                "address_name": "์์ธ ์๋๋ฌธ๊ตฌ ๋ํ๋ 54-24",
                "road_address_name": "์์ธ ์๋๋ฌธ๊ตฌ ์ดํ์ฌ๋๊ธธ 12",
                "place_url": "http://place.map.kakao.com/10368507"
            },
            {
                "id": "213867029",
                "place_name": "๋ค์ธ์ ํต์ฐป์ง",
                "latitude": "37.556443159523",
                "longitude": "126.945667012953",
                "phone": "",
                "address_name": "์์ธ ๋งํฌ๊ตฌ ๋ํฅ๋ 12-1",
                "road_address_name": "์์ธ ๋งํฌ๊ตฌ ์ ์ด๋ก 182",
                "place_url": "http://place.map.kakao.com/213867029"
            },
            {
                "id": "23040316",
                "place_name": "๋ฐ์นด๋ผ",
                "latitude": "37.55606405286577",
                "longitude": "126.9461324344883",
                "phone": "",
                "address_name": "์์ธ ๋งํฌ๊ตฌ ๋ํฅ๋ 2-64",
                "road_address_name": "์์ธ ๋งํฌ๊ตฌ ๋ํฅ๋ก30๊ธธ 6-6",
                "place_url": "http://place.map.kakao.com/23040316"
            },
            {
                "id": "17811924",
                "place_name": "์ด์ง์จ์ด ์ด๋์ ",
                "latitude": "37.5572252103555",
                "longitude": "126.945634755837",
                "phone": "070-7758-8288",
                "address_name": "์์ธ ์๋๋ฌธ๊ตฌ ๋ํ๋ 40-9",
                "road_address_name": "์์ธ ์๋๋ฌธ๊ตฌ ์ดํ์ฌ๋๊ธธ 7",
                "place_url": "http://place.map.kakao.com/17811924"
            }
        ]
    }
    ```

</div>
</details>

<details>
<summary><b>[GET] ์นด๊ณต์ง์๋ก ์ ๋ ฌ๋ ์นดํ ๋ฆฌ์คํธ ์กฐํ (์ธํจ)<b></summary>
<div markdown="1">   

<br>
์๋ก์ด ํ์ด์ง๋ ์ง๋ ์์ ์ฌ๋ผ์ด๋๋ก ํ์ ์ด ๋์ ๊นํ ์์ผ๋ก ์๋, ๊ฒฝ๋, ์นดํ ์ด๋ฆ ๋ฐํํฉ๋๋ค. <br><br>

<img width="300" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b3223d6c-0d6f-4d29-a4b6-4b878bcb6400/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T012725Z&X-Amz-Expires=86400&X-Amz-Signature=d44d401fd6900f79e7c218cbbf2d660b190d20dd0052cde3a65161f5fedf4276&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" />

```
[GET] /cafes/sorted?latitude=12345678901234&longitude=12345678901234
```

- **Response Body**

    ```json
    {
        "success": true,
        "data": [
            {
                "id": "806447073",
                "place_name": "ํฌ์ธํ๋ ์ด์ค ์ด๋์ญ์ ",
                "latitude": "37.5572360514845",
                "longitude": "126.94569812655",
                "avg_star": 3.5
            },
            {
                "id": "1866064248",
                "place_name": "์นดํ๋ด๋ด ์ดํ์ฌ๋์ ",
                "latitude": "37.55722067043155",
                "longitude": "126.94555893119713",
                "avg_star": "false"
            },
            {
                "id": "19622085",
                "place_name": "๊ณต์ฐจ ์ด๋์ ",
                "latitude": "37.5569764014276",
                "longitude": "126.945345206914",
                "avg_star": "false"
            },
            {
                "id": "438330961",
                "place_name": "ํํ๋น ์ด๋์ ",
                "latitude": "37.5571243278597",
                "longitude": "126.945698207623",
                "avg_star": "false"
            },
            {
                "id": "13127567",
                "place_name": "์นดํ์ฅฌ๋",
                "latitude": "37.5572832629733",
                "longitude": "126.946485798103",
                "avg_star": "false"
            },
            {
                "id": "1595131797",
                "place_name": "์ปคํผ๋ฒ ์ด ์ด๋์ญ์ ",
                "latitude": "37.55650794784634",
                "longitude": "126.945485885993",
                "avg_star": "false"
            },
            {
                "id": "10368507",
                "place_name": "๋ผ๋ฐ์ง ์ด๋์ ",
                "latitude": "37.5574344119916",
                "longitude": "126.946005822281",
                "avg_star": "false"
            },
            {
                "id": "213867029",
                "place_name": "๋ค์ธ์ ํต์ฐป์ง",
                "latitude": "37.556443159523",
                "longitude": "126.945667012953",
                "avg_star": "false"
            },
            {
                "id": "23040316",
                "place_name": "๋ฐ์นด๋ผ",
                "latitude": "37.55606405286577",
                "longitude": "126.9461324344883",
                "avg_star": "false"
            },
            {
                "id": "17811924",
                "place_name": "์ด์ง์จ์ด ์ด๋์ ",
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
<summary><b>[GET] ์นดํ ๋ฉ์ธ ์ ๋ณด ์กฐํ (์์)<b></summary>
<div markdown="1">   

<br>
ํด๋น ์นดํ์ ๋ฉ์ธ ์ ๋ณด๋ฅผ ์กฐํํฉ๋๋ค. <br><br>

<img width="300" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5013dd11-114f-48b6-a1a3-c17193efab45/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T012900Z&X-Amz-Expires=86400&X-Amz-Signature=401ba0a2b54580aa2a6405c08037e00f0dcd92e392e37202259c636f33e56b59&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" />

```
[GET] /cafes/{cafe-id}
```

- Response Body
    - ์ฑ๊ณต 1

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

    - ์ฑ๊ณต 2

        ```json
        // 8119644
        {
            "success": true,
            "data": {
                "id": 8119644,
                "name": "ํ๋ฆฐ์ธ์ค๋ค์ด์ด๋ฆฌ",
                "cnt_review": 0,
                "avg_star": null,
                "avg_noise": null,
                "avg_light": null,
                "avg_chair": null,
                "thumbnail": "https://~.png"
            }
        }
        ```

    - ์คํจ

        ```json
        {
            "success": false,
            "message": "์นดํ ์ ๋ณด๊ฐ ์กด์ฌํ์ง ์์ต๋๋ค."
        }
        ```

</div>
</details>


<details>
<summary><b>[GET] ์นดํ ์์ธ ์ ๋ณด ์กฐํ (์์)<b></summary>
<div markdown="1">   

<br>
์นดํ์ ์์ธ ์ ๋ณด๋ฅผ ์กฐํํฉ๋๋ค. (์ฒซ ๋ฒ์งธ ํญ)<br>

<img width="300" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/211b7922-6808-4d00-b44b-c6403f9a5a23/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T013130Z&X-Amz-Expires=86400&X-Amz-Signature=04ec03a6e550666ccdfe51fc5a3381d70fac6ac3284c6885ebaae6c053c8a98c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" />

```
    
[GET] /cafes/{cafe-id}/info

```

- **Response Body**
    - **์ฑ๊ณต**

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
                "review": "์ํธ"
            }
        }
        ```

    - **์ฑ๊ณต (์นดํ ์ ๋ณด๋ง ์๋ ๊ฒฝ์ฐ)**

        ```json
        // 8119644
        {
            "success": true,
            "data": {
                "id": 8119644,
                "name": "ํ๋ฆฐ์ธ์ค๋ค์ด์ด๋ฆฌ",
                "phone": "012002",
                "address": "์์ธํน๋ณ์ ์๋๋ฌธ๊ตฌ",
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

    - **์คํจ (์นดํ ์ ๋ณด ์์ฒด๊ฐ DB์ ์๋ ๊ฒฝ์ฐ)**

        ```json
        {
            "success": false,
            "message": "์นดํ ์ ๋ณด๊ฐ ์กด์ฌํ์ง ์์ต๋๋ค."
        }
        ```

</div>
</details>


<details>
<summary><b>[GET] ์นดํ ๋ฆฌ๋ทฐ ๋ชฉ๋ก ์กฐํ (์ธํจ)<b></summary>
<div markdown="1">   

<br>
ํด๋น ์นดํ์ ๋ฆฌ๋ทฐ ๋ชฉ๋ก์ ์กฐํํฉ๋๋ค. (๋ ๋ฒ์งธ ํญ)<br>

<img width="300" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/eee6c260-d923-4733-a4ae-f75a4bea5bca/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T013444Z&X-Amz-Expires=86400&X-Amz-Signature=868ffa816565304d5c17c715f4e306432408d24d2c346532789546b0da63425e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" />

```
[GET] /cafes/{cafe-id}/reviews 
```

- **Response Body**

    ```json
    {
      "success": "true",
      "data": [
        {
          "star": 1,
          "detail": "์ํธ"
        },
        {
          "star": 4.5,
          "detail": "์ฑ๊ณต์ด๋ค"
        },
        {
          "star": 3.5,
          "detail": "๋ค ์ข์ง๋ง ํ์ฅ์ค์ด ๋ณ๋ก๋ค"
        },
        {
          "star": 2.5,
          "detail": "ํฌ์คํธ๋งจ ํ์คํธ"
        },
        {
          "star": 2.5,
          "detail": "ํฌ์คํธ๋งจ ํ์คํธ"
        },
        {
          "star": 2.5,
          "detail": "ํฌ์คํธ๋งจ ํ์คํธ"
        },
        {
          "star": 3.5,
          "detail": "๋ค ์ข์ง๋ง ํ์ฅ์ค์ด ๋ณ๋ก๋ค"
        },
        {
          "star": 3.5,
          "detail": "๋ค ์ข์ง๋ง ํ์ฅ์ค์ด ๋ณ๋ก๋ค"
        },
        {
          "star": 3.5,
          "detail": "๋ค ์ข์ง๋ง ํ์ฅ์ค์ด ๋ณ๋ก๋ค"
        },
        {
          "star": 4,
          "detail": "์ํธ"
        },
        {
          "star": 4,
          "detail": "์ํธ"
        },
        {
          "star": 3.5,
          "detail": "์ํธ"
        },
        {
          "star": 1,
          "detail": "์ํธ"
        }
      ]
    }
    ```
</div>
</details>



<details>
<summary><b>[GET] ์นดํ ์ด๋ฏธ์ง ๋ชฉ๋ก ์กฐํ (์์)<b></summary>
<div markdown="1">   

<br>
ํด๋น ์นดํ์ ์ด๋ฏธ์ง๋ค์ ์กฐํํฉ๋๋ค. (์ธ ๋ฒ์งธ ํญ)<br>

<img width="300" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d73cfb28-e59a-43ac-beb7-52e74e335879/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T013524Z&X-Amz-Expires=86400&X-Amz-Signature=06fc2076c602760d423416763ca3de188e9027a9e825a0ccb1b68250366c0b03&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" />

```
[GET] /cafes/{cafe-id}/images
```

- **Response Body**
    - **์ฑ๊ณต**

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

    - **์คํจ**

        ```json
        {
            "success": false,
            "message": "์ด๋ฏธ์ง ์กด์ฌํ์ง ์์ต๋๋ค."
        }
        ```

</div>
</details>



<details>
<summary><b>[GET] ์นดํ ๋ฉ๋ด ์กฐํ (์์)<b></summary>
<div markdown="1">  

<br>
ํด๋น ์นดํ์ ๋ฉ๋ด๋ฅผ ์กฐํํฉ๋๋ค. (๋ค ๋ฒ์งธ ํญ)<br>

<img width="300" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d8af312a-7c7b-4bc9-b5a7-6596e8604815/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T013603Z&X-Amz-Expires=86400&X-Amz-Signature=2f4239cf3de97274802dca97c1b42d6f65d9d126ed5b3d1ae9296d5cfd89f909&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" />

```
[GET] /cafes/{cafe-id}/menus
```

- **Response Body**
    - **์ฑ๊ณต**

        ```json
        {
            "success": true,
            "data": [
                {
                    "menu": "๋์ฝ์ธ ๋ผ๋ฉ",
                    "price": 6000
                },
                {
                    "menu": "์นด๋ผ๊ท๋ผ๋ฉ",
                    "price": 6000
                },
                {
                    "menu": "์ฏ์ผ๋ฉด",
                    "price": 6000
                },
                {
                    "menu": "์ฟ ๋ก ๋ผ๋ฉ",
                    "price": 6000
                },
                {
                    "menu": "์์นด์ผ ์ผ๋ผ๋ผ๋ฉ",
                    "price": 6000
                }
            ]
        }
        ```

    - ์คํจ

        ```json
        {
            "success": false,
            "message": "๋ฉ๋ด ์ ๋ณด๊ฐ ์กด์ฌํ์ง ์์ต๋๋ค."
        }
        ```

</div>
</details>


<details>
<summary><b>[POST] ์ด๋ฏธ์ง ๋ฆฌ์คํธ ์๋ก๋ (์์) <b></summary>
<div markdown="1">   

<br>

๋ฆฌ๋ทฐ ์์ฑํ  ๋, ์ด๋ฏธ์ง๋ฅผ ์ฒจ๋ถํ๋ ๊ฒฝ์ฐ API๋ฅผ ํธ์ถํฉ๋๋ค. <br>
์ด๋ฏธ์ง url ๋ฆฌ์คํธ๋ฅผ ๋ฐ์ `๋ฆฌ๋ทฐ ์์ฑ API` ๋ฅผ ํธ์ถํ  ๋ Request Body์ ๋ด์ต๋๋ค. <br>

<img width="300" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/97de5d3b-26b0-4dac-b569-176d2dc4aa4e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T013638Z&X-Amz-Expires=86400&X-Amz-Signature=f4887f1977b5ceb23e3318d4761eb6264c362ef9a46aaf14c4191fcdd334d896&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" />

<br>

```
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
    form-data file๋ก ์ ์ก 
    key๋ file๋ก ์ค์ 
    ```

    ์์

    ![image](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a5c59705-0fd2-4347-bb50-e36b18bc6e28/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210711T022044Z&X-Amz-Expires=86400&X-Amz-Signature=e6037dcb6e212a3d40c5779fe5dc7df3b83590d1e8256bf25fe8c6e3c54e7b7f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

- **Response Body**

    ์ด๋ฏธ์ง url ๋ฆฌ์คํธ๋ฅผ ๋ฐํํฉ๋๋ค.

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
<summary><b>[POST] ๋ฆฌ๋ทฐ ์์ฑ (์์)<b></summary>
<div markdown="1">   

<br>

id๊ฐ `{cafe-id}`์ธ ์นดํ์ ์นด๊ณต ํ๊ธฐ๋ฅผ ์์ฑํฉ๋๋ค.<br>

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
    		"detail": "์ต๊ณ ",
        "imageList": [
            "https://~.jpeg"  
        ]   
    }
    ```

- **Response Body**
    - **์ฑ๊ณต**

        ```json
        {
            "success": true
        }
        ```

    - **์คํจ (๋ณ์  ์๋ ๊ฒฝ์ฐ)**

        ```json
        {
            "success": false,
            "message": "๋ณ์  ์๋ ฅํด์ฃผ์ธ์."
        }
        ```

</div>
</details>

<br><br>
    
## ๐คฉ Backend Member

<table>
  <tr>
    <td align="center"><a href="https://github.com/PARKINHYO"><img src="https://avatars.githubusercontent.com/u/47745785?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Inhyo</b></sub></a><br/></td>
    <td align="center"><a href="https://github.com/ayoung0073"><img src="https://avatars3.githubusercontent.com/ayoung0073?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ayoung</b></sub></a><br/></td>
  </tr>
</table>
    
<br><br>

## ๐ License

Copyright ยฉ 2021 [GDG-Summer-Hackathon-Group12](https://github.com/GDG-Summer-Hackathon-Group12).<br/>
This project is [MIT](https://github.com/GDG-Summer-Hackathon-Group12/serverless-backend/blob/main/LICENSE) licensed.
***
_This README was generated with โค๏ธ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_

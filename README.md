# wanted_pre_onboarding
<br/>

원티드 프리온보딩에 참여하기 위해 작성한 코드를 업로드하는 repository 입니다.



## 1. 서비스 개요

- 본 서비스는 기업의 채용을 위한 웹 서비스 입니다.
- 회사는 채용공고를 생성하고, 이에 사용자는 지원합니다.
<br/>

## 2. 구현
  JobPost 앱에서는 채용정보들을 등록, 수정, 삭제하는 기능을 구현하였습니다.
  ### 채용 등록,수정,삭제
  
  * ModelViewSet을 사용하여 CRUD를 한번에 구현하였습니다.

  회사는 
  * ```GET /job_post/``` 에서 등록된 정보를 확인할 수 있고, 채용정보를 post할 수 있습니다.
  * id를 기준으로 상세페이지에 접근할 수 있으며, 
  * 상세페이지에서는 수정, 삭제를 할 수 있습니다. <br/>
    ```PUT /job_post/<id>```에서 정보를 update할 수 있고,  ```Delete /job_post/<id>``` 에서 정보를 delete할 수 있습니다.<br/>
  * 응답 <br/>
    성공했을 시 HTTP 200 OK 으로 응답하며, 실패했을 시 HTTP 404 Not Found으로 응답합니다.
    
```
[
    {
        "id": 1,
        "position": "Junior Django Developer",
        "compensation": 1000000,
        "description": "Wanted Lab hires backend junior developers",
        "skills": "python, django, docker"
    },
    {
        "id": 2,
        "position": "React Junior Developer",
        "compensation": 2000000,
        "description": "Wanted Lab hire frontend developers",
        "skills": "javascript,react"
    }
]
```
<hr/>
JobOpen 앱에서는 채용목록을 조회하는 기능과 검색기능을 구현했습니다.

  ### 채용 목록 조회
  ``` GET /list/ ```<br/>
  사용자는 채용 목록을 조회할 수 있습니다. 
  ```
  [
    {
        "id": 1,
        "company": "Wanted Lab",
        "country": "Korea",
        "region": "Seoul",
        "position": "Junior Backend",
        "skills": "python, java"
    },
    {
        "id": 2,
        "company": "Naver",
        "country": "Japan",
        "region": "Tokyo",
        "position": "Frontend Senior developer",
        "skills": "react"
    }
  ]
  ```
  
  ### 채용 상세페이지
  
  사용자는 채용 상세페이지에서 채용 내용인 description 필드와 채용보상금인 compensation 필드의 정보를 추가적으로 볼 수 있습니다.  
  
  목록을 정의한 Serializer와 상세페이지를 정의한 Serializer를 나누어 작성하여 구현하였습니다. 
  ```
  {
    "id": 1,
    "company": "Wanted Lab",
    "country": "Korea",
    "region": "Seoul",
    "position": "Junior Backend",
    "compensation": 10000000,
    "description": "blablablabla",
    "skills": "python, java"
}
  ```
  
  
  ### 채용 공고 검색 기능
  
  사용자는 
  * 검색하여 원하는 조건에 해당한는 검색결과를 얻을 수 있습니다. <br/>
  * 검색기능은 ListAPIView에서 SearchFilter로 구현하였으며, 
    검색할 수 있는 필드는 아래와 같습니다.
  
  ```
  search_fields = ['company','country','region','position','skills']
  ```
  
  seoul을 검색했을 시, 다음과 같은 정보를 얻을 수 있습니다.
  
  ```GET /list/?search=seoul```
  
```
[
    {
        "id": 1,
        "company": "Wanted Lab",
        "country": "Korea",
        "region": "Seoul",
        "position": "Junior Backend",
        "skills": "python, java"
    },
    {
        "id": 3,
        "company": "Korean Lab",
        "country": "Korea",
        "region": "Seoul",
        "position": "Senior backend developer",
        "skills": "javascript, java"
    }
]
```
  
  
  ### 

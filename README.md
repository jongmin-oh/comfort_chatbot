## 인공지능 위로 챗봇 오복이

#### history

오복이는 대학교 4학년 졸업작품 수업에 의해 탄생하게 되었습니다.<br>
개인 프로젝트로 진행했는데, 기왕이면 재미있고 비개발자(일반인)도 이용해 볼 수 있는 서비스를 만들고 싶었습니다.<br>
무엇보다도 공개된 데이터가 있었고 챗봇 개발자로써 나만의 챗봇을 개발하고 싶었습니다.<br>
 
 ## "오복이"소개
 
![obok](https://github.com/jongmin-oh/comfort_chatbot/assets/23625693/6cacc048-9994-4f5e-a745-fecae1dbc1a3)

- 이름 : 오복이
- 직업 : 심리상담사
- 종류? : 물범

> TMI : 오복이는 이름 지을 당시 고깃집에서 "오복 가위"를 들고있어서 탄생하게 되었다.

| 일상대화 예시                                       | 고민대화 예시                                       |
|----------------------------------------------------|------------------------------------------------------|
| <div align="center"><img src="assets/일상.jpeg" width="75%" /></div> | <div align="center"><img src="assets/고민.jpeg" width="75%" /></div> |

***

소개글 : 
"위로봇 오복이"는 인공지능 비서가 아닙니다. <br>
오복이는 내가 한 질문에 대해 위로로 답변해주는 감성 대화 챗봇입니다.<br><br>

오복이는 정해진 시나리오로 답변하지 않습니다.(룰 기반이 아닙니다) <br>
(직접구현한 API를 통해 답변합니다.) <br>
~~직접 구현한 API + Generative AI 를 통해 답변합니다.~~ <br><br>

오복이의 기본 알고리즘은  검색을 통해 질문과 가장 유사한 질문을 찾아 그의 해당하는 답변을 해줍니다<br>
오복이는 이전 대화의 문맥을 파악하지 못합니다(싱글턴 챗봇), 사용자가 질문한 문장만 보고 적절한 대답을 합니다.<br><br>

캐릭터 이미지는 Open-AI의 인공지능 “DALL-E”가  생성한 이미지입니다. <br>
다른이미지를 쓰려다 저작권 문제가 있어 직접생성한 이미지를 사용했습니다. <br>



### 웹사이트
 - Streamlit 으로 간단하게 구현하였습니다.
> 위로봇 : [웹사이트](https://comfort.j5ng.com/)

### 카카오톡 채널 & 오픈빌더

 - 프론트엔드 플랫폼으로 카카오톡 채널을 이용했습니다.
 - 벡엔드와 인공지능 알고리즘에 좀 더 집중하기 위해서 사용했습니다.
 - 졸업작품 프로젝트가 끝나고도 계속 유지보수 할 계획이기 때문에 사용자 접근성이 쉬운 카카오톡 채널을 이용했습니다.
 - 카카오톡 채널 챗봇은 얼마전 무료화를 선언 과금에 대한 부담이 없어 사용하였습니다.

> 위로봇 : 카카오톡 채널 홈
http://pf.kakao.com/_BNZRb

### 클라우드 서버

 - ~~배포를 하려면 서버가 필요한데 일단 구글 클라우드 플랫폼(GCP)의 무료 3개월 크리딧을 사용했습니다.~~
 - ~~인스턴스 : e2-medium~~
      ~~CPU : 2-core , 메모리 : 4GB~~
 
2023.03.29 AWS 예약 인스턴스로 교체
 - *계속 서비스할 생각으로 예약 인스턴스(1년치)를 사비로 구매하였습니다.
 - **33만원 비용발생 ㅠㅠ**
 
### EC2 인스턴스
- t3a-medium
- CPU : 2-core , 메모리 : 4GB
- Storage(EBS) : 20GB
- OS : Amazon Linux

### 웹 프레임워크

- FastAPI
- Gunicorn

선정 이유 :
1. Python 기반 웹 프레임 워크
2. 다른 프레임워크에 비해 속도가 가장빠른(Python 기준)
3. 회사에서 사용하기 때문에 익숙함.
4. ORM 지원

***

## 오복이 개발 로그
### 최종 수정일 2023.09.30

#### 오복이 v1.0 배포 ( 2022.11.30 )
  - 엘라스틱 서치 기반 키워드 검색 알고리즘
  - nori 형태소 분석기 사용
  - 10만개의 답변 후보 사용

#### ~~Pingpong API 연동~~ (2022.12.10)
  - ~~스캐터랩의 pingpong 챗봇 빌더를 만들어 오복이 패르소나 연결~~
  - ~~일상적인 질문을 대체함~~
  - ~~10만개에서 찾지못한 질문은 핑퐁AI가 처리하도록 설계~~
  - 핑퐁 챗봇 서비스 종료(2023.08.30)
  
#### 오복이 v2.0 배포 (2023.02.10)
  - 엘라스틱 서치 -> 딥러닝 기반(Sbert) 검색으로 변경
  - Sparse Vector -> Dense vector
  - 키워드 기반 검색 알고리즘에서 문장 임베딩 기반 검색 알고리즘으로 변경
  - klue/roberta-base 의 korSTS/NLI를 파인튜닝한 sbert 모델
  
#### 임베딩 모델 변경 (2023.03.05)
   - klue/roberta-base -> snunlp/KR-SBERT-V40K-klueNLI-augSTS
   - 데이터 증량기법을 사용해 재학습한 모델로 변경

#### ~~인스턴스 내 RDB PostgreSQL 구축 (2023.03.06)~~
- ~~csv 데이터를 Pandas로 불러와서 답변을 찾는 방식에서 PostgreSQL RDBMS 를 통해 답변  Table을 만들어 fetch 해서 사용하게 변경~~
- ~~시간이 조금 늘어나지만 메모리 절약(답변 DB를 메모리에서 계속 들어있지 않음)~~
- ~~사용자가 질문한 내용과 "오복이"가 답변한 답변 로그를 DB에 수집~~
- ChromaDB가 Metadata 같이 처리하게 수정, 로그 수집 하지않음(2023.09.30)

#### Top-K sampling 적용(2023.03.11)

#### AWS 예약 인스턴스로 교체(2023.03.29)
 : GCP 3개월 무료 크레딧 만료 -> AWS 예약 인스턴스 구매

#### 벡터 검색 최적화(2023.04.10)
 1.Faiss 유사도 검색 알고리즘 적용
 2.Faiss PQ 벡터 양자화 적용
   - 임베딩 벡터 메모리 1/4로 감소
   - 유사도 계산 속도 향상 
 3. 핑퐁 답변 유무의 따른 임계치 때문에 유클리디언 거리가 아닌 벡터의 내적으로 계산함.
  

#### 임베딩 모델 최적화(2023.04.10)
 1. Torch 모델에서 -> ONNX 모델 uint8 양자화 모델로 변경
  - 임베딩 속도 7배 향상
  - 모델 크기 1/4로 감소
  - 서버 CPU 부하 감소
  - 정확도 차이 거의 없음 dot score +- 0.02 이하 

#### ~~생성 AI 도입(2023.05.01)~~
 - ~~Naver Hyper Clova API 연동~~
 - ~~Open AI ChatGPT 연동 ***카카오톡 채널 적용 불가**~~
 - 임계치가 이하인 경우 생성AI가 대신 답변했지만, 과금 문제, 악성 유저 예방을 위해 사용 중지(2023.09.30)

#### 오복이 답변 데이터 재구축(2023.06.11)
 - 현재 검색모델의 답변데이터(3만개)가 너무 짧은 답변을함.
 - 해결과 위로보다는 약간의 공감만 해줌( 성의가 없음 )
 - 데이터 수를 줄이더라도 퀄리티있는 답변을 제공해야겠다는 생각이 들었음
 - 하이퍼 클로바가 생성한 문장을 내가 직접 검수해서 답변 데이터로 사용함.

#### 오복이 답변 데이터 재구축 완료(2023.09.30)
 - Chatgpt, HyperClova 사용해서 답변 재구축
 - 좀 더 성의있는 답변과 해결책을 제시하도록 수정
 - 중복되는 질문 최대한 제거
 - 최종 35,363건의 데이터 재구축

#### BM25 키워드 검색 도입(2023.10.10)

#### 답변 추론 프로세스 변경(RRF)
 - Reciprocal rank fusion 점수 반영
 - BM25(키워드) & 딥러닝 모델(임베딩) 점수 랭킹 하이브리드 결합
 - 0~1 사이의 값으로 맵핑

#### 오복이 웹사이트 배포 (2023.10.10)
 - Streamlit 프레임워크 사용

#### 오복이 웹사이트 https 적용 (2023.10.10)
 - 도메인 구매
 - AWS CloudFront 활용하여 https 보안 프로토콜 적용

***

### 서비스 이슈

#### 반복적인 질문을 계속하는 악성 유저(2023.07.01)
 - 한 유저가 계속 똑같은 내용의 질문을 반복함. ( 00은 00을 좋아한다 )
 - 유저 차단으로 일단락했지만, 반복되는 질문에 대한 차단과, 유저별로 하루 request 제한을 두는 방안을 생각중

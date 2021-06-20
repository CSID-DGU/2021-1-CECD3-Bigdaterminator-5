# 2021-1-CECD3-Bigdaterminator-5
### NLP 감성 분석에 기반한 온라인 커뮤니티 이슈 키워드 모니터링 시스템 <br><br>

# About Us
*Team BIGDATERMINATOR*
* 강우원(팀장)
* 김소연
* 김다윤
* 정용헌 <br><br>

# 사용 방법
예시) 네이트판
1. natepann.ipynb 실행
2. 분석(키워드).ipynb 실행
3. 네이트판_감성분석.ipynb 실행
<br><br>

# 개발 목표
많은 사용자가 이용하는 온라인 커뮤니티 4곳(네이트판, FM 코리아, 루리웹, 클리앙)의 인기 게시물을 크롤링하여, 이슈 키워드 뿐만 아니라 이에 대한 감성 분석 결과를 수치화 및 시각화하여 제공하는 소프트웨어를 개발하고자 한다. <br>
추후 카카오톡 플러스친구 구독 형태로 만든 챗봇에서, 매일 push를 보내주는 방식의 프로그램을 개발하는 것을 목표로 한다. <br><br>

# 개념 설계

![image06](https://user-images.githubusercontent.com/48827431/122660322-8f685100-d1bb-11eb-800e-da2a1578f6f9.png)

* 선정한 4가지 온라인 커뮤니티 게시판에서 제목,본문,댓글을 크롤링하여 1~10위 이슈 키워드 추출
* 10가지 이슈 키워드가 포함된 제목,본문,댓글만 다시 수집하여 전처리 진행
* 전처리 된 데이터에 대한 감성분석 진행 후, 그 결과를 시각화하여 제공 <br><br>

# 진행 결과물
1. TF-IDF 텍스트 마이닝 기법을 사용하여, 각 커뮤니티에서 가장 이슈가 되는 키워드 10가지를 추출한다. <br>
예시) 네이트판

![image01](https://user-images.githubusercontent.com/48827431/122660202-7b701f80-d1ba-11eb-9777-1f53198180b4.png)

2. 각 키워드가 속한 제목, 본문, 댓글 데이터를 모두 추출하여 감성 분석에 활용할 수 있도록 전처리를 진행한다.

![image02](https://user-images.githubusercontent.com/48827431/122660226-d6a21200-d1ba-11eb-927b-cd46ab64157d.png)

3. 전처리한 데이터에 대한 감성 분석을 진행하여 긍정, 부정, 중립 감성 점수를 계산하여 반환한다.

![image03](https://user-images.githubusercontent.com/48827431/122660231-e02b7a00-d1ba-11eb-96d3-72bc3452fab0.png)

4. 반환된 감성 분석 결과를 수치화 및 시각화하여 시스템 사용자에게 제공한다.

![image04](https://user-images.githubusercontent.com/48827431/122660237-e7eb1e80-d1ba-11eb-950d-27c000df82e6.png)


5. 최종 결과물 예시 목업 : 추후 카카오톡 플러스친구 구독 형태로 만든 챗봇을 개발하는 것을 목표로 한다.


![image05](https://user-images.githubusercontent.com/48827431/122660238-ea4d7880-d1ba-11eb-84c3-81d927012da0.PNG) <br><br>

# 개발 환경

![image07](https://user-images.githubusercontent.com/48827431/122660407-48c72680-d1bc-11eb-986f-57e0f945e568.PNG)

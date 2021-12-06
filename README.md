# 2021-CECD3-Bigdaterminator-5
### 온라인 커뮤니티 특화 감성 사전 구축을 위한 새로운 용어 극성값 분석 시스템 <br><br>

# About Us
*Team BIGDATERMINATOR*
* 강우원
* 김다윤
* 김소연
* 정용헌 (1학기까지 진행)<br><br>

# 사용 방법
진행 중
<!-- 예시) 네이트판
1. natepann.ipynb 실행
2. 분석(키워드).ipynb 실행
3. 네이트판_감성분석.ipynb 실행 -->
<br><br>

# 개발 목표
온라인 커뮤니티에서 사용되는 용어들은 형태가 다양할 뿐만 아니라 나날이 그 수가 증가하고 있기 때문에, 범용적으로 사용되는 감성 사전을 사용했을 때 없는 단어로 인식되어 극성값이 중립으로 나오는 경우가 많다. 따라서 감성 사전에 존재하지 않는 새로운 커뮤니티 용어의 주변 단어를 탐색한 후 이들의 극성값을 통계 내서 제공하여, 사용자가 새로운 커뮤니티 용어에 대한 극성값을 판단하는 데 도움이 되는 시스템을 제안한다. <br><br>

# 개념 설계

<!-- ![image06](https://user-images.githubusercontent.com/48827431/122660322-8f685100-d1bb-11eb-800e-da2a1578f6f9.png) -->

* NatePann 온라인 커뮤니티 게시판에서 제목과 본문을 크롤링
* 크롤링한 데이터과 knu 감성 사전을 비교하여, 감성 사전에 존재하지 않는 새로운 용어 모두 추출
* kiwipiepy 라이브러리를 적용하여 최종적으로 새로운 용어 후보들 추출
* 추출된 새로운 용어들에 FastText 기법을 적용하여 주변 단어 탐색
* 주변 단어들의 극성값을 통계 내서 사용자에게 제공 <br><br>

 # 최종 결과물
👉[웹 서비스 Git](https://github.com/claudia825/BigDataTerminator_WEB) <br>
https://github.com/claudia825/BigDataTerminator_WEB

<!--  웹 서비스 이미지 넣기 -->

<!-- # 진행 결과물
1. NatePann 온라인 커뮤니티에서  <br>
예시) 네이트판

![image01](https://user-images.githubusercontent.com/48827431/122660202-7b701f80-d1ba-11eb-9777-1f53198180b4.png)

2. 각 키워드가 속한 제목, 본문, 댓글 데이터를 모두 추출하여 감성 분석에 활용할 수 있도록 전처리를 진행한다.

![image02](https://user-images.githubusercontent.com/48827431/122660226-d6a21200-d1ba-11eb-927b-cd46ab64157d.png)

3. 전처리한 데이터에 대한 감성 분석을 진행하여 긍정, 부정, 중립 감성 점수를 계산하여 반환한다.

![image03](https://user-images.githubusercontent.com/48827431/122660231-e02b7a00-d1ba-11eb-96d3-72bc3452fab0.png)

4. 반환된 감성 분석 결과를 수치화 및 시각화하여 시스템 사용자에게 제공한다.

![image04](https://user-images.githubusercontent.com/48827431/122660237-e7eb1e80-d1ba-11eb-950d-27c000df82e6.png)


5. 최종 결과물 : 웹페이지
👉[온라인 커뮤니티 특화 감성 사전 구축을 위한 새로운 용어 극성값 분석 시스템](https://github.com/claudia825/BigDataTerminator_WEB)

# 개발 환경

![image07](https://user-images.githubusercontent.com/48827431/122660407-48c72680-d1bc-11eb-986f-57e0f945e568.PNG) -->

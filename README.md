# 2021-CECD3-Bigdaterminator-5
### 온라인 커뮤니티 특화 감성 사전 구축을 위한 새로운 용어 극성값 분석 시스템 <br><br>

# About Us
*Team BIGDATERMINATOR*
* 강우원
* 김다윤
* 김소연 <br><br>


# 개발 목표
온라인 커뮤니티에서 사용되는 용어들은 형태가 다양할 뿐만 아니라 나날이 그 수가 증가하고 있기 때문에, 범용적으로 사용되는 감성 사전을 사용할 경우, 존재하지 않는 용어로 인식되어 극성값이 중립으로 나오는 경우가 많다. 본 시스템은 이러한 문제점을 해결하기 위해, 감성 사전에 존재하지 않는 커뮤니티 신조어의 연관 용어들을 추출한 후, 신조어와 연관 용어가 포함된 텍스트를 감성 분석하고, 이를 기반으로 신조어의 극성값을 분석하는 기법을 제안한다. <br><br>

# 개념 설계

![image01](https://user-images.githubusercontent.com/70895824/145217126-27c63b83-602e-465e-9727-9acba9c8592c.png)

**1) 데이터 크롤링 및 전처리**
    - NatePann 온라인 커뮤니티 게시판에서 제목과 본문을 크롤링 후 데이터 전처리
**2) 신조어 및 연관 용어 추출기** 
    - KNU 한국어 감성 사전에 존재하지 않는 미등록어 모두 추출
    - kiwipiepy 라이브러리를 적용하여 해당 용어들 중 명사 형태에 가장 가까운 용어들을 신조어 후보로 추출
    - Word2vec과 FastText를 활용하여 코사인 유사도가 0.90 이상인(거리가 가까운) 단어를 연관 용어로 추출
**3) 감성 분석기**
    - 연관 용어와 신조어가 함께 출현하는 문장을 모두 추출한 후 감성 분석 진행
**4) 극성값 추출기** 
    - 감성 분석 결과를 미리 선정한 기준에 따라 분류하여 신조어에 극성값 부여
**5) 시각화** 
    - 신조어의 극성값을 수치화 및 시각화하여 사용자에게 제공 <br><br>

# 사용 방법
진행 중
<!-- 예시) 네이트판
1. natepann.ipynb 실행
2. 분석(키워드).ipynb 실행
3. 네이트판_감성분석.ipynb 실행 -->
<br><br>

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

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

**1) 데이터 크롤링 및 전처리**<br>
  - NatePann 온라인 커뮤니티 게시판에서 제목과 본문을 크롤링 후 데이터 전처리<br>
**2) 신조어 및 연관 용어 추출기**<br>
  - KNU 한국어 감성 사전에 존재하지 않는 미등록어 모두 추출<br>
  - kiwipiepy 라이브러리를 적용하여 해당 용어들 중 명사 형태에 가장 가까운 용어들을 신조어 후보로 추출<br>
  - Word2vec과 FastText를 활용하여 코사인 유사도가 0.90 이상인(거리가 가까운) 단어를 연관 용어로 추출<br>
**3) 감성 분석기**<br>
  - 연관 용어와 신조어가 함께 출현하는 문장을 모두 추출한 후 감성 분석 진행<br>
**4) 극성값 추출기**<br>
  - 감성 분석 결과를 미리 선정한 기준에 따라 분류하여 신조어에 극성값 부여<br>
**5) 시각화**<br>
  - 신조어의 극성값을 수치화 및 시각화하여 사용자에게 제공 <br>


# 진행 결과물
1. NatePann 온라인 커뮤니티에서 데이터 크롤링을 시작할 날짜를 입력한다.  <br>

![image02](https://user-images.githubusercontent.com/70895824/145220049-998e6f59-8313-49ac-93d4-5922737ea60e.png)

2. 추출된 신조어 후보에서 극성값 분석을 원하는 신조어를 입력한다.

![image03](https://user-images.githubusercontent.com/70895824/145220051-e8a55ad6-64e9-4f3a-aeb1-0e80941c4ee1.png)

3. 사용자가 입력한 신조어의 연관 용어가 추출된다. ex) 스우파

![image04](https://user-images.githubusercontent.com/70895824/145220054-2a28a205-0d68-4156-b864-047a8069b4f0.png)

4. 사용자가 입력한 신조어와, 신조어의 연관 용어가 포함된 문장이 모두 추출된다.

![image05](https://user-images.githubusercontent.com/70895824/145220058-af1e0625-3743-4c7b-96df-09256d6a131e.png)

5. 추출된 문장을 감성 분석하여, 최종적으로 신조어의 감성 분석 결과와 극성값을 사용자에게 제공한다.

![image06](https://user-images.githubusercontent.com/70895824/145220064-c9ad478d-da20-4014-b8e0-532f3cd8362c.png)


 # 최종 결과물
 👉[온라인 커뮤니티 특화 감성 사전 구축을 위한 새로운 용어 극성값 분석 시스템](https://github.com/claudia825/BigDataTerminator_WEB)

👉[웹 서비스 Git](https://github.com/claudia825/BigDataTerminator_WEB) <br>
https://github.com/claudia825/BigDataTerminator_WEB

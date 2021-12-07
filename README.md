# README

## 팀원 정보 및 업무 분담 내역

- 윤수현:
  - 전반적인 django, vue 개발 및 API 서버 끌어오기
  - Server AWS 배포, Client netlify 배포



- 서지원:
  - 전반적인 프론트, CSS 관리 및 주요 알고리즘 구현 총괄



- 정확히 어떤 파트를 맡아서 분업한다기 보다, 서로 겹치지 않게 작업 동선을 체크하면서 할 수 있는 것들을 순서대로 해나가는 방식을 택함. 서로 막히는 부분이 있으면 도움을 요청해 함께 디버깅을 함.





## 목표 서비스 구현 및 실제 구현 정도

1. 영화 추천 서비스 :
   - 사용자의 영화 찜 정보를 바탕으로 한 영화 추천
   - 사용자에게서 받은 키워드를 바탕으로 한 영화 추천
2. 영화 검색 기능 :
   - 사용자는 영화 제목이나 줄거리에 있는 키워드로 데이터 베이스에 있는 영화를 검색할 수 있음
   - 관리자는 tmdb에 있는 영화의 제목을 검색하면 받아올 수 있음
3. 사이트 사용자를 위한 영화 게시판 및 커뮤니티 :
   - 사용자들이 영화 리뷰, 혹은 영화 데이터 요청글을 적을 수 있는 게시판
   - 사용자들을 위한 커뮤니티 게시판
4. 기타 기능 :
   - 글에 댓글, 좋아요/싫어요를 누를 수 있는 기능
   - 게시판의 조회수







## 프로젝트 구조

### A. 프로젝트 구조

| Front Area(FINAL-PJT-BACK)                                   | Back Area(FINAL-PJT-FRONT)                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| back/<br />    asgi.py<br />    settings.py<br />    urls.py<br />    wsgi.py<br />    api<br />    tmdb.py<br />    tmdbsend.py<br />    accounts/<br />    migrations/<br />    profile/<br />    admin.py<br />    apps.py<br />    models.py<br />    serializers.py<br />    tests.py<br />    urls.py<br />    views.py<br />communities/<br />    migrations/<br />    admin.py<br />    apps.py<br />    models.py<br />    serializers.py<br />    tests.py<br />    urls.py<br />    views.py<br />movies/<br />    fixtures/<br />    migrations/<br />    admin.py<br />    apps.py<br />    models.py<br />    serializers.py<br />    tests.py<br />    urls.py<br />    views.py<br />movies/<br />    fixtures/<br />    migrations/<br />    admin.py<br />    apps.py<br />    models.py<br />    serializers.py<br />    tests.py<br />    urls.py<br />    views.py<br />static/<br />    images/<br />db.sqlite3<br />manage.py<br />requirements.txt<br />README.md | .history/<br />public/<br />src/<br />    assets/<br />    components/<br />       accounts<br />           TheChangeInformation.vue<br />           TheFollowersMovie.vue<br />           TheFollowingsMovie.vue<br />           TheLikeMovies<br />           TheMyBoards.vue<br />           TheProfileMylinks.vue<br />           TheUserLike.vue<br />        admin/<br />           TheMovieList.vue<br />           TheMovieListItem.vue<br />           TheMovieSearch.vue<br />        boards/<br />           TheBoardLike.vue<br />           TheBoardList.vue<br />           TheBoardListItem.vue<br />           TheCommentForm.vue<br />           TheCommentListItem.vue<br />           TheGenreList.vue<br />           TheGenreListItem.vue<br />           TheRankingBoard.vue<br />           TheRankingFollower.vue<br />           TheRankingGenre.vue<br />           TheRankingMovie.vue<br />        genresearch/<br />           TheGenreList.vue<br />           TheGenreListItem.vue<br />           TheGenreSearchList.vue<br />           TheGenreSearchListItem.vue<br />        movies/<br />           TheDetailGenre.vue<br />           TheMovieLIke.vue<br />           TheMovieSame.vue<br />           TheMovieService.vue<br />           TheMovieStar.vue<br />           TheMovieStarForm.vue<br />           TheMovieStarItem.vue<br />           TheMovieYoutube.vue<br />        search<br />           SearchItem.vue<br />    http/<br />    router/<br />    store/<br />    views/<br />        accounts/<br />           Login.vue<br />           Profile.vue<br />           Signup.vue<br />           TheFollowers.vue<br />           TheFollowings.vue<br />           UserSearch.vue<br />        admin/<br />           Movie.vue<br />           MovieList.vue<br />       boards/<br />           BoardCreate.vue<br />           BoardDetail.vue<br />           Boards.vue<br />           BoardUpdate.vue<br />           RankingBoard.vue<br />        genressearch/<br />           GenreSearch.vue<br />        keywords/<br />           Keywords.vue<br />        movies/<br />           MovieDetail.vue<br />        search/<br />           Search.vue<br />        Home.vue<br />    App.vue<br />    main.js<br />babel.config.js<br />package-lock.json<br />package.json<br />README.md |



### B. Model

![ERD](.\images\ERD.jpg)

### C. URL

##### i. accounts app

+ account 의 모든 URL 패턴은 accounts/ 로 시작한다.

| HTTP verb  | URL 패턴                    | 설명                                |
| ---------- | --------------------------- | ----------------------------------- |
| POST       | signup/                     | 신규 사용자 생성(회원가입)          |
| POST       | login/                      | 로그인 유저 유효성 검사             |
| POST       | api-token-auth/             | JWT 토큰을 보내 웹 인증에 이용      |
| GET        | search/                     | 다른 User 프로필 검색               |
| GET        | \<username>/                | User 프로필 상세 설명 페이지        |
| GET        | \<username>/validation/     | 프로필 유저와 로그인 유저 일치 확인 |
| GET & POST | \<username>/mylinks/        | 개인 홈페이지 링크 조회 및 추가     |
| PUT        | \<int:link_pk>/linksupdate/ | 개인 홈페이지 링크 수정             |
| GET        | \<username>/likemovies/     | 프로필 유저 찜한 영화 목록 조회     |
| GET        | \<username>/follow/         | 프로필 유저 팔로우 추가/취소        |
| GET        | \<username>/followed/       | 프로필 유저 팔로우 상태 조회        |
| GET        | \<username>/followings/     | 프로필 유저 팔로잉 목록 조회        |
| GET        | \<username>/followers/      | 프로필 유저 팔로워 목록 조회        |
| GET        | \<username>/myboards/       | 프로필 유저 작성 글 목록 조회       |
| GET        | /                           | 로그인 유저 운영자 여부 조회        |
| POST       | \<username>/uplodad         | 프로필 이미지 업로드                |



##### ii. communities app

+ communities app의 모든 URL 패턴은 communities/로 시작합니다.

| HTTP verb          | URL 패턴                                | 설명                                 |
| ------------------ | --------------------------------------- | ------------------------------------ |
| GET & POST         | /                                       | Board 글 조회 및 작성                |
| GET & PUT & DELETE | \<int:community_pk>/                    | Board 글 상세 조회 및 수정           |
| GET                | \<int:community_pk>/communitystate      | Board 글 수정 및 삭제 가능 여부 조회 |
| GET & POST         | \<int:community_pk>/comments/           | Board 에 속한 댓글 조회 및 작성      |
| PUT & DELETE       | comment/\<int:comment_pk>/              | 댓글 수정 및 작성                    |
| GET                | comment/\<int:comment_pk>/commentstate/ | 댓글 수정 및 삭제 가능 여부 조회     |
| GET                | \<int:community_pk>/likes/              | 좋아요 기능                          |
| GET                | \<int:community_pk>/dislikes/           | 싫어요 기능                          |
| GET                | \<int:community_pk>/likestate/          | 좋아요 싫어요 상태 조회              |
| GET                | genre_list/                             | 장르 목록 조회                       |
| GET                | ranking/                                | 게시판 랭킹 조회                     |



##### iii. movies app

+ movies app의 모든 URL 패턴은 movies/ 로 시작합니다.

| HTTP verb          | URL 패턴                       | 설명                                |
| ------------------ | ------------------------------ | ----------------------------------- |
| GET & POST         | list/                          | Movie List 조회                     |
| GET & PUT & DELETE | list/\<int:movie_pk>/          | Movie 상세 조회                     |
| GET & POST         | \<int:movie_pk>/review/        | Review List 조회 및 생성            |
| GET                | \<int:movie_pk>/reviewstate    | Review 수정 삭제 가능 여부 조회     |
| PUT & DELETE       | review/\<int:review_pk>/       | Review 수정 및 삭제                 |
| GET                | recommendation/\<int:movie_pk> | 해당 영화의 장르와 동일한 영화 추천 |
| GET                | \<int:movie_pk>/likes          | 해당 영화 찜하기 기능               |
| GET                | \<int:movie_pk>/liked          | 해당 영화 찜하기 상태 조회          |
| GET                | recommend/                     | 찜하기 기준 추천(Home에 표시)       |
| GET                | ranking/                       | 찜하기 순으로 영화 랭킹 조회        |
| GET                | rankinggr/                     | 좋아요한 장루스 차트로 조회         |
| GET                | rankingfr/                     | 팔로워 많은 순으로 User 조회        |
| GET & POST         | recommendation/keywords/       | 키워드 를 활용한 영화 추천          |
| GET & POST         | \<int:movie_pk>/keyword/save   | 영화에 키워드 생성 및 연결          |



### D. Component

![1_com](.\images\1_com.jpg)
![2_com](.\images\2_com.jpg)
![3_com](.\images\3_com.jpg)
![4_com](.\images\4_com.jpg)
![5_com](.\images\5_com.jpg)
![6_com](.\images\6_com.jpg)
![7_com](.\images\7_com.jpg)
![8_com](.\images\8_com.jpg)
![9_com](.\images\9_com.jpg)
![10_com](.\images\10_com.jpg)
![11_com](.\images\11_com.jpg)
![12_com](.\images\12_com.jpg)





## 구현 기능별 설명



### 0. 페이지 템플릿

- 크게 navbar, body, footer로 나누고 그 안에 필요하다면 aside나 section등을 넣어서 구분함(11/21)
- navbar에는 각 기능별 페이지로 넘어갈 수 있는 항목을 띄움(11/20)
- 관리자 페이지를 따로 생성해두었으므로 드롭다운으로 묶음(11/25)
- 영화관의 어두운 분위기를 생각하며 전체적으로 어두운 배경을 깔아줌(11/21)
- 로고를 그림으로 그려서 띄움(11/20)
- 사용자의 직관적인 이해를 돕기 위해 여러 아이콘들을 배치함(11/25)
- 전체적으로 구글 무료 폰트 적용(11/21)
- 반응형 웹으로 구성함





### 1. 로그인 / 회원가입

- 로그인 및 회원가입을 할 수 있는  페이지(11/19)

- 로그인하지 않으면 상단의 네비게이션바에 다른 목록들이 나타나지 않도록 구현(11/21)

- URL을 알아내 경로로 접근하려 해도 Vuex 에 포함된 로그인 상태를 조회하여, 비로그인 시에 자동으로 로그인 화면으로 이동하도록 구현(11/24)

- 아이디, 비밀번호 8~12자의 대*소문자, 숫자로 되어있는지, 닉네임은 한글인지 유효성 검사를 Client 에서 조회 후, 회원 가입 기능 구현(11/24) -> 오류로 인해 Server 에서 유효성 검사후 Alert 메시지를 띄우는 식으로 변경 (11/25)

- 로그인 시, 어드민 여부를 조회하여 어드민 전용 페이지인 Movie,Movie List 를 들어갈 수 있도록 구현(11/23)

- 회원가입이 되어있지 않다면 회원가입을 유도할 수 있도록 a태그 걸어둔 텍스트 띄워줌(11/23)

  ![1](.\images\1.png)

  ![2](.\images\2.png)
  
  


### 2. 프로필 페이지

- 사용자의 프로필을 볼 수 있는 페이지(11/21)

- 개인정보 수정, 프로필 이미지 업로드 구현(11/24)

- 로그인한 유저와 프로필 유저가 동일 할 경우,  개인 SNS에 연결 및 수정할 수 있도록 구현함(11/22)

- npm 으로 프로필 페이지 관련 패키지 설치 후, 프로필 페이지 구현(11/21)

- 프로필 하단에는 찜한 영화와 본 영화 목록, 팔로잉/팔로워 수를 볼 수 있음(11/21)

- 개인이 작성한 글 목록을 조회하여 체크 박스를 활용한 삭제 기능 구현(11/22)

  ![3](.\images\3.png)

  ![4](.\images\4.png)

  ![5](.\images\5.png)
  
  

### 3. 관리자 페이지

- 관리자가 보다 편하게 데이터베이스에 영화를 추가할 수 있도록 관리자 페이지를 따로 생성함(11/17)

- 영화 검색을 해서 영화를 찾고, '등록'버튼을 눌러 영화를 등록할 수 있음(11/17)
- 등록한 영화는 영화 목록에서 볼 수 있음(11/17)
- 관리자가 아니면 영화 등록 페이지를 볼 수 없음(11/23)

  ![6](.\images\6.png)

  ![7](.\images\7.png)

  

### 4. 게시판 : 장르 게시판 

- 장르별로 분류해서 글을 쓸 수 있는 게시판(11/22)

- 왼쪽에 드롭다운으로 장르를 선택해서 해당 장르와 관련된 게시글을 볼 수 있음(11/22)

- 게시글 상세 페이지로 넘어가면 좋아요/싫어요를 누를 수 있고, 둘 다 동시에 누를 수는 없음(11/23)

- 댓글을 달 수 있도록 구현함(11/23)

- 게시글 별 조회수 확인 가능(11/)

  ![8](.\images\8.png)

  

### 5. 게시판 : 랭킹 게시판

- 각종 랭킹을 볼 수 있는 게시판(11/24)

- 영화 랭킹 및 팔로워 수, 찜하기 등의 랭킹 확인 가능(11/24)

- 찜한 영화의 장르를 분류하여, 원형 차트로 눈으로 볼 수 있게 구현 (11/24)

- 랭킹 게시판의 직관성을 위하여 1위에 있는 영화와 사용자에게 왕관 아이콘 부여(11/25)

  ![9_ran](.\images\9_ran.png)
  ![10_ran](.\images\10_ran.png)
  ![11_ran](.\images\11_ran.png)
  ![12_ran](.\images\12_ran.png)
  
  
  
  


### 6. 영화 커뮤니티

- 영화에 관련된 글을 게시할 수 있는 페이지(11/18)

- 장르별로 구분해서 글을 쓸 수 있음(11/18)

- 커뮤니티에 작성한 글은 조회수 확인 가능함(11/)

  ![13_ran](.\images\13_ran.png)
  ![14_ran](.\images\14_ran.png)
  
  

### 7. 영화 정보 : 검색

- 데이터 베이스에 등록된 영화를 검색할 수 있는 페이지(11/19)
- 영화 제목 혹은 영화 설명에 있는 키워드로 영화 검색 가능(11/21)

![15_se](.\images\15_se.png)



### 8. 영화 정보 : 상세 페이지

- 영화의 포스터와 줄거리 등 상세 정보들을 볼 수 있는 페이지(11/20)
- 탭을 통해서 줄거리, 별점, 관련 영화, 트레일러러 등을 볼 수 있음(11/22)

![16_de](.\images\16_de.png)
![17_se](.\images\17_se.png)
![18_se](.\images\18_se.png)
![19_se](.\images\19_se.png)
![20_de](.\images\20_de.png)
![21_de](.\images\21_de.png)



### 9. 영화 추천

+ 찜한 영화를 기준으로 선호 장르를 파악하여 영화 추천하는 알고리즘 구현(11/23)
+ 사용자들이 등록한 키워드를 통해 키워드 추천이 가능하도록 도와주는 알고리즘 구현(11/25)

![22_de](.\images\22_de.png)
![23_rs](.\images\23_rs.PNG)



## 필수 기능에 대한 설명



- 영화 정보 데이터베이스를 필수적으로 가지고 있어야함 : TMDB API를 사용해서 사이트 내에서 영화정보들을 데이터 베이스에 추가할 수 있음
- 영화 커뮤니티에 필요한 기능 구현 : 사용자를 위한 커뮤니티를 생성, 영화 데이터를 요청하면 관리자가 관리자용 페이지를 통해 사용자가 요청한 영화 데이터를 등록할 수 있도록 함. 사용자는 커뮤니티를 통해 댓글을 달며 소통할 수 있음
- 영화 추천 알고리즘 : 사용자는 키워드 버튼을 선택함으로서 영화를 추천받을 수도 있고, 찜한 영화를 바탕으로 관련된 영화를 랜덤으로 추천받을 수도 있다.







## URL 배포

사이트 URL : https://jwsh.netlify.app/

FRONT_URL: https://lab.ssafy.com/yogjesi/final-pjt-front.git

BACK_URL:  https://lab.ssafy.com/yogjesi/final-pjt-back.git



## 느낀점

#### 윤수현 :

+ 관통프로젝트로 하루 하루 과제형으로 하다가 첫 진행한 첫 장기 프로젝트는 기대반 설렘반이였다.
+ 기존에 기획했던 것들 중 진행해보고자 했지만, 기술적 어려움 & 시간의 쫓김 에 많은 부분이 축소되거나 삭제되었던 것이 많이 아쉬웠고, 다음에는 기획단계에서 구체적이고 효율적으로 구성하여 시간 배분을 적절히 하게 해야함을 느꼈다.
+ console 을 통해 다양한 오류를 직면할 수 있었는데, 이를 해결해 나감으로써 구현 과정을 몸소 체득할 수 있었고, 또 다시 진행한다면 더욱 클린코드로 효율적인 프로젝트 진행할 수 있을거란 자신감을 얻었다.
+ 같은 기능이더라도, 구현 에 따라 차등을 느낄 수 있음을 느꼇고, 만든 것이 쌓임에 따라 그 전 코드와 새로짠 코드가 충돌을 할 수 있음을 배울 수 있었다. 또한 이를 융화시켜 해결해 나감으로써 깔끔하게 방청소한듯 뿌듯함을 느낄 수 있었다.
+ 적절한 패키지 사용은, 개발을 더욱 부드럽게 진행하게 해준다는 것을 느낄 수 있었다.



### 서지원:

- 프로젝트에 들어서니 나의 부족한 점들을 여실히, 여과없이 알 수 있었다. 프로젝트를 진행하는데 있어서 중요한 것은 코드를 짜는 능력 뿐만 아니라 의사소통, 시간을 관리하는 능력 등이 있더라. 할 수 있을 거라고 생각했던 부분들도 막상 프로젝트로 대하고 보니 막막해지기 일쑤였다.
- 배웠으니 할 수 있을 거라고 생각했지만, 막상 알고리즘 구현단계로 들어가니 되는 것과 되지 않는 것들을 동시에 맞닥뜨리게 되었다. 게다가 콘솔과 터미널창에 뜨는 수많은 오류들은 나를 약간 겁먹게 했지만, 페어님 덕분에 하나 하나 풀어나가면서 여러 종류의 에러들에 대해서 배울 수 있었다. 감사하다.
- 데이터베이스의 구조에 대해서 많이 생각해볼 수 있었다. 모델링이 중요하다고 하는 이유도 알 것 같았다. 다른 것보다 데이터의 흐름이 어떻게 들어가서 어떻게 연결되고 어떤 방법으로 이어지는지 보고 아는 것이 이 프로젝트의 즐거움 중 하나였다. 너무너무 신기해서 계속해서 영화를 등록하고 데이터베이스에 어떻게 들어가서 어떤 식으로 연결되어 있는지 들여다보았다. 앞으로 다른 프로젝트를 하는데 있어 이 프로젝트는 분명 큰 도움이 되겠지.
- 별별 에러들을 다 봤다. 하지만 마감 날 오전에 마주한 broken pipe는 내 심장을 덜컹거리게 한 에러 중 단연코 최고였다고 할 수 있다. 논리적으로 생각할 수 있는 시간도 부족했지만, 페어님 덕분에 침착하게 해결할 수 있었다. 매우 다행이었다.
- 그리고 난 이구역의 검색왕이 될 것이다. 하하하!! 영어를 할 줄 안다는 것은 양질의 정보를 찾고 싶을 때 많은 도움이 되는 것 같다.
- 의사소통하는 능력을 기를 수 있었다. 지금껏 진행했던 그 어느 프로젝트보다 의견을 많이 교환했다. 그래서 프로젝트를 진행하는데 크게 막히는 부분이 없었으며, 서로 열정이 넘쳐서 좋은 분위기로 프로젝트를 진행할 수 있었다. 진짜 감사한 것이, 내가 막히는 부분이 있으면 페어님께서 내가 스스로 생각해볼 수 있도록 알려주었다.  이 프로젝트를 통해 정말 많은 것들을 배워간다. 


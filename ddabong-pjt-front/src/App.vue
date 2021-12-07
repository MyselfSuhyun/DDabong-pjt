<template>
  <div id="app">
    <div id="nav" class="navbar navbar-expand-md navbar-dark" style="background-color: rgb(46, 46, 46);">
      <div class="container-fluid">
        <router-link to="/"><img src="./assets/changmok.png" height="50px" alt="abc"></router-link>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse class="justify-content-end" id="nav-collapse" is-nav>
          <span class="row" v-if="isLogined">
            <!-- li 태그가 ul 태그안에 있어야 안정감있어서 span 안에 일일이 걸어줌 -->
            <ul class="navbar-nav">
              <!-- 관리자용 드롭다운 -->
              <b-nav-item-dropdown text="관리자용" right v-show="isAdmined">
                <b-dropdown-item href="#"><router-link to="/movie">영화추가</router-link></b-dropdown-item>
                <b-dropdown-item href="#"><router-link :to="{ name:'MovieList'}">영화목록</router-link></b-dropdown-item>
              </b-nav-item-dropdown>
              <li class="m-2 nav-item active">
                <router-link to="/">홈</router-link>
              </li>
              <li class="m-2 nav-item active">
                <router-link :to="{name:'Boards'}">장르게시판</router-link>
              </li>
              <li class="m-2 nav-item active">
                <router-link :to="{name:'RankingBoard'}">랭킹게시판</router-link>
              </li>
              <li class="m-2 nav-item active">
                <router-link :to="{ name:'Keywords'}">키워드추천</router-link>
              </li>
              <li class="m-2 nav-item active">
                <router-link :to="{ name:'Search'}">영화검색</router-link>
              </li>
              <li class="m-2 nav-item active">
                <router-link :to="{ name:'GenreSearch'}">장르검색</router-link>
              </li>
              <li class="m-2 nav-item active">
                <router-link :to="{ name:'UserSearch'}">유저찾기</router-link>
              </li>
              <li class="m-2 nav-item active">
                <router-link @click.native="logout" to="#">로그아웃</router-link>
              </li>
              <li class="mx-2 nav-item active">
                <!-- <font-awesome-icon icon="fa-solid fa-circle-user" /> -->
                <!-- <i class="fas fa-user-circle"></i> -->
                <router-link :to="{name: 'Profile', params:{userName:this.currentuser}}">
                  <img src="./assets/user.png" alt="" style="width:40px">
                </router-link>
              </li>
            </ul> 
          </span>
          <span class="inline" v-else>
            <ul class="navbar-nav">
              <li class="m-2 nav-item active">
                <router-link :to="{ name:'Signup'}">Signup</router-link>
              </li>
              <li class="m-2 nav-item active">
                <router-link :to="{ name:'Login'}" >Login</router-link>
              </li>
            </ul>
          </span>   
        </b-collapse>
      </div>
    </div>

    <body style="background-color:rgb(80, 80, 80);">
      <div id="wrap">
        <section>
          <div class="container-fluid">
            <div class="row mb-5">
              <router-view @login="isLogin=true"/>   
            </div>
          </div>
        </section>

        <footer id="footer" class="footer" style="background-color:rgb(46, 46, 46); height:120px; align-items:center;">
          <div class="row">
            <p id="footertext" class="col my-5" style="text-decoration:none;">쌍따봉 극장은 여러분을 환영합니다!</p>
          </div>
        </footer>

      </div>

    </body>
  </div>
</template>


<script>
import {mapState,mapActions} from 'vuex'

export default {
  name: 'App',
  methods: {
    logout: function() {
      this.deActiveLogined
      localStorage.removeItem('jwt')
      this.logoutValid
      this.$router.push({name:'Login'})
    },
  },
  computed:{
    ...mapState([
      'isAdmined','currentuser','isLogined',
    ]),
    ...mapActions([
      'logoutValid','adminValid','activeLogined','deActiveLogined'
    ])
  },
  created: function() {
    // 1. Vue Instance 가 새엉된 직후에 호출되어 jwt  가져오기
    const token = localStorage.getItem('jwt')
    // 2. 토큰이 있으면
    if (token) {
      // 3. True 로 변경하고 없으면 유지
      this.activeLogined
      this.adminValid
    }
  },

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang&family=IBM+Plex+Sans+KR:wght@600&family=Jua&family=Roboto+Mono&family=Song+Myung&display=swap');



#app {
  /* font-family: 'Jua', sans-serif; */
  font-family: 'IBM Plex Sans KR', sans-serif;
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  /* font-family: 'Song Myung', serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /* height: 1000px; */
  color: #2c3e50;
  background-color:rgb(80, 80, 80);
}

#nav {
  padding: 15px;
}

#nav a {
  font-weight: bold;
  font-size: medium;
  text-decoration: none;
  color: #747b81;
}

#nav a.router-link-exact-active {
  color: #9f9ae7;
}

#footerfont {
  display: flex; 
  flex-direction: row; 
  align-items: center; 
  justify-content: center; 
  position: fixed; 
  bottom: 0px; 
  height: 60px;
  color: #59626b;
}

#footertext {
  font-family: 'Gowun Batang', serif;
  /* font-family: 'IBM Plex Sans KR', sans-serif; */
  /* font-family: 'Jua', sans-serif; */
  /* font-family: 'Roboto Mono', monospace; */
  /* font-family: 'Song Myung', serif; */
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content:center;
  color: #59626b;
}

#title {
  /* font-family: 'Gowun Batang', serif; */
  font-family: 'IBM Plex Sans KR', sans-serif;
  /* font-family: 'Jua', sans-serif; */
  /* font-family: 'Roboto Mono', monospace; */
  /* font-family: 'Song Myung', serif; */
  margin: 30px;
  color: white;
}

#detail {
  font-family: 'Gowun Batang', serif;
  /* font-family: 'IBM Plex Sans KR', sans-serif; */
  /* font-family: 'Jua', sans-serif; */
  /* font-family: 'Roboto Mono', monospace; */
  /* font-family: 'Song Myung', serif; */
  font-weight: bold;
  color: rgb(155, 155, 155);
  margin: 20px;
}

#searchtext {
  /* font-family: 'IBM Plex Sans KR', sans-serif; */
  font-family: 'Jua', sans-serif;
  /* font-family: 'Song Myung', serif; */
}

/* footer 하단 고정 [E] */
#wrap {
  min-height: 100vh;
  position: relative;
  width:100%;
}

footer {
  width:100%;
  height: 120px;
  bottom: 0px;
  position: absolute;
}

section {
  padding-bottom: 120px;
}
html, body {
  margin:0;
  padding:0;
}

</style>
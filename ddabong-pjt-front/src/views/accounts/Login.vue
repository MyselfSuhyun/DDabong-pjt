<template>
  <div>
    <div id="title">
      <h1>Login</h1>
    </div>
    <form id="inputform" class="container-fluid">
      <div class="row col-12 col-md-4">
        <div class="input-group my-2">
          <span class="input-group-text" id="inputGroup-sizing-sm" style="width:120px;">아이디</span>
          <input class="form-control"
          placeholder="ID"
          autocomplete="off"
          type="text"
          id="username"
          v-model="credentials.username">
        </div>
        <div class="input-group my-2">
          <span class="input-group-text" id="inputGroup-sizing-sm" style="width:120px;">비밀번호</span>
          <input class="form-control"
          autocomplete="off"
          placeholder="PASSWORD"
          type="password"
          id="password"
          v-model="credentials.password"
          @keyup.enter="login">
        </div>
      </div>
    </form>
    <div class="my-2">
      <button id="signuplink" class="btn" @click="signup">아직 회원이 아니세요?</button>
    </div>
    <button id="btntext" class="btn btn-primary my-2" @click="login">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'
import {mapActions} from 'vuex'
export default {
  name: 'Login',
  data: function() {
    return {
      credentials: {
        username: null,
        password: null,
      },

    }
  },
  methods: {
    signup: function() {
      this.$router.push({name: 'Signup'})
    },
    login: function() {
      //  console.log(this.credentials)
      axios({
        method: 'post',
        url: 'https://jwsh.link/accounts/login/',
        data: this.credentials
      })
      .then(res =>{
        if (res.data.Success){
         axios({
          method: 'post',
          url: 'https://jwsh.link/accounts/api-token-auth/',
          data: this.credentials
          })
          .then((res) =>{
            localStorage.setItem('jwt',res.data.token)
            this.$emit('login')
            this.adminValid
            this.activeLogined
            this.$router.push({name:'Home'})
          })
          .catch(function(error) {
              console.log(error.response.data)
          })
        }
      })
      .catch(err =>{
        alert(err.response.data)
      })
    },
  },
  computed:{
    ...mapActions([
      'adminValid','activeLogined'
    ])
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@600&family=Jua&family=Roboto+Mono&family=Song+Myung&display=swap');

#cardtext {
  font-family: 'IBM Plex Sans KR', sans-serif;
  /* font-family: 'Jua', sans-serif; */
  /* font-family: 'Song Myung', serif; */
}

#btntext {
  font-family: 'IBM Plex Sans KR', sans-serif;
  /* font-family: 'Jua', sans-serif; */
  /* font-family: 'Song Myung', serif; */
}

#title {
  font-family: 'Roboto Mono', monospace;
}

.input-group {
  text-align: center;
}

#signuplink {
  color:rgb(189, 199, 209);
}

#inputform {
  display:flex;
  justify-content: center;
  align-content: center;
  padding-top:50px;
  padding-bottom: 100px;
}

</style>
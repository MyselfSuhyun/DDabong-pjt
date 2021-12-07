<template>
  <div>
    <div id="title">
      <h1>Signup</h1>
    </div>
    <form id="inputform" class="container-fluid">
      <div class="row col-5">
        <div class="input-group">
          <span class="input-group-text" id="inputGroup-sizing-default" style="width:125px;">아이디</span>
          <input class="form-control"
          placeholder="ID"
          autocomplete="off"
          type="text"
          id="username"
          aria-describedby="inputGroup-sizing-default"
          v-model="credentials.username">
        </div>
        <div class="input-group">
          <span class="input-group-text" id="inputGroup-sizing-default" style="width:125px;">닉네임</span>
          <input class="form-control"
          placeholder="NICKNAME"
          autocomplete="off"
          type="text"
          id="nickname"
          aria-describedby="inputGroup-sizing-default"
          v-model="credentials.nickname">
        </div>
        <div class="input-group">
          <span class="input-group-text" id="inputGroup-sizing-sm" style="width:125px;">비밀번호</span>
          <input class="form-control"
          placeholder="PASSWORD"
          autocomplete="off"
          type="password"
          id="password"
          aria-describedby="inputGroup-sizing-default"
          v-model="credentials.password">
        </div>
        <div class="input-group">
          <span class="input-group-text" id="inputGroup-sizing-sm" style="width:125px;">비밀번호 확인</span>
          <input class="form-control"
          placeholder="PASSWORD CHECK"
          autocomplete="off"
          type="password"
          id="passwordConfirmation"
          aria-describedby="inputGroup-sizing-default"
          v-model="credentials.passwordConfirmation"
          @keyup.enter="signUp">
        </div>
      </div>
    </form>
    <button id="btntext" class="btn btn-secondary" @click="signUp">회원가입</button>

  </div>
</template>

<script>
import axios from 'axios'
import {mapActions} from 'vuex'
export default {
  name: 'Signup',
  data: function() {
    return {
      credentials: {
        username: "",
        nickname: "",
        password: "",
        passwordConfirmation: "",
      },
    }
  },
  methods: {
    signUp: function() {
      axios({
        method: 'post',
        url: 'https://jwsh.link/accounts/signup/',
        data: this.credentials
      })
      .then(() =>{
        axios({
        method: 'post',
        url: 'https://jwsh.link/accounts/api-token-auth/',
        data: this.credentials
        })
        .then(res =>{
          localStorage.setItem('jwt',res.data.token)
          this.adminValid
          this.activeLogined
          this.$emit('login')
          this.$router.push({name:'Home'})
          this.$router.go()
        })
      })
      .catch(err =>{
        alert(err.response.data)
      })
    },
    ...mapActions([
      'adminValid','activeLogined'
    ])
  },
  computed:{

  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@600&family=Jua&family=Roboto+Mono&family=Song+Myung&display=swap');

#inputGroup-sizing-sm {
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

</style>
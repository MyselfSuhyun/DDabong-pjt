<template>
<!-- MovieDetail의 자식 컴포넌트 -->
  <div>
    <div id="thirddetail" class="mb-3 mt-5">
      <h2>키워드 입력</h2>
    </div>
    <h6 id="seconddetail">이 영화와 관련된 키워드를 입력해주시면</h6>
    <h6 id="seconddetail">보다 좋은 서비스를 제공하는 힘이 됩니다.</h6>
    <div class="input-group my-3">
      <input id="inputtext" type="text" class="form-control"
      @keyup.enter="saveKeyword"
      v-model="inputKeyword"
      placeholder="관련된 키워드를 입력해주세요.">
      <button @click="saveKeyword" id="btntext"
      class="btn btn-secondary">키워드 입력</button>
    </div>
    <div id="detail">
      <h6>이 영화와 관련된 키워드는요...</h6>
      <!-- 아래에 관련된 키워드들을 다 출력해주자. -->
    </div>
    <div id="inputtext" v-for="(keyword, index) in showKeywords" :key="index">
      {{ keyword.content }}
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import TheMovieKeywords from '@/components/movies/TheMovieKeywords'

export default {
  name:'TheMovieService',
  data: function(){
    return {
      inputKeyword:null,
      showKeywords: null,
    }
  },
  props:{
    movieNo:Number,
  },
  methods: { 
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    saveKeyword: function() {
      const enterKeyword = {
        content: this.inputKeyword,
      }
      axios({
        method: 'post',
        url: `https://jwsh.link/movies/${this.movieNo}/keyword/save`,
        data: enterKeyword,
        headers: this.setToken()
      })
        .then(() => {
          this.getKeywords()
          this.inputKeyword = null
          
        })
        .catch(err => {
          console.log(err)
        })
    },
    getKeywords: function () {
      axios({
        method: 'get',
        url: `https://jwsh.link/movies/${this.movieNo}/keyword/save`,
        headers: this.setToken() // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          this.showKeywords = res.data
        })
        .catch(err => {
          console.log(err)
        })
    }, 
  },
  created: function() {
    this.getKeywords()
  }
}
</script>

<style>

</style>
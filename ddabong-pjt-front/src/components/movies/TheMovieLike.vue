<template>
  <div>
    <div v-show="isLiked">
      <button id="littlebtn" class="btn btn-secondary" @click="likeMovie">찜하기 취소</button>
    </div>
    <div v-show="!isLiked">
      <button id="littlebtn" class="btn btn-secondary" @click="likeMovie">찜하기</button>
    </div>
    <div id="detail"><p>찜: <span>{{likeCount}}</span></p></div>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'TheMovieLike',
  data:function(){
    return {
      isLiked:null,
      likeCount:null,
    }
  },
  props:{
    movieNum:Number,
  },
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    likeMovie: function(){
      axios({
        methods: 'get',
        url: `https://jwsh.link/movies/${this.movieNum}/likes/`,
        headers: this.setToken()
      })
      .then(res=> {
        this.isLiked=res.data.isLiked
        this.likeCount =res.data.likeCount
      })
      .catch(err => {
        console.log(err)
      })
    },
    likeMovied: function(){
      axios({
        methods: 'get',
        url: `https://jwsh.link/movies/${this.movieNum}/liked/`,
        headers: this.setToken()
      })
      .then(res=> {
        this.isLiked=res.data.isLiked
        this.likeCount = res.data.likeCount
      })
      .catch(err => {
        console.log(err)
      })
    },
  },
  created: function() {
    this.likeMovied()
  }
}
</script>

<style>
  #littlebtn {
    /* font-family: 'Gowun Batang', serif; */
    /* font-family: 'IBM Plex Sans KR', sans-serif; */
    font-family: 'Jua', sans-serif;
    /* font-family: 'Roboto Mono', monospace; */
    /* font-family: 'Song Myung', serif; */
    font-weight: bold;
    color: rgb(155, 155, 155);
    margin: 20px;
  }

</style>
<template>
  <div class="Home">
    <div id="title">
      <h1>쌍따봉극장에 오신 것을 환영합니다!</h1>
    </div>
    <button id="btntext" class="btn btn-outline-success mb-4" v-show="!isLikeNone" @click="algoTest">다른거 추천 받기</button>
    <br>
    <p id="rec" v-show="isLikeNone">영화를 추천받으시려면 검색해서 찜!해주세요.</p>
    <div v-show="!isLikeNone">
      <div class="container-fluid">
        <div class="row">
          <div class="col-12 col-lg-6 offset-lg-3">
            <b-list-group>
              <p v-for="(movie,index) in recommendMovies" :key="index">
                <b-list-group-item @click="movieDetail(movie.id)" id="mainlist" variant="dark">{{movie.title}}</b-list-group-item>              
                <!-- <img :src="image(movie.poster_path)" alt=""> -->
              </p>
            </b-list-group>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import _ from 'lodash'
import {mapState} from 'vuex'


export default {
  name: 'Home',
  data: function () {
    return {
      isLikeNone: false,
      recommendMovies: Object,
    }
  },

  methods: {
    movieDetail: function(movie_id) {
      this.$router.push({name:"MovieDetail",params:{movieNum:movie_id}})
    },
    image(img) {
      return `http://image.tmdb.org/t/p/w300/${img}`
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    algoTest: function () {
      // console.log(this.setToken())
      axios({
        method: 'get',
        url: 'https://jwsh.link/movies/recommend/',
        headers: this.setToken() // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then((res) => {
          if (res.data.isLikeNone){
            this.isLikeNone = res.data.isLikeNone
          }else{
            this.recommendMovies = _.sampleSize(res.data,10)
            this.isLikeNone = false
          }


        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  computed:{
    ...mapState([
      'currentuser','isLogined',
    ]),
  },
  created: function(){
    this.algoTest()
    if (this.isLogined==false){
      this.$router.push({name:'Login'})
    }
  }
}
</script>

<style scoped>
#rec {
  /* font-family: 'Gowun Batang', serif; */
  font-family: 'IBM Plex Sans KR', sans-serif;
  /* font-family: 'Jua', sans-serif; */
  /* font-family: 'Roboto Mono', monospace; */
  /* font-family: 'Song Myung', serif; */
  font-weight: bold;
  color: rgb(34, 34, 34);
  margin: 20px;
}

#mainlist {
  /* font-family: 'Gowun Batang', serif; */
  font-family: 'IBM Plex Sans KR', sans-serif;
  /* font-family: 'Jua', sans-serif; */
  /* font-family: 'Roboto Mono', monospace; */
  /* font-family: 'Song Myung', serif; */
  font-weight: bold;
  font-size: 13px;
  color: rgb(34, 34, 34);
  /* margin: 20px; */
}
</style>
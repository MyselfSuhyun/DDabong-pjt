<template>
  <div>
    <div id="title">
      <h1>당신의 키워드는?</h1>
    </div>
    <div id="detail">
      <h4>키워드를 선택하세요! 관련된 영화를 추천해 드릴게요.</h4>
    </div>
    <!-- 버튼 안에는 키워드를 받아와야 함 -->
    <div class="row">
      <button id="btntext" class="col m-5 btn btn-info" v-show="allKeywords.length>2" @click="getKeyword(firstKeyword)">{{ firstKeyword }}</button>
      <button id="btntext" class="col m-5 btn btn-info" v-show="allKeywords.length>2" @click="getKeyword(secondKeyword)">{{ secondKeyword }}</button>
    </div>
    <div class="d-flex flex-wrap">
      <div class="card mb-3col-12 col-sm-2 col-md-3" @click="moveDetail(movie.id)" v-for="(movie,index) in recommendMovies" :key="index">
        <img class="card-img-top" :src="image(movie.poster_path)" alt="">
        <p id="detail" class="card-text">{{movie.title}}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import { mapState } from 'vuex'

export default {
  name: 'Keywords',
  data: function() {
    return {
      firstKeyword: null,
      secondKeyword: null,
      selectedKeywords: [],
      allKeywords:[],
      recommendMovies: Object
    }
  },
  methods: {
    image(img) {
      return `http://image.tmdb.org/t/p/w300/${img}`
    },
    moveDetail(movie_id){
      this.$router.push({name:"MovieDetail",params:{movieNum:movie_id}})
    },
    // 키워드 두개 랜덤으로 받아와서 버튼에 띄우는 함수
    getTestFunction: function() {
      const twoKeywords = _.sampleSize(this.allKeywords,2)
      this.firstKeyword = twoKeywords[0]
      this.secondKeyword = twoKeywords[1]
    },
    getKeyword: function(keyword) {
      this.selectedKeywords.push(keyword)
      this.allKeywords = this.allKeywords.filter((element) => element !== keyword)
      this.getTestFunction()
      this.getSelectedKeywords()
      
    },
    getSelectedKeywords: function() {
      const sendKeywords = {
        content: this.selectedKeywords,
      }
      axios({
        method: 'post',
        url: 'https://jwsh.link/movies/recommendation/keywords/',
        data: sendKeywords,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`}
      })
        .then(res => {
          // console.log(res) 
          this.recommendMovies = _.sampleSize(res.data,4)        
        })
        .catch(err => {
          console.log(err)
        })
    }

  },
  computed:{
    ...mapState([
      'isLogined'
    ])
  },
  created: function () {
    // this.getTestFunction()
    if (this.isLogined==false){
      this.$router.push({name:'Login'})
    }
    axios({
        method: 'get',
        url: 'https://jwsh.link/movies/recommendation/keywords/',
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`}
      })
        .then((res) => {
          const twoKeywords = _.sampleSize(res.data,2)
          this.firstKeyword = twoKeywords[0].content
          this.secondKeyword = twoKeywords[1].content
          for (let i=0;i < res.data.length;i++) {
            this.allKeywords.push(res.data[i].content)
          }
        })
        .catch(err => {
          console.log(err)
        })
  }

}
</script>

<style>

</style>
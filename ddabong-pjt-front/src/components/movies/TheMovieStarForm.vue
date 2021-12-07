<template>
  <div>
    <div id="seconddetail" class="mb-3 mt-5">
      <h2>평점 등록</h2>
    </div>
    
    <div v-if="!isReviewed">
      <star-rating class="justify-content-center" :increment="0.5" :star-size="30" :show-rating="false" v-model="rating" :border-width="5" border-color="#d8d8d8" :rounded-corners="true" :read-only="false" ></star-rating>
      <input 
        type="text"
        v-model.trim="content" 
        @keyup.enter="createReview">
      <button id="btntext" class="btn btn-secondary" @click="createReview">작성</button>
    </div>
    <div v-if="isReviewed">
      <p id="thirddetail">이전에 등록한 평점</p>
      <span v-show="!updateState"><star-rating :increment="0.5" :star-size="30" :show-rating="false" v-model="myReview.stars" :border-width="5" border-color="#d8d8d8" :rounded-corners="true" :read-only="true" :inline="true" ></star-rating>
      {{myReview.content}}</span>
      <button id="btntext" class="btn btn-secondary btn-sm" v-show="!updateState" @click="updateStar">수정</button>
      <star-rating class="col" v-show="updateState" :increment="0.5" :star-size="30" :show-rating="false" v-model="tmpStar" :border-width="5" border-color="#d8d8d8" :rounded-corners="true" :read-only="false" :inline="true" ></star-rating>
      <input id="inputtext" v-show="updateState" v-model="tmpContent" type="text">
      <button id="btntext" class="btn btn-secondary btn-sm"  v-show="updateState" @click="updateStars">완료</button>
      <button id="btntext" class="btn btn-secondary btn-sm"  v-show="updateState" @click="updateStar">취소</button>
      <button id="btntext" class="btn btn-secondary btn-sm"  @click="starDelete">삭제</button>
      
    </div>
    <div id="seconddetail" class="mb-3 mt-5">
      <h2>전체 평점</h2>
    </div>
    <the-movie-star-item v-for="(review,index) in reviews"
    :key="index"
    :review-item="review"></the-movie-star-item>
  </div>
</template>

<script>
import TheMovieStarItem from '@/components/movies/TheMovieStarItem'
import StarRating from 'vue-star-rating'
import axios from 'axios'
export default {
  name:'TheMovieStarForm',
  data: function() {
    return {
      reviews:null,
      rating:2.5,
      content:null,
      isReviewed: false,
      myReview:{ 
        id: null, 
        user: { 
          id: null, 
          nickname: null, 
          username: null
          }, 
        content: null, 
        stars: null, 
        created_at: null, 
        updated_at: null, 
        movie: null },
      tmpContent: null,
      tmpStar: 2,
      updateState:false,
      isComment: null,
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
    
    createReview: function () {
      const reviewItem = {
        content: this.content,
        stars: this.rating,
      }

      if (reviewItem.content) {
        axios({
          method: 'post',
          url: `https://jwsh.link/movies/${this.movieNum}/review/`,
          data: reviewItem,
          headers: this.setToken()
        })
          .then(() => {
            this.getReviews()
            this.content = null
            this.rating = 2.5
            this.reviewState()
          })
          .catch(err => {
            console.log(err)
          })
        }
    },
    updateStar: function() {
      this.updateState = !this.updateState
      this.tmpContent = this.myReview.content
      this.tmpStar = this.myReview.stars
    },
    updateStars: function() {
      const updateReview = {
        ...this.myReview,
        content:this.tmpContent,
        stars:this.tmpStar,
      }
      axios({
        method: 'put',
        url: `https://jwsh.link/movies/review/${this.myReview.id}/`,
        data: updateReview,
        headers: this.setToken()
      })
        .then(() => {
          this.updateState = !this.updateState
          this.getReviews()
          this.reviewState()
        })
        .catch(err => {
          console.log(err)
        })
    },
    starDelete: function() {
      axios({
        method: 'delete',
        url: `https://jwsh.link/movies/review/${this.myReview.id}/`,
        headers: this.setToken()
      })
      .then(() => {
        this.isReviewed=false
        this.getReviews()
      })
      .catch(err => {
        console.log(err)
      })
    },
    getReviews: function () {
      axios({
        method: 'get',
        url: `https://jwsh.link/movies/${this.movieNum}/review/`,
        headers: this.setToken() // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          // console.log(res.data)
          // console.log(res)
          this.reviews = res.data
          this.averStars()
          
        })
        .catch(err => {
          console.log(err)
        })
    },
    reviewState: function () {
      axios({
        method: 'get',
        url: `https://jwsh.link/movies/${this.movieNum}/reviewstate`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
      })
        .then(res => {
          if(res.data){
            this.isReviewed = true
            this.myReview = res.data
            this.tmpContent = res.data.content
            this.tmpStar = res.data.stars
          }
          // console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
    averStars: function(){
      let averStar = 0
      for (let i = 0; i<this.reviews.length;i++){
        averStar += this.reviews[i].stars
      }
      this.$emit('aver-star',averStar/this.reviews.length)
    }
  },
  created: function(){
    this.getReviews()
    this.reviewState()
  },
  components:{
    TheMovieStarItem,
    StarRating,
  }
}
</script>

<style>

</style>
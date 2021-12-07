<template>
  <div>
    <div id="title">
      <h2>찜한 영화 목록</h2>  
    </div>
    <div class="container" >

      <div v-if="isMovied">

        <div class="d-flex flex-row flex-wrap">
          <div class="card col-12 col-sm-3 col-lg-2 px-1 my-2" v-for="(likeMovie,index) in likeMovies" :key="index" @click="movieDetail(likeMovie.id)">
            <img class="card-img-top" :src="image(likeMovie.poster_path)" alt="" style="width: auto;">
            <div class="card-body">
              <p class="card-text">{{likeMovie.title}}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import axios from 'axios'
export default {
  name:'TheLikeMovies',
  data: function () {
    return{
      isMovied:true,
      likeMovies:{
        type:Object,
      },
    }
  },
  props:{
    userName:String,
  },
  methods:{
    image (img) {
      if(img){
        return `http://image.tmdb.org/t/p/w300/${img}`
      }
      
    },
    movieDetail: function(movie_id){
      this.$router.push({name: 'MovieDetail', params:{movieNum:movie_id}})
    },
    getLikeMovies: function () {
      axios({
        method: 'get',
        url: `http://13.125.243.60/accounts/${this.userName}/likemovies/`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
      })
        .then(res => {
          if(res.data[0]){
            this.likeMovies = _.sampleSize(res.data,12)
          }else{
            this.isMovied =false
          }
        })
        .catch(err => {
          console.log(err)
        })
    },

  },
  created: function() {
    this.getLikeMovies()
  },
}
</script>

<style>

</style>
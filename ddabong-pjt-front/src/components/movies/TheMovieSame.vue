<template>
  <div class="d-flex flex-row flex-wrap">
    <div class="card col-12 col-md-3 px-1 my-2" v-for="(movie,index) in movies" :key="index">        
      <img class="card-img-top" @click="moveDetail(movie.id)" :src="image(movie.poster_path)">
      <div class="card-text">
        <p id="forthdetail">{{movie.title}}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
export default {
  name:'TheMovieSame',
  data: function() {
    return {
      movies:Object
    }
  },
  props:{
    movieId:Number,
  },
  methods:{
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
    getMovies: function () {
      axios({
        method: 'get',
        url: `https://jwsh.link/movies/recommendation/${this.movieId}`,
        headers: this.setToken() // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          // console.log(res.data)
          // console.log(res)
          this.movies = _.sampleSize(res.data,4)
        })
        .catch(err => {
          console.log(err)
        })
    },
    moveDetail: function(movie_id) {
      this.$router.push({name: 'MovieDetail', params:{movieNum:movie_id}})
      this.$router.go()
    }
  },
  created: function() {
    this.getMovies()
  }
}
</script>

<style>

</style>
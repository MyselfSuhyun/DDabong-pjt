<template>
  <div>
    <div class="card" @click="toggleShow">
      <div v-if="show" id="cardtext">
        <img style="width:100%;" :src="image(movieItem.poster_path)" alt="">
        <h5 class="card-title my-3">{{ movieItem.title }}</h5>
      </div>
      <div v-if="!show">
        <p>{{movieItem.overview}}</p>
      </div>
    </div>
    <button id="btntext" class="btn btn-secondary btn-sm my-1" @click="createMovie">등록</button>
  </div>
</template>

<script>
// import Velocity from 'velocity-animate'
import axios from 'axios'
export default {
  name:'TheMovieListItem',
  data: function() {
    return{
      show:true
    }
  },
  props:{
    movieItem: {
      type: Object
    }
  },
  methods: {
    // poster 경로를 받아오기 위해 url 생성을 위한 method
    image (img) {
      return `http://image.tmdb.org/t/p/w300/${img}`
    },
    toggleShow(){
      this.show = !this.show
      // console.log(this.movieItem)
      // console.log(this.movieItem.genres.length)
    },
    createMovie: function () {
      let genres_list = []
      for(let i = 0;i<this.movieItem.genres.length;i++){
        genres_list.push(this.movieItem.genres[i].id)
      }
      // console.log(genres_list)
      const theMovieItem = {
        ...this.movieItem,
        tmdb_id: this.movieItem.id,
        genres : genres_list,
      }
      // console.log(theMovieItem)
      // console.log(this.movieItem)
      axios({
        method: 'post',
        url: 'http://13.125.243.60/movies/list/',
        data: theMovieItem
      })
      .then(()=>{
        // this.$router.push({name:'MovieList'})
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  }

}
</script>

<style>

</style>
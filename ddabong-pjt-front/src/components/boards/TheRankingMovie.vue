<template>
  <div>
    <br>
    <div class="container">
      <div class="row">
        <div class="col">
          <img :src="king" alt="king" style="width:30px">
          <div id="secondtitle">
            <h4>1위</h4>
          </div>          
          <div @click="moveFirstDetail">
            <div id="seconddetail">
              <h4>{{firstmovie.title}}</h4>
            </div>            
            <img :src="image(firstmovie.poster_path)" alt="">
          </div>  
        </div>
        <div class="col">
          <img :src="crown" alt="crown" style="width:30px">
          <div id="secondtitle">
            <h4>순위 목록</h4>
          </div>          
          <hr>
          <div v-for="(movie,index) in likemovies" :key="index">
            <div id="seconddetail" @click="moveDetail(movie.id)">
              <p>{{index+1}}위: {{movie.title}}</p> 
              <p>/ 찜 : {{movie.like_users.length}} 명</p>
              <hr>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import crown from "@/assets/crown.png"
import king from "@/assets/king.png"

export default {
  name: 'TheRankingMovie',
  data: function() {
    return {
      firstmovie:Object,
      likemovies:Object,
      crown,
      king,
    }
  },
  methods:{
    image(img) {
      return `http://image.tmdb.org/t/p/w300/${img}`
    },
    moveFirstDetail: function(){
      this.$router.push({name: 'MovieDetail', params:{movieNum:this.firstmovie.id}})
    },
    moveDetail: function(movie_id){
      this.$router.push({name: 'MovieDetail', params:{movieNum:movie_id}})
    },
  },
  created: function() {
    axios({
      method: 'get',
      url: 'https://jwsh.link/movies/ranking/',
      headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`}
    })
      .then(res => {
        this.firstmovie = res.data[0]
        this.likemovies = res.data
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style>
#secondtitle {
  /* font-family: 'Gowun Batang', serif; */
  font-family: 'IBM Plex Sans KR', sans-serif;
  /* font-family: 'Jua', sans-serif; */
  /* font-family: 'Roboto Mono', monospace; */
  /* font-family: 'Song Myung', serif; */
  color: rgb(231, 231, 231);
}

#detail {
  font-family: 'Gowun Batang', serif;
  /* font-family: 'IBM Plex Sans KR', sans-serif; */
  /* font-family: 'Jua', sans-serif; */
  /* font-family: 'Roboto Mono', monospace; */
  /* font-family: 'Song Myung', serif; */
  font-weight: bold;
  color: rgb(155, 155, 155);
  margin: 20px;
}

</style>
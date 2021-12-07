<template>
  <div class="row">
    <div id="title">
      <h1>영화 상세정보</h1>
    </div>

    <div class="container-fluid">
      <div class="row" style="padding:5%">
        <aside class="col-12 col-md-3">
          <img :src="image(movie.poster_path)" alt="" style="width:100%">
          <!-- 찜하기 -->
          <the-movie-like
          :movie-num="Number($route.params.movieNum)"></the-movie-like>
        </aside>
        <section class="col-12 col-md-9">
          <div class="mx-3">
            <div class="row">
              <div>
                <b-card title="Card Title" no-body>
                  <!-- <b-card-header header-tag="nav"> -->
                    <b-nav tabs justified>
                      <b-nav-item active><span id="seconddetail" class="col" @click="pageMovie(1)">상세정보</span></b-nav-item>
                      <b-nav-item active><span id="seconddetail" class="col" @click="pageMovie(2)">평점</span></b-nav-item>
                      <b-nav-item active><span id="seconddetail" class="col" @click="pageMovie(3)">비슷한 영화</span></b-nav-item>
                      <b-nav-item active><span id="seconddetail" class="col" @click="pageMovie(4)">키워드 입력</span></b-nav-item>
                      <b-nav-item active><span id="seconddetail" class="col" @click="pageMovie(5)">관련 영상</span></b-nav-item>
                    </b-nav>
                  <!-- </b-card-header> -->

                  <b-card-body class="text-center">
                    <div v-if="moviePage===1">
                      <h5 id="thirddetail">제목: {{ movie.title }} </h5>
                      <h7 id="thirddetail">장르: 
                        <the-detail-genre 
                        v-for="(genre,index) in movie.genres" 
                        :key="index"
                        :genre-item="genre">
                        </the-detail-genre> </h7>
                      <div id="thirddetail" class="m-4"><p>{{ movie.overview }} </p></div>
                      
                      
                      <div class="row my-3">
                        <p class="col" id="seconddetail">평점: {{ movie.vote_average }} </p>
                        <star-rating class="col" style="width:200px;" id=setstar :increment="0.1" :star-size="30" 
                        :show-rating="false" v-model="abcVote" :border-width="5" border-color="#d8d8d8" 
                        :rounded-corners="true" :read-only="true" ></star-rating>
                        <p class="col" id="seconddetail">관람객수: {{ movie.popularity }} </p>
                      </div>

                    </div>
                    <div v-if="moviePage===2">
                      <the-movie-star
                      :movie-num="Number($route.params.movieNum)"></the-movie-star>
                    </div>
                    <div v-if="moviePage===3">
                      <the-movie-same
                      :movie-id="Number(movie.id)"></the-movie-same>
                    </div>
                    <div v-if="moviePage===4">
                      <the-movie-service
                      :movie-no="Number($route.params.movieNum)"></the-movie-service>
                    </div>
                    <div v-if="moviePage===5">
                      <the-movie-youtube :tmdb-id="Number(movie.tmdb_id)"></the-movie-youtube>
                    </div>
                  </b-card-body>
                </b-card>
              </div>              
            </div>

          </div>
        </section>
      </div>
    </div>

    


  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import TheMovieStar from '@/components/movies/TheMovieStar'
import TheMovieSame from '@/components/movies/TheMovieSame'
import TheMovieService from '@/components/movies/TheMovieService'
import TheDetailGenre from '@/components/movies/TheDetailGenre'
import TheMovieYoutube from '@/components/movies/TheMovieYoutube'
import axios from 'axios'
import TheMovieLike from '@/components/movies/TheMovieLike.vue'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'MovieDetail',
  data: function() {
    return {
      movie:{
        "id": null,
        "tmdb_id": null,
        "title": null, 
        "poster_path": null, 
        "release_date": null, 
        "overview": null, 
        "vote_average": null, 
        "vote_count": null, 
        "popularity": null, 
        "runtime": null, 
        "genres": null,
        "like_users":null,
      },
      isLiked:null,
      page:1,
    }
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
    getMovie: function(){
      axios({
        methods: 'GET',
        url: `https://jwsh.link/movies/list/${this.$route.params.movieNum}`,
        headers: this.setToken()
      })
        .then(res=> {
          // console.log(res)
          this.movie = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    ...mapActions([
      'pageMovie',
    ])
  },
  computed: {
    abcVote: function() {
      return this.movie.vote_average/2
    },
    ...mapState([
      'isLogined','moviePage',
    ])
  },
  created: function() {
    this.getMovie() 
    if (this.isLogined==false){
      this.$router.push({name:'Login'})
    }
  },
  components:{
    TheMovieStar,
    TheMovieSame,
    TheMovieService,
    StarRating,
    TheMovieLike,
    TheDetailGenre,
    TheMovieYoutube,
  }

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@600&family=Jua&family=Song+Myung&display=swap');

#searchtext {
  /* font-family: 'IBM Plex Sans KR', sans-serif; */
  font-family: 'Jua', sans-serif;
  /* font-family: 'Song Myung', serif; */
}

#title { 
  font-family: 'IBM Plex Sans KR', sans-serif;
  /* font-family: 'Jua', sans-serif; */
  /* font-family: 'Roboto Mono', monospace; */
  /* font-family: 'Song Myung', serif; */
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

#thirddetail {
  font-family: 'Gowun Batang', serif;
  /* font-family: 'IBM Plex Sans KR', sans-serif; */
  /* font-family: 'Jua', sans-serif; */
  /* font-family: 'Roboto Mono', monospace; */
  /* font-family: 'Song Myung', serif; */
  font-weight: bold;
  color: rgb(88, 88, 88);
  margin: 20px;
}


</style>
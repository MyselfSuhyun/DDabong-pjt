<template>
  <div>
    <div class="container">
      <div class="row">
        <div id="title">
          <h1>영화 검색</h1>
        </div>
        <div id="searchtext" class="input-group my-4">
          <input class="form-control" type="text"
          @keyup.enter="comeData"
          v-model="inputWord"
          placeholder="영화 제목 / 내용을 입력하세요!">
          <button @click="comeData"
          class="btn btn-secondary">영화 검색</button>
        </div>
        <div id="detail">
          <h6>자세한 정보를 보시려면 영화를 클릭하세요!</h6>
        </div>
        <div id="seconddetail" v-show="show">
          <p>해당영화는 없습니다. 다시 검색해주세요.</p>
          <p>새로운 영화 등록을 요청하시려면 게시판을 이용해 주세요.</p>
        </div>
        <search-item v-show="!show" v-for="(movie, index) in searchedMovies"
        :key="index"
        :movie-item="movie"
        class="card-group col-3">
        </search-item>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import SearchItem from '@/components/search/SearchItem'
import { mapState } from 'vuex'

export default {
  name: 'Search',
  data:function() {
    return {
      inputWord: null,
      show: false
    }
  },
  components:{
    SearchItem,
  },
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    comeData: function() {
      const foundItem = {
        searched: this.inputWord,
      }
      axios({
        method: 'post',
        url: 'https://jwsh.link/movies/search/',
        data: foundItem,
        headers: this.setToken()
      })
        .then(res => {
          if(res.data.length){
            this.$store.dispatch('movieSearch',res.data)
            this.show = false
          }else{
            this.show = true
          }
          
          this.inputWord = ""
          
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  computed:{
    ...mapState([
      'searchedMovies','isLogined',
    ])
  },
  created: function(){
    if (this.isLogined==false){
      this.$router.push({name:'Login'})
    }
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
  font-family: 'IBM Plex Sans KR', sans-serif;
  /* font-family: 'Jua', sans-serif; */
  /* font-family: 'Roboto Mono', monospace; */
  /* font-family: 'Song Myung', serif; */
  color: rgb(155, 155, 155);
}
#seconddetail {
  font-family: 'Gowun Batang', serif;
  /* font-family: 'IBM Plex Sans KR', sans-serif; */
  /* font-family: 'Jua', sans-serif; */
  /* font-family: 'Roboto Mono', monospace; */
  /* font-family: 'Song Myung', serif; */
  color: rgb(0, 0, 0);
}

</style>
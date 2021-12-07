<template>
  <div>
    <div id="title" class="my-5">
      <h1>추가한 영화 목록 조회</h1>
    </div>
    <div id="movielist" class="container-fluid">
      <ul class="list-group col-8">
        <li class="list-group-item" v-for="movie in userMovies" :key="movie.id">
          <div>
            <div id="oneline"><input type="checkbox" v-model="checkedValues" :value="movie.id"></div>
            <div id="oneline"><span id="listtext">{{ movie.title }}</span></div>
            <div id="oneline"><button @click="deleteMovie(movie)" id="deletebtn" class="movie-btn btn btn-outline-secondary mx-3">X</button></div>           
          </div>
        </li>
      </ul>
    </div>
    <div style="padding-top: 20px; padding-bottom: 50px;">
      <button id="btn" class="btn btn-danger" @click="selectDelete">체크 삭제</button>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
import {mapState} from 'vuex'

export default {
  name: 'MovieList',
  data: function () {
    return {
      movies: null,
      checkedValues: []
    }
  },
  methods: {
    getMovies: function(){
      this.$store.dispatch('getMovies')
    },
    deleteMovie: function (movie) {
      axios({
        method: 'delete',
        url: `https://jwsh.link/movies/list/${movie.id}/`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`} 
      })
        .then((res) => {
          console.log(res)
          this.getMovies()
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 체크 박스에 있는 친구들 일괄 삭제
    selectDelete: function(){
      for (let movie_id of this.checkedValues){
        axios({
        method: 'delete',
        url: `https://jwsh.link/movies/list/${movie_id}/`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`} 
      })
        .then(() => {
          // console.log(res)
          this.getMovies()
        })
        .catch(err => {
          console.log(err)
        })
      }
    }
    // updateMovieStatus: function (movie) {
    //   const todoItem = {
    //     ...todo,
    //     is_completed: !todo.is_completed
    //   }

    //   axios({
    //     method: 'put',
    //     url: `https://jwsh.link/todos/${todo.id}/`,
    //     data: todoItem,
    //   })
    //     .then(res => {
    //       console.log(res)
    //       todo.is_completed = !todo.is_completed
    //     })
    //   },
    },
  // todo 가 생성될 떄에 자동으로 목록을 불러오겠다!
  computed:{
    ...mapState([
      'userMovies','isAdmined'])

  },
  created: function() {
    if (!this.isAdmined) {
      this.$router.push({name:'Home'})
    }else{
      this.getMovies()
    }
  }
}
</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .is-completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
  .is-not-completed{
    color: red;
  }

  #deletebtn{
    justify-content: end;
  }
  
  #movielist {
    display: flex;
    justify-content: center;
  }

  #oneline {
    display: inline-block;
  }

  #listtext {
    font-family: 'Gowun Batang', serif;
    /* font-family: 'IBM Plex Sans KR', sans-serif; */
    /* font-family: 'Jua', sans-serif; */
    /* font-family: 'Roboto Mono', monospace; */
    /* font-family: 'Song Myung', serif; */
  }

  #btn { 
    /* font-family: 'Gowun Batang', serif; */
    /* font-family: 'IBM Plex Sans KR', sans-serif; */
    font-family: 'Jua', sans-serif;
    /* font-family: 'Roboto Mono', monospace; */
    /* font-family: 'Song Myung', serif; */
  }
</style>

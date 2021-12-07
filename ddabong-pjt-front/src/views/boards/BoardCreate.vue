<template>
  <div>
    <div id="title">
      <h1> {{selectedGenreBoard.name}} 게시글 작성</h1>
    </div>
    <div class="container-fluid">
      <div class="row" style="padding:5%">
        <aside class="col-12 col-md-2">
          <the-genre-list></the-genre-list>
        </aside>
        <section class="col-12 col-md-10 offset-md-0">
          <div class="offset-1 col-10">
            <p><input id="inputtext"
              placeholder="제목을 입력해주세요." 
              type="text" class="form-control"
              v-model.trim="title" 
            ></p>
            <p><textarea id="inputtext"
                  class="form-control"
                  placeholder="내용을 입력해주세요."
                  rows= 10,
                  cols= 50,
                  v-model.trim="content" 
                >
                </textarea></p>
          </div>
          <button id="btn" class="btn btn-success mx-1 col-2" @click="boardBack">뒤로가기</button>
          <button id="btn" class="btn btn-primary mx-1 col-2" @click="createBoard">글작성</button>
        </section>
      </div>
    </div>


  </div>
</template>

<script>
import TheGenreList from '@/components/boards/TheGenreList'
import {mapState} from 'vuex'
import axios from 'axios'

export default {
  name: 'BoardCreate',
  data: function() {
    return {
      title: null,
      content: null,
      genre:null,
    }
  },
  
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    boardBack: function(){
      this.$router.push({name:'Boards'})
    },
    createBoard: function () {
      const todoItem = {
        title: this.title,
        content: this.content,
        genre: this.$store.state.selectedGenreBoard.id,
      }
      if (todoItem.title) {
        axios({
          method: 'post',
          url: 'https://jwsh.link/communities/',
          data: todoItem,
          headers: this.setToken()
        })
          .then(() => {
            this.$router.push({ name: 'Boards' })
          })
          .catch(err => {
            console.log(err)
          })
        }
      },
  },
  computed:{
    ...mapState([
      'selectedGenreBoard','isLogined'
    ])
  },
  created: function(){
    if (this.isLogined==false){
      this.$router.push({name:'Login'})
    }
  },
  components:{
    TheGenreList,
  }
}
</script>

<style>
  #btn {
    /* font-family: 'Gowun Batang', serif; */
    /* font-family: 'IBM Plex Sans KR', sans-serif; */
    font-family: 'Jua', sans-serif;
    /* font-family: 'Roboto Mono', monospace; */
    /* font-family: 'Song Myung', serif; */
  }

  #inputtext {
    /* font-family: 'Gowun Batang', serif; */
    font-family: 'IBM Plex Sans KR', sans-serif;
    /* font-family: 'Jua', sans-serif; */
    /* font-family: 'Roboto Mono', monospace; */
    /* font-family: 'Song Myung', serif; */
  }
</style>
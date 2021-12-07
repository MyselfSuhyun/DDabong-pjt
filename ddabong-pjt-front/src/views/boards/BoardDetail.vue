<template>
  <div>
    <div id="title">
      <h2>게시글</h2>
    </div>
    <div class="container">
      <div class="row" style="margin: 10%;;">
        <div class="card">
          <div class="card-header">
            <div id="seconddetail" class="card-title">제목: {{ board.title }}</div>
          </div>
          <div class="card-body">
            <p id="seconddetail" class="card-text my-5 mx-3">{{board.content}}</p>
          </div>
          <div class="card-footer text-muted row" style="height:40px">
            <p id="forthdetail" class="col">작성시간: {{ board.created_at | luxon }}</p>
            <p id="forthdetail" class="col">조회수 : {{board.hits}}</p>
            <p id="forthdetail" class="col">작성자: {{board.user.nickname}}({{board.user.username}}) </p>
          </div>      
        </div>
      </div>
    </div>

    <!-- 좋아요 버튼 -->
    <the-board-like
    :board-num="Number($route.params.boardNum)"></the-board-like>
    <the-comment-form
    :board-num="Number($route.params.boardNum)"></the-comment-form>
    <span v-if="isBoard">
      <button class="btn btn-secondary m-1" @click="moveUpdate">수정</button>
      <button class="btn btn-dark m-1" @click="boardDelete">삭제</button>
    </span>
  </div>
</template>

<script>
import TheBoardLike from '@/components/boards/TheBoardLike'
import TheCommentForm from '@/components/boards/TheCommentForm'

import axios from'axios'
import { mapState } from 'vuex'
export default {
  name: 'BoardDetail',
  data: function() {
    return {
      board :{ 
        "id": null, 
        "user": { "id": null, "nickname": null, "username":null },
        "title": null, 
        "content": null, 
        "image": null, 
        "hits": null, 
        "created_at": null, 
        "updated_at": null, 
        "genre": null, 
        "like_users": null, 
        "dislike_users": null
        },
      isBoard:null,
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
    moveUpdate: function() {
      this.$router.push({name:"BoardUpdate",params:{boardNum:this.board.id}})
    },
    boardDelete: function() {
      axios({
        method: 'delete',
        url: `https://jwsh.link/communities/${this.$route.params.boardNum}/`,
        headers: this.setToken()
      })
        .then(() => {
          this.$router.push({name:'Boards'})
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  computed:{
    ...mapState([
      'isLogined'
    ])
  },
  components:{
    TheBoardLike,
    TheCommentForm, 
  },
  created:function(){
    if (this.isLogined==false){
      this.$router.push({name:'Login'})
    }
  },
  beforeCreate: function() {
    axios({
      method: 'get',
      url: `https://jwsh.link/communities/${this.$route.params.boardNum}`,
      headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`} // Authorization: JWT tokensdjiadnoiqwnd
    })
      .then(res => {
        // console.log(res)
        this.board = res.data
        // console.log(res.data)
      })
      .catch(err => {
        console.log(err)
      })
    axios({
        methods: 'get',
        url: `https://jwsh.link/communities/${this.$route.params.boardNum}/communitystate/`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`}
      })
      .then(res=> {
        // console.log(res.data.isLiked)
        this.isBoard=res.data.isBoard
      })
      .catch(err => {
        console.log(err)
      })
  },
}
</script>

<style>
#forthdetail {
  font-family: 'Gowun Batang', serif;
  /* font-family: 'IBM Plex Sans KR', sans-serif; */
  /* font-family: 'Jua', sans-serif; */
  /* font-family: 'Roboto Mono', monospace; */
  /* font-family: 'Song Myung', serif; */
  font-weight: lighter;
  font-size: 11px;
  color: rgb(46, 46, 46);
}

</style>
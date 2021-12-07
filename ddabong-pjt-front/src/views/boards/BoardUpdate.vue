<template>
  <div class="row">
    <div id="title">
      <h1>게시글 수정</h1>
    </div>
    <div class="d-flex justify-content-center">
      <div class="col-12 col-sm-8 col-lg-6">
        <input id="inputtext"
          type="text" class="form-control"
          v-model.trim="board.title" 
        >  
        <p><textarea class="form-control" id="inputtext"
              rows= 10,
              cols= 50,
              v-model.trim="board.content" 
            >
            </textarea></p>
        <button id="btntext" class="btn btn-secondary" style="width:100px;" @click="boardBack">뒤로가기</button>
        <button id="btntext" class="btn btn-success" style="width:100px; " @click="updateBoard">글수정</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'BoardUpdate',
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
        }
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
     this.$router.push({name:"BoardDetail",params:{boardNum:this.board.id}})
    },
    updateBoard: function () {
      const todoItem = {
        ...this.board,
        title: this.board.title,
        content: this.board.content,
      }
      if (todoItem.title) {
        axios({
          method: 'put',
          url: `https://jwsh.link/communities/${this.board.id}/`,
          data: todoItem,
          headers: this.setToken()
        })
          .then(() => {
            this.$router.push({name:"BoardDetail",params:{boardNum:this.board.id}})
          })
          .catch(err => {
            console.log(err)
          })
        }
      },
  },
  computed:{
    ...mapState([
      'isLogined'
    ])
  },
  created: function(){
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
  }
}
</script>

<style>

</style>
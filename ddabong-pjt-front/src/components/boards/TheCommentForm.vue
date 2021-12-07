<template>
  <div>
    <div class="container-fluid">
      <div class="row">
        <div class="col-12 col-md-8 offset-md-2">
          <div class="input-group">
            <input 
              type="text" class="form-control row"
              v-model.trim="content" 
              @keyup.enter="createComment"
            >
            <button id="btntext" class="btn btn-success" @click="createComment">작성</button>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <the-comment-list-item   
      v-for="(comment,index) in comments"
      :key="index"
      :comment-item="comment"
      @comment-delete="getComments"></the-comment-list-item>
    </div>
  </div>
</template>

<script>
import TheCommentListItem from '@/components/boards/TheCommentListItem'
import axios from 'axios'
export default {
  name:'TheCommentForm',
  data: function() {
    return {
      content:null,
      comments:null,
    }
  },
  props:{
    boardNum:{
      type:Number
    },
  },
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    
    createComment: function () {
      const commentItem = {
        content: this.content,
      }

      if (commentItem.content) {
        axios({
          method: 'post',
          url: `https://jwsh.link/communities/${this.boardNum}/comments/`,
          data: commentItem,
          headers: this.setToken()
        })
          .then(() => {
            this.getComments()
            this.content = null
          })
          .catch(err => {
            console.log(err)
          })
        }
    },
    getComments: function () {
      axios({
        method: 'get',
        url: `https://jwsh.link/communities/${this.boardNum}/comments/`,
        headers: this.setToken() // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          this.comments = null,
          console.log(res.data)
          // console.log(res)
          this.comments = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created: function(){
    this.getComments()
  },
  components:{
    TheCommentListItem,
  } 
}
</script>

<style>

</style>
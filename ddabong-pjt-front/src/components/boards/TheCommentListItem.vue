<template>
  <div v-if="isDeleted">
    <div class="container-fluid">
      <div class="row">
        <div class="col-12 col-md-8 offset-md-2">
          <b-card class="text-start">
            <p>{{commentItem.user.nickname}}: 
              <span v-show="!updateState">{{content}}</span>
              <span v-show="isComment">
              <input v-show="updateState" v-model="tmp" type="text">
              <button id="seclittlebtn" class="btn btn-secondary btn-sm" v-show="!updateState" @click="updateContent">수정</button>
              <button id="seclittlebtn" class="btn btn-secondary btn-sm" v-show="updateState" @click="updateComplete">완료</button>
              <button id="seclittlebtn" class="btn btn-secondary btn-sm" v-show="updateState" @click="updateContent">취소</button>
              <button id="seclittlebtn" class="btn btn-secondary btn-sm" @click="commentDelete">삭제</button></span>
            </p>
          </b-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import Velocity from 'velocity-animate'
import axios from 'axios'
export default {
  name:'TheCommentListItem',
  data: function() {
    return{
      content:this.commentItem.content,
      tmp: this.commentItem.content,
      updateState:false,
      isComment: null,
      isDeleted: true,
    }
  },
  props:{
    commentItem: {
      type: Object
    },
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    updateContent: function() {
      this.updateState = !this.updateState
      this.tmp = this.content
    },
    updateComplete: function() {
      const updateItem = {
        ...this.commentItem,
        content:this.tmp
      }
      axios({
        method: 'put',
        url: `https://jwsh.link/communities/comment/${this.commentItem.id}/`,
        data: updateItem,
        headers: this.setToken()
      })
        .then(() => {
          this.content = this.tmp
          this.updateState = !this.updateState
        })
        .catch(err => {
          console.log(err)
        })
    },
    commentDelete: function() {
      axios({
        method: 'delete',
        url: `https://jwsh.link/communities/comment/${this.commentItem.id}/`,
        headers: this.setToken()
      })
      .then(() => {
        this.$router.go()
        // this.isDeleted=false
        // this.$emit('comment-delete')
      })
      .catch(err => {
        console.log(err)
      })
    },
  },
  created:function() {
      axios({
        methods: 'get',
        url: `https://jwsh.link/communities/comment/${this.commentItem.id}/commentstate/`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`}
      })
      .then(res=> {
        this.isComment=res.data.isComment
      })
      .catch(err => {
        console.log(err)
      })
  }

}
</script>

<style>
#seclittlebtn {
  /* font-family: 'Gowun Batang', serif; */
  /* font-family: 'IBM Plex Sans KR', sans-serif; */
  font-family: 'Jua', sans-serif;
  /* font-family: 'Roboto Mono', monospace; */
  /* font-family: 'Song Myung', serif; */
  color: rgb(53, 53, 53);
}
</style>
<template>
  <div>
    <div id="title">
      <h2>내가 쓴 글</h2>
    </div>
    <div v-for="(myboard,index) in myBoards" :key="index">
      <input type="checkbox" v-model="checkedValues" :value="myboard.id">
      <span @click="movieBoard(myboard.id)">{{myboard.genres}}{{myboard.title}} / {{myboard.content}}</span>
      <button @click="deleteBoard(myboard)">X</button>
    </div>
    <button id="btn" class="btn btn-secondary" @click="selectDelete">체크 삭제</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'TheMyBoards',
  data: function(){
    return {
      myBoards:Object,
      checkedValues: []
    }
  },
  props:{
    userName:String,
  },
  methods:{
    getMyBoards: function () {
      axios({
        method: 'get',
        url: `http://13.125.243.60/accounts/${this.userName}/myboards/`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
      })
        .then(res => {
          this.myBoards = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteBoard: function (board) {
      axios({
        method: 'delete',
        url: `http://13.125.243.60/communities/${board.id}/`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
      })
        .then(() => {
          // console.log(res)
          this.getMyBoards()
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 체크 박스에 있는 친구들 일괄 삭제
    selectDelete: function(){
      for (let myBoard_id of this.checkedValues){
        axios({
        method: 'delete',
        url: `http://13.125.243.60/communities/${myBoard_id}/`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
      })
        .then(() => {
          // console.log(res)
          this.getMyBoards()
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
    movieBoard: function(board_id) {
      this.$router.push({name:"BoardDetail",params:{board_id}})
    }
  },

  created: function(){
    this.getMyBoards()
  },
}
</script>

<style>

</style>
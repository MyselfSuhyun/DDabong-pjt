<template>
  <div>
    <div id="secondtitle" class="my-4">
      <h4>게시판 조회수 랭킹</h4>
    </div> 
    <div class="container-fluid">
      <div class="row mx-4">
        <table class="table table-secondary table-hover">
          <thead>
            <tr>
              <th id="seconddetail" scope="col">랭킹</th>
              <th id="seconddetail" scope="col">제목</th>
              <th id="seconddetail" scope="col">작성자</th>
              <th id="seconddetail" scope="col">조회수</th>
              <th id="seconddetail" scope="col">좋아요</th>
            </tr>
          </thead>
          <tbody>
            <tr  v-for="(board,index) in likeboards" :key="index" @click="moveBoard(board.id)">
              <td id="listtext" scope="col">{{index+1}}</td>
              <td id="listtext" scope="col">{{board.title}}</td>
              <td id="listtext" scope="col">{{board.user.nickname}}</td>
              <td id="listtext" scope="col">{{board.hits}}</td>
              <td id="listtext" scope="col">{{board.like_users.length}}</td>
            </tr>
          </tbody>
        </table>     
      </div>  
    </div>   

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'TheRankingBoard',
  data:function(){
    return {
      likeboards : Object
    }
  },
  methods:{
    moveBoard: function(board_id){
      this.$router.push({name: 'BoardDetail', params:{boardNum:board_id}})
    },
  },
  created: function() {
    axios({
      method: 'get',
      url: 'https://jwsh.link/communities/ranking/',
      headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`}
    })
      .then(res => {
        this.likeboards = res.data
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style>
#listtext {
  /* font-family: 'Gowun Batang', serif; */
  font-family: 'IBM Plex Sans KR', sans-serif;
  /* font-family: 'Jua', sans-serif; */
  /* font-family: 'Roboto Mono', monospace; */
  /* font-family: 'Song Myung', serif; */
  color: rgb(53, 53, 53);
}
</style>
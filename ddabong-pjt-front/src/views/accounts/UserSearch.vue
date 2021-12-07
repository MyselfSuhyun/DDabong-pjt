<template>
  <div>
   <div class="container">
      <div class="row">
        <div id="title">
          <h1>유저검색(닉네임 or 아이디)</h1>
        </div>
        <div id="searchtext" class="input-group my-4">
          <input class="form-control" type="text"
          @keyup.enter="searchProfile"
          v-model="userSearch"
          placeholder="검색할 닉네임 또는 아이디를 입력하세요!">
          <button @click="searchProfile"
          class="btn btn-secondary">유저 검색</button>
        </div>
        <div id="detail">
          <h6>유저프로필을 확인하려면 아래 버튼을 클릭하세요!</h6>
        </div>
        <br>
        <p id="thirddetail" v-show="show">해당 유저는 없습니다. 다시 검색해주세요.</p>
        <div v-show="!show" v-for="(user,index) in searchedUsers"
        :key=index class="card-group col-3">
        <!-- 이미지 동그라게 해줄수있나용? -->
        <!-- 넹!! -->
          <div class="box" style="background: #BDBDBD;">
            <img class="profile" :src="imgSelect(user.image)" alt="">
          </div>        
          <span><button id="btntext" class="btn" @click="moveProfile(user.username)">{{user.nickname}}님 프로필 보기</button></span>
        </div>        
      </div>
    </div>
  </div>

</template>

<script>
import Img from "@/assets/profile-example.gif"
import axios from 'axios'
import { mapState } from 'vuex'
export default {
  name:'UserSearch',
  data: function() {
    return {
      userSearch:null,
      show:false,
    }
  },
  methods:{
    searchProfile: function(){
      const searchItem = {
        usersearch: this.userSearch,
      }
      if(searchItem.usersearch){
        axios({
        method: 'post',
        url: `https://jwsh.link/accounts/search/`,
        headers: {Authorization: `JWT ${localStorage.getItem('jwt')}`},
        data: searchItem
        })
        .then(res => {
          if(res.data.length){
            this.$store.dispatch('userSearch',res.data)
            this.show = false
          }else{
            this.show = true
          }
          this.userSearch=null
          // console.log(res)
        })
        .catch(err => {
          console.log(err)
        }) 
      }
    },
    imgSelect: function(image) {
      if (image){
        return `https://jwsh.link${image}`
      }else {
        return Img
      }
    },
    moveProfile: function(moveName){
      this.$router.push({name: 'Profile', params:{userName:moveName}})
    },
  },
  computed:{
    ...mapState([
      'searchedUsers','isLogined'
    ])
  },
  created:function(){
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

  .box {
    width:150px;
    height:150px;
    border-radius:70%;
    overflow:hidden;
  }
  
  .profile {
    width: 100%;
    height:100%;
    object-fit: cover;
  }
</style>
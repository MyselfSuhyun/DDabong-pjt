<template>
  <div>
    <div class="container">
      <br>
      <div class="row">
        <div class="col">
          <img :src="king" alt="king" style="width:30px">
          <div id="secondtitle">
            <h4>1위</h4>
          </div>  
          <div @click="moveFirstProfile">
            <div id="seconddetail">
              <h4>{{firstuser.nickname}}({{firstuser.username}})</h4>
            </div>            
            <img :src="imgSelect(firstuser.image)" alt="">
          </div>
        </div>
        <div class="col">
          <img :src="crown" alt="crown" style="width:30px">
          <div id="secondtitle">
            <h4>순위 목록</h4>
          </div>   
          <hr>
          <div v-for="(user,index) in likeusers" :key="index">
            <div id="seconddetail" @click="moveProfile(user.username)">
              <p>{{index+1}} 등: {{user.nickname}}({{user.username}}) 팔로워 : {{user.followers.length}} 명</p>
              <hr>
            </div>
          </div>
        </div>
      </div>
    </div>



  </div>
</template>

<script>
import Img from "@/assets/profile-example.gif"
import axios from 'axios'
import crown from "@/assets/crown.png"
import king from "@/assets/king.png"

export default {
  name:'TheRankingFollower',
  data: function(){
    return {
      firstuser:Object,
      likeusers:Object,
      crown,
      king,
    }
  },
  methods:{
    imgSelect: function(userimage) {
      if (userimage){
        return `https://jwsh.link${userimage}`
      }else {
        return Img
      }
    },
    moveFirstProfile: function(){
      this.$router.push({name: 'Profile', params:{userName:this.firstuser.username}})
    },
    moveProfile: function(username){
      this.$router.push({name: 'Profile', params:{userName:username}})
    },
  },
  created: function() {
    axios({
      method: 'get',
      url: 'https://jwsh.link/movies/rankingfr/',
      headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`}
    })
      .then(res => {
        this.firstuser = res.data[0]
        this.likeusers = res.data
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style>

</style>
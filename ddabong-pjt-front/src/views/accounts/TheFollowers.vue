<template>
  <div>
    <button id="btntext" class="btn btn-secondary" @click="back">뒤로가기</button>
      <div v-for="(follower,index) in followers" :key="index">
        <span>{{follower.nickname}}({{follower.username}}}</span>
        <the-followers-movie :movie-item="follower.like_movies"></the-followers-movie>
         <button id="btntext" class="btn btn-success" @click="moveProfile(follower.username)" > 프로필이동</button>
      </div>
  </div>
</template>

<script>
import TheFollowersMovie from '@/components/accounts/TheFollowersMovie'
import axios from 'axios'
import { mapState } from 'vuex'
export default {
  name:'TheFollowers',
  data: function(){
    return {
      followers:Object,
    }
  },
  methods:{
    getFollowers: function () {
      axios({
        method: 'get',
        url: `https://jwsh.link/accounts/${this.$route.params.userName}/followers/`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
      })
        .then(res => {
          // console.log(res.data)
          // console.log(res)
          this.followers = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    moveProfile: function(moveName){
      this.$router.push({name: 'Profile', params:{userName:moveName}})
    },
    back: function() {
      this.$router.go(-1)
    },
  },
  computed:{
    ...mapState([
      'isLogined'
    ])
  },
  created:function(){
    this.getFollowers()
    if (this.isLogined==false){
      this.$router.push({name:'Login'})
    }
  },
  components:{
    TheFollowersMovie
  }
}
</script>

<style>

</style>
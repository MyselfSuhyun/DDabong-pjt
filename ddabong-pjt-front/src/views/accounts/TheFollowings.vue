<template>
  <div>
    <button id="btntext" class="btn btn-secondary" @click="back">뒤로가기</button>
      <div v-for="(following,index) in followings" :key="index">
        <span>{{following.nickname}}({{following.username}}}</span>
        <the-followings-movie :movie-item="following.like_movies"></the-followings-movie>
         <button id="btntext" class="btn btn-secondary" @click="moveProfile(following.username)"> 프로필이동</button>
      </div>
  </div>
</template>

<script>
import TheFollowingsMovie from '@/components/accounts/TheFollowingsMovie'
import axios from 'axios'
import { mapState } from 'vuex'
export default {
  name:'TheFollowings',
  data: function(){
    return {
      followings:Object,
    }
  },
  methods:{
    getFollowings: function () {
      axios({
        method: 'get',
        url: `https://jwsh.link/accounts/${this.$route.params.userName}/followings/`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
      })
        .then(res => {
          // console.log(res.data)
          // console.log(res)
          this.followings = res.data
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
    this.getFollowings()
    if (this.isLogined==false){
      this.$router.push({name:'Login'})
    }
  },
  components:{
    TheFollowingsMovie
  }
}
</script>

<style>

</style>
<template>
  <div>
    <div v-if="isValid">
      <div v-show="isFollowed">
        <button id="btntext" class="btn btn-secondary" @click="likeUser">팔로우 취소</button>
      </div>
      <div v-show="!isFollowed">
        <button id="btntext" class="btn btn-secondary" @click="likeUser">팔로우</button>
      </div>
    </div>

    <div class="row my-3" style="padding-right:30%; padding-left:30%;">
      <div id="detail" class="col"><p>팔로잉 수: <span @click="moveFollowings">{{followings}}</span></p></div>
      <div id="detail" class="col"><p>팔로워 수: <span @click="moveFollowers">{{followers}}</span></p></div>   
    </div>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'TheUserLike',
  data:function(){
    return {
      isFollowed:null,
      followings:0,
      followers:0,
    }
  },
  props:{
    userName:String,
    isValid:Boolean,
  },
  
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    likeUser: function(){
      axios({
        methods: 'get',
        url: `http://13.125.243.60/accounts/${this.userName}/follow/`,
        headers: this.setToken()
      })
      .then(res=> {
        this.isFollowed=!res.data.isFollowed
        this.followings = res.data.followings
        this.followers = res.data.followers
      })
      .catch(err => {
        console.log(err)
      })
    },
    likeUsered: function(){
      axios({
        methods: 'get',
        url: `http://13.125.243.60/accounts/${this.userName}/followed/`,
        headers: this.setToken()
      })
      .then(res=> {
        this.isFollowed=res.data.isFollowed
        this.followings = res.data.followings
        this.followers = res.data.followers
      })
      .catch(err => {
        console.log(err)
      })
    },
    moveFollowings: function(){
      this.$router.push({name: 'TheFollowings', params:{userName:this.userName}})
    },
    moveFollowers: function(){
      this.$router.push({name: 'TheFollowers', params:{userName:this.userName}})
    }
  },
  mounted: function() {
    this.likeUsered()
  },
}
</script>

<style>

</style>
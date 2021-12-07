<template>
  <div>
    <div class="row">
      <div class="col">
        <div v-show="isLiked">
          <button class="btn btn-outline-primary" @click="likeBoard">
            <img :src="ddabong" alt="like" style="width:100px; color:blue;">
          </button>
        </div>
        <div v-show="!isLiked">
          <button class="btn btn-outline" @click="likeBoard">
            <img :src="ddabong" alt="emptyLike" style="width:100px">
          </button>
        </div>
        <p id="thirddetail">좋아요 <span>{{likeCount}}명</span></p>
      </div>
      <div class="col">
        <div v-show="disLiked">
          <button class="btn btn-outline-danger" @click="disLikeBoard">
            <img :src="nono" alt="" style="width:100px;, color:red;">
          </button>
        </div>
        <div v-show="!disLiked">
          <button class="btn btn-outline" @click="disLikeBoard">
            <img :src="nono" alt="" style="width:100px;">
          </button>
        </div>
        <p id="thirddetail">싫어요 <span>{{disLikeCount}}명</span></p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ddabong from '@/assets/ddabong.png'
import nono from '@/assets/nono.png'

export default {
  name:'TheBoardLike',
  data: function() {
    return {
      isLiked:null,
      disLiked:null,
      likeCount:null,
      disLikeCount:null,
      ddabong,
      nono,
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
    likeBoard: function(){
      axios({
        methods: 'get',
        url: `https://jwsh.link/communities/${this.boardNum}/likes/`,
        headers: this.setToken()
      })
      .then(()=> {
        // console.log(res.data)
        this.likeState()
      })
      .catch(err => {
        console.log(err)
      })
    },
    disLikeBoard: function(){
      axios({
        methods: 'get',
        url: `https://jwsh.link/communities/${this.boardNum}/dislikes/`,
        headers: this.setToken()
      })
      .then(()=> {
        // console.log(res.data)
        this.likeState()
      })
      .catch(err => {
        console.log(err)
      })
    },
    likeState: function(){
      axios({
        methods: 'get',
        url: `https://jwsh.link/communities/${this.boardNum}/likestate/`,
        headers: this.setToken()
      })
      .then(res=> {
        // console.log(res.data)
        this.isLiked=res.data.isLiked
        this.disLiked=res.data.disLiked
        this.likeCount=res.data.likeCount
        this.disLikeCount=res.data.disLikeCount
      })
      .catch(err => {
        console.log(err)
      })
    },
  },
  created: function() {
    this.likeState()
  }
}
</script>

<style>

</style>
<template>
  <div >
    <div>
      <vue-profile 
        :nickname="(user.nickname+'('+user.username+')')"
        bodyPhrase="스티치 귀여워"
        :socialLinks="myLinks"
        :profileImg="imgSelect()"
        :coverImg="backImg"
      />
    </div>
    <!--  -->
    <div>
      <b-button id="btntext" class="btn btn-secondary" v-if="isValid" v-b-modal="'my-modal'">개인정보수정</b-button>
      <b-modal id='my-modal' hide-footer>
      <!-- The modal -->
      <the-change-information 
        :user-info="user" 
        @get-to-change="getToChange"></the-change-information>
      </b-modal>
      <the-profile-mylinks v-if="isChange"></the-profile-mylinks>
      <b-button id="btntext" class="btn btn-secondary" v-if="isValid" v-b-modal.modal-prevent-closing>SNS링크수정</b-button>
      <b-button id="btntext" class="btn btn-secondary" v-if="isValid" @click="myBoards">내가 쓴글 보기</b-button>
      <the-user-like :is-valid="!isValid"
      :user-name="userName"></the-user-like>
      <the-like-movies v-show="!isBoard"
      :user-name="userName"></the-like-movies>
      <the-my-boards v-show="isBoard"
      :user-name="userName"></the-my-boards>
      <b-modal
        id="modal-prevent-closing"
        ref="modal"
        title="SNS 계정을 입력해주세요"
        @ok="handleOk"
      >
        <form ref="form" @submit.stop.prevent="handleSubmit">
          <b-form-group
            class="input-group-text"
            label="facebook"
            label-for="facebook-input"
          >
          <b-form-input
            id="facebook-input"
            class="form-control mx-3"
            v-model="tmpLinks.facebook"
            required
            ></b-form-input>
          </b-form-group>
          <b-form-group
            class="input-group-text"
            label="twitter"
            label-for="twitter-input"
          >
          <b-form-input
            id="twitter-input"
            class="form-control mx-3"
            v-model="tmpLinks.twitter"
            required
            ></b-form-input>
          </b-form-group>
          <b-form-group
            class="input-group-text"
            label="youtube"
            label-for="youtube-input"
          >
          <b-form-input
            id="youtube-input"
            class="form-control mx-3"
            v-model="tmpLinks.youtube"
            required
            ></b-form-input>
          </b-form-group>
          <b-form-group
            class="input-group-text"
            label="instagram"
            label-for="instagram-input"
          >
          <b-form-input
            id="instagram-input"
            class="form-control mx-3"
            v-model="tmpLinks.instagram"
            required
            ></b-form-input>
          </b-form-group>
          <b-form-group
            class="input-group-text"
            label="git"
            label-for="git-input"
          >
          <b-form-input
            id="git-input"
            class="form-control mx-3"
            v-model="tmpLinks.git"
            required
            ></b-form-input>
          </b-form-group>
        </form>
      </b-modal>
    </div>
  </div>
</template>

<script>
import TheLikeMovies from '@/components/accounts/TheLikeMovies'
import TheUserLike from '@/components/accounts/TheUserLike'
import TheMyBoards from '@/components/accounts/TheMyBoards'
import TheChangeInformation from '@/components/accounts/TheChangeInformation'
// npm i vue-profile
import Img from "@/assets/profile-example.gif"
import backImg from "@/assets/background.jpg"
import axios from 'axios'
import { mapState } from 'vuex'
export default {
  name:'Profile',
  data: function() {
    return {
      userName: this.$route.params.userName,
      user:{
        id: null, 
        username: null, 
        nickname: null,
        image: null,
      },
      myLinks: { 
        facebook:null,
        twitter:null,
        youtube:null,
        instagram:null,
        git:null,
      },
      tmpLinks: {
        facebook:"",
        twitter:"",
        youtube:"",
        instagram:"",
        git:"",
      },
      isValid:false,
      isBoard:false,
      submittedNames: [],
      Img,
      backImg,

    }
  },
  methods:{
    getToChange: function() {
      this.getProfile()
      this.$router.go()
    },
    imgSelect: function() {
      if (this.user.image){
        return `https://jwsh.link${this.user.image}`
      }else {
        return Img
      }
    },
    myBoards:function(){
      this.isBoard=!this.isBoard
    },
    handleOk(bvModalEvt) {
      bvModalEvt.preventDefault()
      this.handleSubmit()
    },
    handleSubmit() {
      if(this.links_id){
        this.updateMylinks()
      }else{
        this.createMylinks()
      }
      // Hide the modal manually
      this.$nextTick(() => {
        this.$bvModal.hide('modal-prevent-closing')
      })
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    changeUser: function(){
      this.isChange= true
    },
    getProfile: function () {
      axios({
        method: 'get',
        url: `https://jwsh.link/accounts/${this.userName}`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`} // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          this.user = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    getMylinks: function () {
      if(this.isValid){     
        axios({
          method: 'get',
          url: `https://jwsh.link/accounts/${this.userName}/mylinks/`,
          headers: this.setToken() // Authorization: JWT tokensdjiadnoiqwnd
        })
          .then(res => {   
            if(res.data[0].facebook){
              this.tmpLinks.facebook=res.data[0].facebook
              this.myLinks.facebook="https://www.facebook.com/"+this.tmpLinks.facebook
            }else{
              this.myLinks.facebook=null
            }
            if(res.data[0].twitter){
              this.tmpLinks.twitter=res.data[0].twitter
              this.myLinks.twitter="https://twitter.com/"+this.tmpLinks.twitter
            }else{
              this.myLinks.twitter=null
            }
            if(res.data[0].instagram){
              this.tmpLinks.instagram=res.data[0].instagram
              this.myLinks.instagram="https://www.instagram.com/"+this.tmpLinks.instagram
            }else{
              this.myLinks.instagram=null
            }
            if(res.data[0].youtube){
              this.tmpLinks.youtube=res.data[0].youtube
              this.myLinks.youtube="https://www.youtube.com/channel/"+this.tmpLinks.youtube
            }else{
              this.myLinks.youtube=null
            }
            if(res.data[0].git){
              this.tmpLinks.git=res.data[0].git
              this.myLinks.git="https://github.com/"+this.tmpLinks.git
            }else{
              this.myLinks.git=null
            }
            if(res.data[0].id){
              this.links_id = res.data[0].id
            }

          })
          .catch(err => {
            console.log(err)
          })
      }
    },
    createMylinks: function () {

      if (this.tmpLinks) {
        axios({
          method: 'post',
          url: `https://jwsh.link/accounts/${this.userName}/mylinks/`,
          data: this.tmpLinks,
          headers: this.setToken()
        })
          .then(() => {
            this.getMylinks()
          })
          .catch(err => {
            console.log(err)
          })
        }
    },
    updateMylinks: function () {
      const updateMylinks = {
        ...this.tmpLinks
      }
      axios({
        method: 'put',
        url: `https://jwsh.link/accounts/${this.links_id}/linksupdate/`,
        data: updateMylinks,
        headers: this.setToken()
      })
        .then(() => {
          this.getMylinks()
        })
      },
    validationUser: function(){
      axios({
        method: 'get',
        url: `https://jwsh.link/accounts/${this.userName}/validation/`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`} // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          this.isValid=res.data.isValid
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  computed:{
    ...mapState([
      'isLogined'
    ]),
  },
  created: function(){
    this.getProfile()
    this.validationUser()
    this.getMylinks()
    if (this.isLogined==false){
      this.$router.push({name:'Login'})
    }
  },
  components:{
    TheLikeMovies,
    TheUserLike,
    TheMyBoards,
    TheChangeInformation,
  }

}
</script>

<style>

</style>
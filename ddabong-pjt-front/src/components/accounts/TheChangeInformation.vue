<template>
  <div class="file-upload">
    <form @submit.prevent="formSubmit" method="post">
      <span id="detail">닉네임</span>
      <input class="form-control"
      placeholder="NICKNAME"
      type="text"
      v-model="nickname"><br>
      <span id="detail">비밀번호</span>
      <input class="form-control"
      placeholder="PASSWORD"
      type="password"
      v-model="password"><br>
      <!-- <span>새로운비밀번호</span>
      <input class="form-control"
      placeholder="변경될 비밀번호"
      type="password"
      v-model="newpassword"><br>
      <span>새로운비밀번호확인</span>
      <input class="form-control"
      placeholder="변경될 비밀번호확인"
      type="password"
      v-model="newpasswordConfirm"> -->
      
      <p id="detail">프로필 사진</p>
      <img v-if="previewImgUrl" :src="previewImgUrl" style="width:50%"/>
      <input class="form-control" type="file" ref="selectFile" @change="previewFile" />
      <ul v-if="selectFile">
      </ul> 
      <div class="container">
        <div class="row">
          <button class="btn btn-secondary my-3" type="submit" :disabled="isUploading">정보수정</button>
        </div>
      </div>
      
      <!-- <div>
        <hr />
        response : {{ response }}
      </div> -->
    </form>
  </div>
</template>

<script>
import http from "@/http"
export default {
  name:'TheChangeInformation',
  data: function() {
    return {
      nickname:this.userInfo.nickname,
      password:null,
      newpassword:null,
      newpasswordConfirm:null,
      selectFile: null, // 파일 객체
      previewImgUrl: null, // 미리보기 이미지 URL
      isUploading: false, // 파일 업로드 체크
      response: null, // 파일 업로드후 응답값
    }
  },
  methods: {
      previewFile() {
        // 선택된 파일이 있는가?
        if (0 < this.$refs.selectFile.files.length) {
          // 0 번째 파일을 가져 온다.
          this.selectFile = this.$refs.selectFile.files[0]
          // 마지막 . 위치를 찾고 + 1 하여 확장자 명을 가져온다.
          let fileExt = this.selectFile.name.substring(
            this.selectFile.name.lastIndexOf(".") + 1
          )
          // 소문자로 변환
          fileExt = fileExt.toLowerCase()
          // 이미지 확장자 체크, 1메가 바이트 이하 인지 체크
          if (
            ["jpeg","jpg", "png", "gif", "bmp"].includes(fileExt) &&
            this.selectFile.size <= 1048576
          ) {
            // FileReader 를 활용하여 파일을 읽는다
            var reader = new FileReader()
            reader.onload = e => {
              // base64
              this.previewImgUrl = e.target.result
              console.log(this.previewImgUrl)
            }
            reader.readAsDataURL(this.selectFile)
          } else if (this.selectFile.size <= 1048576) {
            // 이미지외 파일
            this.previewImgUrl = null
          } else {
            alert("파일을 다시 선택해 주세요.")
            this.selectFile = null
            this.previewImgUrl = '127.0.0.1:8000'+this.userInfo.image
          }
        } else {
          // 파일을 선택하지 않았을때
          this.selectFile = null
          this.previewImgUrl = '127.0.0.1:8000'+this.userInfo.image
        }
        console.log(this.selectFile)
      },

      async formSubmit() {
        if (this.password) {
          let form = new FormData()
          if(this.selectFile){
            form.append("image", this.selectFile) // api file name
            }
          form.append("password",this.password)
          form.append("nickname",this.nickname)
          form.append("username",this.userInfo.username)
          // form.append("newpassword",this.newpassword)
          // form.append("newpasswordConfirm",this.newpasswordConfirm)
          // const userform = {
          //   ...this.userInfo,
          //   nickname: this.nickname,
          //   password: this.password,
          //   // image: this.selectFile,
          //   newpassword: this.newpassword,
          //   newpasswordConfirm: this.newpasswordConfirm
          // }
          this.isUploading = true
          http
            .post(`/accounts/${this.userInfo.username}/upload/`, form, {
              headers: {
                "Content-Type": "multipart/form-data",
                Authorization: `JWT ${localStorage.getItem('jwt')}`
              },
            })
            .then(res => {
              this.response = res
              this.nickname = res.data.nickname
              this.isUploading = false
              this.$emit('get-to-change')
            })
            .catch(error => {
              this.response = error
              this.isUploading = false
            })
        } else {
          alert("현재 비밀번호를 입력해야 수정 가능합니다.")
        }

        return true
      },
    },
    created: function(){
      if (this.userInfo.image){
        return this.previewImgUrl = `http://13.125.243.60${this.userInfo.image}`
      }
    },
    props:{
      userInfo:Object,
    },

}
</script>

<style>

</style>
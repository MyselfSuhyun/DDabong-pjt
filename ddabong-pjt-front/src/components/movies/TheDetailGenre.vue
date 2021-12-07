<template>
  <span>
    {{result}},
  </span>
</template>

<script>
export default {
  name:'TheDetailGenre',
  data:function(){
    return {
      result:null,
    }
  },
  props:{
    genreItem:Number,
  },
  created:function(){
    if(this.genreItem==28){
      this.result="액션"
    } else if (this.genreItem==12){
      this.result="모험"
    } else if(this.genreItem==16){
      this.result="애니메이션"
    } else if(this.genreItem==35){
      this.result="코미디"
    } else if (this.genreItem==80){
      this.result="범죄"
    } else if(this.genreItem==99){
      this.result="다큐멘터리"
    } else if(this.genreItem==18){
      this.result="드라마"
    } else if (this.genreItem==10751){
      this.result="가족"
    } else if(this.genreItem==14){
      this.result="판타지"
    } else if(this.genreItem==36){
      this.result="역사"
    } else if (this.genreItem==27){
      this.result="공포"
    } else if(this.genreItem==10402){
      this.result="음악"
    } else if(this.genreItem==9648){
      this.result="미스터리"
    } else if (this.genreItem==10749){
      this.result="로맨스"
    } else if(this.genreItem==878){
      this.result="SF"
    } else if(this.genreItem==10770){
      this.result="TV 영화"
    } else if (this.genreItem==53){
      this.result="스릴러"
    } else if(this.genreItem==10752){
      this.result="전쟁"
    } else if(this.genreItem==37){
      this.result="서부"
    }
    
  }
}
</script>

<style>

</style>
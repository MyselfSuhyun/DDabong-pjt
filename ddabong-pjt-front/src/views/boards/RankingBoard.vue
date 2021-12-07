<template>
  <div>
    <div id="title">
      <h2>랭킹게시판</h2>
    </div>
    
    <div class="row" style="margin-left:5%; margin-right:5%;">
      <button class="col btn btn-outline-light" @click="pageRanking(1)">영화랭킹</button>
      <button class="col btn btn-outline-light" @click="pageRanking(2)">장르랭킹</button>
      <button class="col btn btn-outline-light" @click="pageRanking(3)">팔로워랭킹</button>
      <button class="col btn btn-outline-light" @click="pageRanking(4)">게시판랭킹</button>
    </div>
    
    <the-ranking-movie v-show="rankingPage==1"></the-ranking-movie>
    <the-ranking-genre v-show="rankingPage==2"></the-ranking-genre>
    <the-ranking-follower v-show="rankingPage==3"></the-ranking-follower>
    <the-ranking-board v-show="rankingPage==4"></the-ranking-board>
  </div>
</template>

<script>
import TheRankingMovie from '@/components/boards/TheRankingMovie'
import TheRankingGenre from '@/components/boards/TheRankingGenre'
import TheRankingFollower from '@/components/boards/TheRankingFollower'
import TheRankingBoard from '@/components/boards/TheRankingBoard'
import {mapActions, mapState} from 'vuex'
export default {
  name:'Ranking',
  data: function() {
    return {
      page : 1,
    }
  },
  methods:{
    ...mapActions([
      'pageRanking'
    ])
  },
  components:{
    TheRankingMovie,
    TheRankingGenre,
    TheRankingFollower,
    TheRankingBoard,
  },
  computed:{
    ...mapState([
      'isLogined','rankingPage',
    ])
  },
  created: function(){
    if (this.isLogined==false){
      this.$router.push({name:'Login'})
    }
  }
}
</script>

<style>

</style>
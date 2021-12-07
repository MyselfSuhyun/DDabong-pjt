<template>
  <div class="movie">
    <div id="title" class="my-5">
      <h1>영화 검색</h1>
    </div>
    <div id="inputformin">
      <the-movie-search @keyup.enter.native="onKeywordEnter"></the-movie-search>
    </div>
    
    <div id="detail" class="my-5">
      <h4>검색어 : {{ keyword }}</h4>
    </div>
    <section>
      <the-movie-list></the-movie-list>
    </section>
  </div>
</template>

<script>
import TheMovieSearch from '@/components/admin/TheMovieSearch'
import TheMovieList from '@/components/admin/TheMovieList'
import {mapState} from 'vuex'
export default {
  name: 'Movie',
  data: function() {
    return {
      video:null,
    }
  },
  methods:{
    onKeywordEnter: function(){
      this.$store.dispatch('updateMovieList')
    }
  },
  components:{
    TheMovieSearch,
    TheMovieList,
  },
  computed:{
    ...mapState([
      'keyword','isAdmined'])

  },
  created: function() {
    if (!this.isAdmined) {
      this.$router.push({name:'Home'})
    }
  }

}
</script>

<style>
#inputformin {
  display:flex;
  justify-content: center;
  align-content: center;
  padding-top:30px;
  padding-bottom: 20px;
}
</style>
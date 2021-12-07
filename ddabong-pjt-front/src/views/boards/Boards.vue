<template>
  <div>
    <div id="title" class="my-5">
      <h1>{{ selectedGenreBoard.name }} 게시판</h1>
    </div>
    <div class="container-fluid">
      <div class="row" style="padding:5%">
        <aside class="col-12 col-md-2">
          <the-genre-list></the-genre-list>
        </aside>
        <section class="col-12 col-md-10 offset-md-0">
          <the-board-list></the-board-list>
        </section>
        
      </div>
    </div>
  </div>
</template>

<script>
import TheGenreList from '@/components/boards/TheGenreList'
import TheBoardList from '@/components/boards/TheBoardList'
import {mapState} from 'vuex'
export default {
  name: 'Boards',
  components:{
    TheGenreList,
    TheBoardList,
  },
  computed:{
    ...mapState([
      'selectedGenreBoard','isLogined'
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
/* #genrelist {
  display: inline-flex;
  justify-content: flex-start;
} */
</style>
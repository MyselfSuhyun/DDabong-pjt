<template>
  <div>
    <div class="row">
      <div id="title">
        <h1>장르 게시판</h1>
      </div>
      <div id="detail">
        <h5>선택한 장르 : {{selectedGenre.name}}</h5>
      </div>
      <div class="container-fluid">
        <div class="row" style="padding:5%">
          <aside class="col-12 col-md-2">
            <the-genre-list></the-genre-list>
          </aside>
          <section class="col-12 col-md-10 offset-md-0">
            <the-genre-search-list></the-genre-search-list>
            <!-- 페이지네이션 : 함수 걸러 돌아와라 나자신 -->
            <!-- <nav aria-label="Page navigation example">
              <ul class="pagination">
                <li class="page-item">
                  <a class="page-link" href="#" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                  </a>
                </li>
                <li class="page-item"><a class="page-link" href="#">1</a></li>
                <li class="page-item"><a class="page-link" href="#">2</a></li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
                <li class="page-item">
                  <a class="page-link" href="#" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                  </a>
                </li>
              </ul>
            </nav> -->
          </section>
          
        </div>
      </div>
    </div>    
  </div>

</template>

<script>
// import TheMovieSearch from '@/components/TheMovieSearch'
import TheGenreList from '@/components/genresearch/TheGenreList'
import TheGenreSearchList from '@/components/genresearch/TheGenreSearchList'
import {mapState,mapActions} from 'vuex'
export default {
  name: 'GenreSearch',
  components:{
    TheGenreList,
    TheGenreSearchList,
  },
  methods:{
    ...mapActions([
      'getMovies',
    ])
  },
  computed:{
    ...mapState([
      'selectedGenre','isLogined',
    ]),
  },
  created: function(){
    this.getMovies()
    if (this.isLogined==false){
      this.$router.push({name:'Login'})
    }
  }
}
</script>

<style>
  #detail{
    font-family: 'Gowun Batang', serif;
  }
</style>
<template>
  <div>
    <the-genre-search-list-item v-for="(movie,index) in selectedMovieList.slice().reverse()"
    :key="index"
    :movie-item="movie"></the-genre-search-list-item>
  </div>
</template>

<script>
import TheGenreSearchListItem from '@/components/genresearch/TheGenreSearchListItem'
import {mapState,mapGetters} from 'vuex'

export default {
  name:'TheGenreSearchList',
  data: function() {
    return {
      movies:[],
    }
  },
  components:{
    TheGenreSearchListItem,
  },
  methods:{

  },
  computed:{
    ...mapGetters([
      'selectedMovieList',
    ]),
    ...mapState([
      'selectedGenre','userMovies',
    ]),
  },


}
</script>

<style>

</style>
<template>
  <div class="row">
    <the-movie-list-item class="col-12 col-md-3" v-for="(movie,index) in movieList"
    :key="index"
    :movie-item="movie"
    ></the-movie-list-item>
  </div>
</template>

<script>
import TheMovieListItem from '@/components/admin/TheMovieListItem.vue'
import { mapState } from 'vuex'
export default {
  name: 'TheMovieList',
  mehods: {
  },
  components:{
    TheMovieListItem,
  },
  computed :{
    ...mapState([
      'movieList',
    ])
  }
}
</script>

<style>

</style>
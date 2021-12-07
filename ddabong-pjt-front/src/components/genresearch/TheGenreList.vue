<template>
  <b-dropdown id="inputtext" text="장르 선택">
    <the-genre-list-item  v-for="(genre,index) in genres"
    :key="index"
    :genre-item="genre"
    ></the-genre-list-item>
  </b-dropdown>
</template>

<script>
import TheGenreListItem from '@/components/genresearch/TheGenreListItem'
import axios from 'axios'
import {mapState} from 'vuex'

export default {
  name: 'TheGenreList',
  data: function () {
    return {
      genres: null,
    }
  },
  methods: {
    getGenres: function () {
      axios({
        method: 'get',
        url: 'https://jwsh.link/communities/genres_list/'
      })
        .then(res => {
          // console.log(res)
          this.genres = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    // onGenreSelected: function(genreItem){
    //   this.genre = genreItem
    // }
  },
  computed:{
    ...mapState([
      'selectedGenre',
    ]),
  },
  components:{
    TheGenreListItem,
  },
  created: function() {
    this.getGenres()
  }
}
</script>

<style>

</style>
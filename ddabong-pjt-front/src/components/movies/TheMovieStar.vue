<template>
  <div>
    <div id="seconddetail" class="my-3">
      <h2>평균 평점</h2>
    </div>
    <star-rating class="justify-content-center" id=setstar :increment="0.1" :star-size="30" :show-rating="false" v-model="rating" :border-width="5" border-color="#d8d8d8" :rounded-corners="true" :read-only="true" ></star-rating>
    <the-movie-star-form
    :movie-num="Number(movieNum)" 
    @aver-star="averChange"></the-movie-star-form>
  </div>
</template>

<script>
import TheMovieStarForm from '@/components/movies/TheMovieStarForm'
import StarRating from 'vue-star-rating'
export default {
  name:'TheMovieStar',
  data: function() {
    return {
      rating:null,
    }
  },
  props:{
    movieNum:Number,
  },
  methods:{
    averChange: function(value) {
      // console.log(value)
      this.rating=value
    },
  },
  components: {
    TheMovieStarForm,
    StarRating
  }
}
</script>

<style>

</style>
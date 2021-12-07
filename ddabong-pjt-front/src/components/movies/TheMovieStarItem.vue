<template>
  <div>
    <star-rating :increment="0.5" :star-size="30" :show-rating="false" v-model="reviewItem.stars" :border-width="5" border-color="#d8d8d8" :rounded-corners="true" :read-only="true" :inline="true" ></star-rating>
    <span id="seconddetail">{{reviewItem.user.username}}: {{reviewItem.content}}</span>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
export default {
  name: 'TheMovieStarItem',
  props:{
    reviewItem:Object,
  },
  components:{
    StarRating,
  }
  
}
</script>

<style>

</style>
<template>
  <div class="d-flex flex-row flex-wrap">
    <div class="card col-12 col-md-3 px-1 my-2" v-for="(random, index) in randomItem" :key="index">        
      <img class="card-img-top" :src="image(random.poster_path)" alt="">
      <div class="card-text">
        <p>{{random.title}}</p>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name:'TheFolloingsMovie',
  data: function(){
    return {
      randomItem:Object
    }
  },
  props:{
    movieItem:{
      type:Array,
    }
  },
  methods: {
    image(img) {
      return `http://image.tmdb.org/t/p/w300/${img}`
    },
  },
  created:function(){
    this.randomItem = _.sampleSize(this.movieItem,5)
  }
}
</script>

<style>

</style>
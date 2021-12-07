<template>
  <div >
    <p id="thirddetail" @click="onGenreClick">{{genreItem.name}}</p>
  </div>
</template>

<script>
// import Velocity from 'velocity-animate'
// import axios from 'axios'
export default {
  name:'TheGenreListItem',
  data: function() {
    return{
    }
  },
  props:{
    genreItem: {
      type: Object
    }
  },
  methods: {
    onGenreClick: function(){
      this.$store.dispatch('genreBoardSelected',this.genreItem)
    },
  }

}
</script>

<style>

</style>
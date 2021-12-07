<template>
    <!-- <p>{{movieItem.genres}}</p> -->
    <div @click="moveDetail" class="offset-1 col-10">
      <ol class="list-group">
        <li class="list-group-item">{{movieItem.title}}</li>
      </ol>
    </div>

</template>

<script>
// import Velocity from 'velocity-animate'
// import axios from 'axios'
export default {
  name:'TheGenreSearchListItem',
  data: function() {
    return{
    }
  },
  props:{
    movieItem: {
      type: Object
    }
  },
  methods: {
    moveDetail: function() {
      this.$router.push({name: 'MovieDetail', params:{movieNum:this.movieItem.id}})
    }
  }

}
</script>

<style>

</style>
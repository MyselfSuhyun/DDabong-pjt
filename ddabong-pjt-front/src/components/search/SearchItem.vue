<template>
  <div>
    <div class="card" @click="goToDetail">
      <img class="card-image-top" :src="image(movieItem.poster_path)" alt="image">
      <div id="cardtext" class="card-body">
        <p>{{ movieItem.title }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchItem',
  props:{
    movieItem:Object
  },
  methods: {
    image (img) {
      return `http://image.tmdb.org/t/p/w300/${img}`
    },
    goToDetail: function() {
      this.$router.push({name: 'MovieDetail', params:{movieNum:this.movieItem.id}})
    }

  }

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@600&family=Jua&family=Song+Myung&display=swap');

#cardtext {
  font-family: 'IBM Plex Sans KR', sans-serif;
  /* font-family: 'Jua', sans-serif; */
  /* font-family: 'Song Myung', serif; */
}

</style>
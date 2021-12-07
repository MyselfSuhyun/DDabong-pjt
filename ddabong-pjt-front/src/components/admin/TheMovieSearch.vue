<template>
  <div class="col-12 col-lg-5">
    <div class="input-group">
      <input class="form-control" placeholder="영화 제목을 입력하세요." type="text" @keyup.enter="enterKeyword" v-model="keyword">
      <button class="btn btn-secondary" @click="enterKeyword">입력</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TheMovieSearch',
  data : function () {
    return {
      keyword: null,
    }
  },
  methods: {
    enterKeyword : function() {
      this.$store.dispatch('changeKeyword',this.keyword)
      this.keyword=null
    }
  }

}
</script>

<style>

</style>
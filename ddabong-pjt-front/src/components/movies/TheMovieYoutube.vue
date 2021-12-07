<template>
  <div>
    <div v-if="detailYoutube">
      <iframe :src="videoURI(detailYoutube)" width="640" height="360" frameborder="0"></iframe>
    </div>
    <p id="thirddetail" v-show="detailYoutube==false">관련 영상을 찾을 수 없습니다.</p>
  </div>
</template>

<script>
import axios from 'axios'
import {mapActions, mapState} from 'vuex'
export default {
  name:'TheMovieYoutube',
  deta:function(){
    return {
      movie:Object,
    }
  },
  props:{
    tmdbId:Number,
  },
  methods:{
    videoURI : function(uri){
      return `https://www.youtube.com/embed/${uri}`
    },
    ...mapActions([
      'detailYoutubeList',
    ]),
    getMovie: function(){
      axios({
        methods: 'GET',
        url: `https://jwsh.link/movies/list/${this.$route.params.movieNum}`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`}
      })
        .then(res=> {
          // console.log(res)
          this.detailYoutubeList(res.data.tmdb_id)
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  computed:{
    ...mapState([
      'detailYoutube',
    ])
  },
  created: function(){
    this.getMovie()
  },
}
</script>

<style>

</style>
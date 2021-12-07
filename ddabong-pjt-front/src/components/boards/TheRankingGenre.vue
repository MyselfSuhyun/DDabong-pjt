<template>
  <div>
    <br>
    <div id="seconddetail" class="my-5">
      <p>여러분이 가장 좋아하는 장르의 영화는?</p>
    </div>
    <GChart class="container"
    :settings="{packages:['corechart']}"
    type="PieChart"
    :data="chartData"
    :options="chartOptions"
    />
  </div>
</template>


<script>
import { GChart } from 'vue-google-charts'
import axios from 'axios'
export default {
  name:'TheRankingGenre',
  data: function(){
    return {
      chartData: [],
      chartOptions: {
        chart: {
          width: 100,
          height: 100
        },
        backgroundColor: {
            'fill': 'rgb(75, 75, 75)',
            'opacity': 100
        },
      }
    }
  },
  methods:{
  },
  mounted: function() {
    axios({
      method: 'get',
      url: 'https://jwsh.link/movies/rankinggr/',
      headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`}
    })
      .then(res => {
        this.chartData=res.data
        console.log(this.chartData)
      })
      .catch(err => {
        console.log(err)
      })
  },
  components: {
    GChart
  }

}
</script>

<style>

</style>
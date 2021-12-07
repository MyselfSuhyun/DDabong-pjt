<template>
  <tr @click="moveDetail">
    <td id="seconddetail">{{boardItem.id}}</td>
    <td id="seconddetail"><a href="#" style="text-decoration:none; color:black;">{{boardItem.title}}</a></td>
    <td id="seconddetail">{{boardItem.user.nickname}}</td>
    <td id="seconddetail">{{boardItem.hits}}</td>
  </tr>
</template>

<script>
// import Velocity from 'velocity-animate'
// import axios from 'axios'
export default {
  name:'TheBoardListItem',
  data: function() {
    return{
    }
  },
  props:{
    boardItem: {
      type: Object
    }
  },
  methods: {
    moveDetail: function() {
      this.$router.push({name:"BoardDetail",params:{boardNum:this.boardItem.id}})
    },
  }

}
</script>

<style>

</style>
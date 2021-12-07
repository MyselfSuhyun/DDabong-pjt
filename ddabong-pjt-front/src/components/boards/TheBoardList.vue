<template>
  <div >

    <div id="boardtable">
      <div>
        <div style="display: flex; justify-content;flex-end;">
          <button class="btn btn-primary my-2" @click="moveCreate">글 작성</button>
        </div>
        <table class="table table-secondary table-hover">
          <thead>
            <tr>
              <th scope="col">글번호</th>
              <th scope="col">제목</th>
              <th scope="col">글작성자</th>
              <th scope="col">조회수</th>
            </tr>
          </thead>
          <tbody>
            <the-board-list-item  v-for="(board,index) in selectedBoardList.slice().reverse()"
            :key="index"
            :board-item="board"
            ></the-board-list-item>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import TheBoardListItem from '@/components/boards/TheBoardListItem'
import {mapState,mapGetters} from 'vuex'
export default {
  name: 'TheBoardList',
  data: function () {
    return { 
    }
  },
  methods: {
    getBoards: function(){
      this.$store.dispatch('getBoards')
    },
    moveCreate: function() {
      this.$router.push({name:'BoardCreate'})
    }
  },
  computed:{
    ...mapGetters([
      'selectedBoardList',
    ]),
    ...mapState([
      'userBoards','selectedGenreBoard',
    ]),
  },
  components:{
    TheBoardListItem,
  },
  created: function() {
    this.getBoards()
  }
}
</script>

<style>

</style>
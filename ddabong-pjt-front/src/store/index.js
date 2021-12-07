import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
const API_KEY = '4775dca612e07fb742a5fcdc1532178e'
const API_URL = 'https://api.themoviedb.org/3/search/movie'

import _ from 'lodash'
export default new Vuex.Store({
  state: {
    keyword: null,
    movieList: [],
    selectedGenre: { "id": 0, "name": "전체" },
    selectedGenreBoard: { "id": 0, "name": "전체" },
    userMovies: [],
    userBoards: [],
    isAdmined: false,
    currentuser: null,
    isLogined: false,
    searchedMovies: [],
    searchedUsers: [],
    rankingPage: 1,
    moviePage: 1,
    detailYoutube: null,
  },
  mutations: {
    CHANGE_KEYWORD : function(state,keyword){
      state.keyword = keyword
    },
    GENRE_SELECTED : function(state,genre){
      state.selectedGenre = genre
    },
    GENRE_BOARD_SELECTED : function(state,genre){
      state.selectedGenreBoard = genre
    },
    UPDATE_MOVIE_LIST : function(state,movieSearchList){
      state.movieList = movieSearchList
    },
    GET_MOVIES: function(state,movies){
      state.userMovies = movies
    },
    GET_BOARDS: function(state, boards){
      state.userBoards = boards
    },
    ADMIN_VALID: function(state, value){
      state.isAdmined = value
    },
    CURRENT_USER: function(state,value){
      state.currentuser = value
    },
    LOGOUT_VALID: function(state){
      state.isAdmined = false
      state.currentuser = false
    },
    USER_SEARCH: function(state,data){
      state.searchedUsers = data
    },
    MOVIE_SEARCH: function(state,data){
      state.searchedMovies = data
    },
    ACTIVE_LOGINED: function(state){
      state.isLogined = true
    },
    DEACTIVE_LOGINED: function(state){
      state.isLogined = false
    },
    PAGE_RANKING: function(state,page){
      state.rankingPage= page
    },
    PAGE_MOVIE: function(state,page){
      state.moviePage=page
    },
    DETAIL_YOUTUBE: function(state,data){
      if(data==="a"){
        state.detailYoutube = null
      }else{
        state.detailYoutube = data
      }
    }
  },
  actions: {
    genreSelected : function({commit},genre){
      
      commit('GENRE_SELECTED',genre)
    },
    genreBoardSelected : function({commit},genre){
      
      commit('GENRE_BOARD_SELECTED',genre)
    },
    changeKeyword : function({commit},keyword){
      commit('CHANGE_KEYWORD',keyword)
    },
    updateMovieList: function({commit}){
      const params = {
        api_key: API_KEY,
        language : 'ko-KR',
        query: this.state.keyword
      }
      axios({
        method : 'GET',
        url : API_URL,
        params,
      })
      .then(response=>{
        // console.log(response.data.results.length)
        var i
        let id_list = []
        for(i=0;i<response.data.results.length;i++){
          // console.log(response.data.results[i].id)
          id_list.push(response.data.results[i].id)
        }
        // console.log(id_list)
        let movie_search_list = []
        for ( i of id_list){
          // console.log(i)
          axios({
            method : 'GET',
            url : `https://api.themoviedb.org/3/movie/${i}`,
            params,
          })
          .then(response=>{
            // console.log(response.data)
            movie_search_list.push(response.data)
          })
        }
      // console.log(movie_search_list)
       commit('UPDATE_MOVIE_LIST',movie_search_list)
      })
    },
    detailYoutubeList: function({commit},tmdb_id){
      const params = {
        api_key: API_KEY,
        language : 'ko-KR',
      }
      axios({
        method : 'GET',
        url : `https://api.themoviedb.org/3/movie/${tmdb_id}/videos?`,
        params,
      })
      .then(response=>{
        const len = response.data.results.length
        if (!len){
          const params = {
            api_key: API_KEY,
          }
          axios({
            method : 'GET',
            url : `https://api.themoviedb.org/3/movie/${tmdb_id}/videos?`,
            params,
          })
          .then(response=>{
            const len2 = response.data.results.length
            if(!len2){
              commit('DETAIL_YOUTUBE',"a")
            }
            let result2 = []
            for (let i = 0; i<len2; i++){
              result2.push(response.data.results[i].key)
            }
            const data = _.sampleSize(result2,1)
            commit('DETAIL_YOUTUBE',data)
          })
        }
        let result = []
        for (let i = 0; i<len; i++){
          result.push(response.data.results[i].key)
        }
        const data = _.sampleSize(result,1)
        commit('DETAIL_YOUTUBE',data)
      })
    },
    getMovies: function () {
      axios({
        method: 'get',
        url: 'https://jwsh.link/movies/list/'
      })
        .then(res => {
          // console.log(res)
          this.commit('GET_MOVIES',res.data) 
        })
        .catch(err => {
          console.log(err)
        })
    },
    getBoards: function (context) {
      axios({
        method: 'get',
        url: 'https://jwsh.link/communities/',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
      })
        .then(res => {
          // console.log(res.data)
          context.commit('GET_BOARDS', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    adminValid: function ({commit}) {
      axios({
        method: 'get',
        url: 'https://jwsh.link/accounts/',
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`}
      })
        .then(res => {
          commit('ADMIN_VALID',res.data.isAdmined)
          commit('CURRENT_USER',res.data.currentUser)
        })
        .catch(err => {
          console.log(err)
        })
    },
    logoutValid: function({commit}){
      commit('LOGOUT_VALID')
    },
    userSearch: function({commit},data){
      commit('USER_SEARCH',data)
    },
    movieSearch: function({commit},data){
      commit('MOVIE_SEARCH',data)
    },
    activeLogined: function({commit}){
      commit('ACTIVE_LOGINED')
    },
    deActiveLogined: function({commit}){
      commit('DEACTIVE_LOGINED')
    },
    pageRanking:function({commit},page){
      commit('PAGE_RANKING',page)
    },
    pageMovie:function({commit},page){
      commit('PAGE_MOVIE',page)
    },
  },
  getters: {
    selectedMovieList: function(state){
      // console.log(!state.selectedGenre)
      if (state.selectedGenre.id!=0){
        return state.userMovies.filter(movie =>{
          const arr = movie.genres
          return arr.indexOf(state.selectedGenre.id)!==-1
        })
      }else {
        return state.userMovies
        }
      },
    selectedBoardList: function(state){
      // console.log(!state.selectedGenreBoard)

      if (state.selectedGenreBoard.id !=0){
        return state.userBoards.filter(board =>{
          return board.genre==state.selectedGenreBoard.id
        })
      }else {
        return state.userBoards
        }
      }
    },
  modules: {
  }
})

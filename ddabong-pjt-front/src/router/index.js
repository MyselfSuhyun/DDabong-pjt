import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Profile from '@/views/accounts/Profile'
import Home from '../views/Home.vue'
import Movie from '../views/admin/Movie.vue'
import MovieList from '@/views/admin/MovieList'
import GenreSearch from '@/views/genresearch/GenreSearch'
import Keywords from '@/views/keywords/Keywords'
import Boards from '@/views/boards/Boards.vue'
import BoardCreate from '@/views/boards/BoardCreate.vue'
import BoardDetail from '@/views/boards/BoardDetail.vue'
import BoardUpdate from '@/views/boards/BoardUpdate.vue'
import Search from '@/views/search/Search.vue'
import MovieDetail from '@/views/movies/MovieDetail.vue'
import TheFollowings from '@/views/accounts/TheFollowings'
import TheFollowers from '@/views/accounts/TheFollowers'
import UserSearch from '@/views/accounts/UserSearch'
import RankingBoard from '@/views/boards/RankingBoard'

Vue.use(VueRouter)

const routes = [
  // 유저 검색 게시판
  { 
    path: '/profile/search',
    name: 'UserSearch',
    component: UserSearch,
  },
  {
    path: '/movie/:movieNum',
    name: 'MovieDetail',
    component: MovieDetail,
  },
  {
    path: '/search',
    name: 'Search',
    component: Search,
  },
  // accounts
  // 1. 회원가입
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  // 2. 로그인
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  // 3. 프로필 페이지
  {
    path: '/profile/:userName',
    name: 'Profile',
    component: Profile,
  },
  // 4. 팔로잉 목록
  {
    path: '/profile/:userName/followings',
    name: 'TheFollowings',
    component: TheFollowings
  },
  // 5. 팔로워 목록
  {
    path: '/profile/:userName/followers',
    name: 'TheFollowers',
    component: TheFollowers
  },
  // 6. 게시판 목록
  {
    path: '/boards/',
    name: 'Boards',
    component: Boards,
  },
  // 7. 게시판 글 작성
  {
    path: '/boards/create/',
    name: 'BoardCreate',
    component: BoardCreate,
  },
  // 8. 게시판 글 상세 정보
  {
    path: '/boards/:boardNum',
    name: 'BoardDetail',
    component: BoardDetail,
  },
  // 9. 게시판 글 수정
  {
    path: '/boards/:boardNum/update',
    name: 'BoardUpdate',
    component: BoardUpdate,
  },
  // 10. 랭킹 게시판
  {
    path: '/ranking',
    name: 'RankingBoard',
    component: RankingBoard
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/movie',
    name: 'Movie',
    component: Movie
  },
  {
    path: '/movies',
    name: 'MovieList',
    component: MovieList,
  },
  // 장르 검색 게시판
  { 
    path: '/genresearch',
    name: 'GenreSearch',
    component: GenreSearch,
  },
  {
    path: '/keywords',
    name: 'Keywords',
    component: Keywords,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

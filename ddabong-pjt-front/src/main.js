import Vue from 'vue'
import App from './App.vue'
// Vue profile 설치
import VueProfile from "vue-profile"
// vue router 등록
import router from './router'
// veux 틍록
import store from './store'
// 부트스트랩을 위한 import 와 CDN
// npm i vue bootstrap-vue bootstrap
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueLuxon from "vue-luxon"


Vue.use(VueLuxon, {
  input: {
      zone: "utc",
      format: "iso"
  },
  output: "short"
});

import VueGoogleCharts from 'vue-google-charts'
 
Vue.use(VueGoogleCharts)

Vue.use(VueProfile, 'vue-profile')
Vue.use(BootstrapVue)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

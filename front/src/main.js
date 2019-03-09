import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import Vuetify from 'vuetify/dist/vuetify.min.css'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false
Vue.use(Vuetify)
Vue.use(VueAxios, axios)

new Vue({
  render: h => h(App),
}).$mount('#app')

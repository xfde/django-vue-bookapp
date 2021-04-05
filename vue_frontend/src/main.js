//import {createAppInEl, createSharedStore} from "@/util/create_app_utils";
import App from './App.vue'
import {createApp} from 'vue'
import store from "@/vuex/vuex_module_counter"
import router from './router'
import 'element-plus/lib/theme-chalk/index.css'
import { VueCookieNext } from 'vue-cookie-next'
import Toaster from '@meforma/vue-toaster';

createApp(App).use(VueCookieNext).use(store).use(Toaster).use(router).mount("#app");

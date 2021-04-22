import Vuex from 'vuex';
import Vue from 'vue';
import user from './modules/user';
import marketing from './modules/marketing';
import analytics from './modules/analytics';
import core from './modules/core';
//Load vuex
Vue.use(Vuex);

//Create store
export default new Vuex.Store({
    modules: {
        user,
        marketing,
        analytics,
        core
    }
});
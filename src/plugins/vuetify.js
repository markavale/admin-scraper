import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import 'vuetify/dist/vuetify.min.css'


Vue.use(Vuetify);

const opts = {}

export default new Vuetify({
    opts,
    icons: {
        iconfont: 'md', // 'mdi' || 'mdiSvg' || 'md' || 'fa' || 'fa4' || 'faSvg'
    },
    // theme: {
    //     themes: {
    //         dark: {
    //             primary: '#15314b',
    //             secondary: '#15314b',
    //             anchor: '#15314b',
    //         },
    //     },
    // },
});
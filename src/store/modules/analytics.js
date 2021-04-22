import { axiosBase } from "@/api/axiosConfig";


const state = {
    pageViews: {}
}

const getters = {

}

const actions = {
    pageViewsIncrement: (context, payload) => {
        return new Promise((resolve, reject) => {
            axiosBase
                .post('api/page-views/', payload)
                .then(res => {
                    resolve(true);
                    context.commit('incrementViews', res.data);
                })
                .catch(err => reject(err));
        })
    }
}
const mutations = {
    incrementViews: (state, views) => state.pageViews.unshift(views),
}


export default {
    state,
    getters,
    actions,
    mutations,
}
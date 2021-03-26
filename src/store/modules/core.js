import { axiosBase } from "@/api/axiosConfig";
// import index from '@/store/index';
// import router from "@/router";
// import axios from 'axios';
const state = {
  crawlerSets: [],
  scrapers: [],
  scraperAnalysis: {}
};

const getters = {
  getScrapers: (state) => state.scrapers,
  getCrawlerSets: (state) => state.crawlerSets,
  getScraperAnalysis: (state) => state.scraperAnalysis,
};

const actions = {
  // fetching crawler set objects
  fetchCrawlerSets: ({ commit }) => {
    return new Promise((resolve, reject) => {
      axiosBase
        .get("api/crawler-sets/", {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${localStorage.getItem("token")}`,
          },
        })
        .then(res => {
            console.log(res.data.results);
            commit("setCrawlerSets", res.data.results);
            resolve(true)
        })
        .catch(err => reject(err));
    });
  },
  // fecthing scraper objects
  fetchScrapers: ({ commit }) => {
    return new Promise((resolve, reject) => {
      axiosBase
        .get("api/scrapers/", {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            Authorization: `Token ${localStorage.getItem("token")}`,
          },
        })
        .then((res) => {
          console.log(res.data.results);
          commit("setScrapers", res.data.results);
          resolve(true);
        })
        .catch((err) => {
          // router.push("/login");
          reject(err);
        });
    });
  },

  // Fetching scraper analysis
  fetchScraperAnalysis: ({commit}) => {
    return new Promise((resolve, reject) => {
      axiosBase
      .get("api/scraper-analysis/", {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      })
      .then(res => {
        console.log(res.data)
        commit("setScraperAnalysis", res.data)
        resolve(true)
      })
      .catch(err => reject(err));
    })
  }
};

const mutations = {
  setCrawlerSets: (state, payload) => (state.crawlerSets = payload),
  setScrapers: (state, payload) => (state.scrapers = payload),
  setScraperAnalysis: (state, payload) => (state.scraperAnalysis = payload),
};

export default {
  state,
  getters,
  actions,
  mutations,
};

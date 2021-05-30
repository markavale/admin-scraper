import { axiosBase } from "@/api/axiosConfig";
// import { resolve } from "core-js/fn/promise";
// import index from '@/store/index';
// import router from "@/router";
// import axios from 'axios';
const state = {
  crawlerSets: [],
  scrapers: [],
  scraperAnalysis: {},
  scraperDates: {},
  reportInstance: {},
  articleErrors: [],
  websiteDownloadLatency: [],
};

const getters = {
  getReportInstance: (state) => state.reportInstance,
  getScraperDates: (state) => state.scraperDates,
  getScrapers: (state) => state.scrapers,
  getCrawlerSets: (state) => state.crawlerSets,
  getScraperAnalysis: (state) => state.scraperAnalysis,

  getArticleErrors: (state) => state.articleErrors,
  getWebsiteDownloadLatency: (state) => state.websiteDownloadLatency,

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
        .get("api/scrapers/?ordering=-timestamp", {
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
  },

  // fetching scraper by dates
  fetchScraperByDates: ({commit}) => {
    return new Promise((resolve, reject) => {
      axiosBase
      .get("api/dashboard/", {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      })
      .then(res => {
        console.log(res.data)
        commit("setScraperDates", res.data)
        resolve(true)
      })
      .catch(err => reject(err));
    })
  },

  // get  report instance
  reportInstance: (context, payload) => {
    return new Promise((resolve, reject) => {
      axiosBase
      .get(`api/scrapers/${payload}/`, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      })
      .then(res => {
        context.commit('setReportInstance', res.data)
        console.log(res.data)
        resolve(true)
      })
      .catch(err=>reject(err))
    })
  },

  websiteErrorReports: (context) => {
    return new Promise((resolve, reject) => {
      axiosBase
      .get('api/article-errors/', {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      })
      .then(res => {
        console.log(res.data.results)
        context.commit('setWebsiteErrorReports', res.data.results)
        resolve(true)
      })
      .catch(err=>reject(err))
    })
  },

  // website download latency
  websiteDownloadLatency: (context) => {
    return new Promise((resolve, reject) => {
      axiosBase
      .get('api/website-latency/', {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      })
      .then(res => {
        console.log(res.data.results)
        context.commit("setWebsiteDownloadLatency", res.data.results)
        resolve(true)
      })
      .catch(err=>reject(err))
    })
  },




};

const mutations = {
  setScraperDates: (state, payload) => (state.scraperDates = payload),
  setCrawlerSets: (state, payload) => (state.crawlerSets = payload),
  setScrapers: (state, payload) => (state.scrapers = payload),
  setScraperAnalysis: (state, payload) => (state.scraperAnalysis = payload),
  setReportInstance: (state, payload) => (state.reportInstance = payload),
  // article errors 
  setWebsiteErrorReports: (state, payload) => (state.articleErrors = payload),

  // website download latency
  setWebsiteDownloadLatency: (state, payload) => (state.websiteDownloadLatency = payload),
};

export default {
  state,
  getters,
  actions,
  mutations,
};

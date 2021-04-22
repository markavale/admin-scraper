import { axiosBase } from "@/api/axiosConfig";
// import index from '@/store/index';
import router from "@/router";
// import axios from 'axios';
const state = {
    users: [],
    isPopUp: localStorage.getItem("isPopUp") || null,
    user: {},
    token: localStorage.getItem("token") || null,
};

const getters = {
    getUsers: (state) => state.users,
    isAuthenticated(state) {
        return state.token != null;
        // return localStorage.getItem('token') != null
    },
    getAccessToken: (state) => state.token,
    requestUser: (state) => state.user,
};

const actions = {
    fetchUsers: ({ commit }) => {
        return new Promise((resolve, reject) => {
            axiosBase
                .get("auth/user/", {
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded",
                        Authorization: `Token ${localStorage.getItem("token")}`,
                    },
                })
                .then((res) => {
                    console.log(res.data);
                    commit("setUsers", res.data);
                    resolve(true);
                })
                .catch((err) => {
                    router.push("/login");
                    reject(err);
                });
        });
    },
    fetchCurrentUser: (context) => {
        return new Promise((resolve, reject) => {
            axiosBase
                .get("auth/user/", {
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded",
                        Authorization: `Token ${localStorage.getItem("token")}`,
                    },
                })
                .then((res) => {
                    console.log(res.data);
                    console.log(res.data.username);
                    context.commit("currentUser", res.data);
                    resolve(true);
                })
                .catch((err) => reject(err));
        });
    },
    Login: (context, credentials) => {
        return new Promise((resolve, reject) => {
            axiosBase
                .post("auth/login-user/", {
                    username: credentials.username,
                    password: credentials.password
                })
                .then((res) => {
                    console.log(res.data.key);
                    context.commit("setToken", res.data.key);
                    resolve(true);
                    // return new Promise((resolve, reject) => {
                    //     axiosBase
                    //         .post("auth/user/", {
                    //             headers: {
                    //                 "Content-Type": "application/x-www-form-urlencoded",
                    //                 Authorization: `Token ${localStorage.getItem("token")}`,
                    //             },
                    //         })
                    //         .then((res) => {
                    //             console.log("after login");
                    //             console.log(res.data);
                    //             console.log(res.data.username);
                    //             context.commit("currentUser", res.data);
                    //             resolve(true);
                    //         })
                    //         .catch((err) => reject(err));
                    // });
                })
                .catch((error) => {
                    reject(error);
                    console.log("error!!!");
                    context.commit("destroyToken");
                });
        });
    },
    Logout: (context) => {
        return new Promise((resolve, reject) => {
            axiosBase
                .post("auth/logout/")
                .then(() => {
                    localStorage.removeItem("token");
                    context.commit("destroyToken");
                    router.push({ name: "login" });
                    resolve(true);
                })
                .catch((err) => {
                    reject(err);
                });
        });
    },
    Register: (context, data) => {
        return new Promise((resolve, reject) => {
            axiosBase
                .post("auth/registration/", {
                    username: data.username,
                    email: data.email,
                    password1: data.password1,
                    password2: data.password2,
                    // note!!! Pleaseeee don't add comma(,) at the end of data fields or else you will get an error!!!!
                })
                .then((res) => {
                    resolve(true);
                    console.log(data);
                    console.log(res.data);
                    context.commit("newUser", res.data);
                })
                .catch((err) => {
                    context.commit("destroyToken");
                    reject(err);
                });
        });
    },
    // setDevHoursModal() {
    //     if (localStorage) {
    //         let nextPopup = localStorage.getItem('isPopUp') || null

    //         if (nextPopup > new Date()) {
    //             return this.show = true;
    //         }

    //         let expires = new Date()
    //         expires = expires.setHours(expires.getHours() + 24)

    //         localStorage.setItem('isPopUp', expires)
    //     }
    // }
};

const mutations = {
    setUsers: (state, users) => (state.users = users),
    newUser: (state, newUser) => state.users.unshift(newUser),
    setToken: (state, token) => {
        localStorage.setItem("token", token);
        state.token = token;
    },
    destroyToken: (state) => {
        state.token = null;
        state.user = null;
    },
    currentUser: (state, user) => (state.user = user),
};

export default {
    state,
    getters,
    actions,
    mutations,
};
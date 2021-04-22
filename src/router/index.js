import Vue from "vue";
import VueRouter from "vue-router";
// import Home from "../views/Home.vue";
import Sidebar from "@/components/Sidebar";
import Login from "@/views/auth/Login";
import Register from "@/views/auth/Register";
import Logout from "@/components/auth/Logout";
import Dashboard from "@/views/Dashboard";

Vue.use(VueRouter);

const routes = [
  // {
  //     path: '/',
  //     name: 'home',
  //     component: Home,
  //     meta: {
  //         requiresAuth: false,
  //         title: 'Mark Anthony Vale'
  //     }
  // },
  {
    path: "/",
    name: "sidebar",
    component: Sidebar,
    meta: {
      requiresAuth: false,
      title: "Admin",
    },
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: Dashboard,
    meta: {
      requiresAuth: true,
      title: "MMI ADMIN SCRAPER",
    },
  },
  // reports
  {
    path: "/reports",
    name: "reports",
    component: () =>
      import(/* webpackChunkName: "reports" */ "../views/table/Reports.vue"),
    meta: {
      requiresAuth: true,
      title: "Scraping Reports",
    },
  },
  {
    path: "/reports/:id",
    name: "report-instance",
    component: () =>
      import(
        /* webpackChunkName: "report-instance" */ "../views/table/ReportInstance.vue"
      ),
    meta: {
      requiresAuth: true,
      title: "Report Instance",
    },
  },
  // Webiste error reports 
  {
    path: "/website-errors",
    name: "website-errors",
    component: () =>
      import(/* webpackChunkName: "website-errors" */ "../views/table/website_errors/WebsiteErrors.vue"),
    meta: {
      requiresAuth: true,
      title: "Website Error Reports",
    },
  },

  // Webiste downlaod latency reports
  {
    path: "/download-latency-reports",
    name: "download-latency-reports",
    component: () =>
      import(/* webpackChunkName: "download-latency-reports" */ "../views/table/download_reports/DownloadLatencyReports.vue"),
    meta: {
      requiresAuth: true,
      title: "Article Download Latency Reports",
    },
  },

  // views
  {
    path: "/test-view",
    name: "test",
    component: () =>
      import(/* webpackChunkName: "test" */ "../views/Test.vue"),
    meta: {
      requiresAuth: true,
      title: "Test",
    },
  },

  // views
  {
    path: "/daily-timeline",
    name: "timelines",
    component: () =>
      import(/* webpackChunkName: "timelines" */ "../views/timelines/DailyTimeline.vue"),
    meta: {
      requiresAuth: true,
      title: "Daily Timeline",
    },
  },

  {
    path: "/about",
    name: "about",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
    meta: {
      requiresAuth: true,
      title: "About Me",
    },
  },
  {
    path: "/login",
    name: "login",
    component: Login,
    meta: {
      requiresLogged: true,
      title: "Login",
    },
  },
  {
    path: "/sign-up",
    name: "sign-up",
    component: Register,
    meta: {
      requiresLogged: true,
      title: "Sign Up",
    },
  },
  {
    path: "/logout",
    name: "logout",
    component: Logout,
    meta: {
      requiresAuth: true,
      title: "Logout",
    },
  },
  {
    path: "/mav/auth/password/reset/confirm/:uid/:token/",
    name: "password-confirm",
    component: () =>
      import(
        /* webpackChunkName: "password-confirm" */ "@/views/auth/PasswordConfirm.vue"
      ),
    meta: {
      requiresLogged: true,
      title: "Passoword Confirm",
    },
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
  // authRoutes,
  // todo_routes
});

export default router;

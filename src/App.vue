<template>
  <!-- <v-app>
    <v-main>
      <router-view />
    </v-main>
    <v-btn
      v-scroll="onScroll"
      v-show="fab"
      fab
      dark
      fixed
      bottom
      right
      color="primary"
      @click="toTop"
    >
      <v-icon>keyboard_arrow_up</v-icon>
    </v-btn>
    <Loading :isLoading="loading" />
  </v-app> -->
  <v-app>
    <Sidebar>
      <!-- <v-main>
      <router-view />
    </v-main> -->
    </Sidebar>
    <v-btn
      v-scroll="onScroll"
      v-show="fab"
      fab
      dark
      fixed
      bottom
      right
      color="primary"
      @click="toTop"
    >
      <v-icon>keyboard_arrow_up</v-icon>
    </v-btn>
  </v-app>
</template>

<script>
import "cxlt-vue2-toastr/dist/css/cxlt-vue2-toastr.css";
import Sidebar from "@/components/Sidebar";
// import { axiosBase } from "@/api/axiosConfig";
// import Loading from "@/components/index/Loading";

export default {
  name: "App",
  components: {
    Sidebar,
    // Loading,
  },
  mounted() {
    this.pageVisits();
    // this.showLoading();
  },

  data: () => ({
    fab: false,
    counter: 1,
    errors: [],
    loading: false,
  }),
  methods: {
    showLoading() {
      this.loading = true;
      setTimeout(() => {
        this.loading = false;
      }, 3500);
    },
    pageVisits() {
      //
      this.$store
        .dispatch("pageViewsIncrement", {
          counter: this.counter,
        })
        .then(() => console.log("Inceremented!!!"))
        .catch((err) => {
          console.log(err);
          let error_data = err.response.data;
          console.log(error_data);
        });
    },
    onScroll(e) {
      if (typeof window === "undefined") return;
      const top = window.pageYOffset || e.target.scrollTop || 0;
      this.fab = top > 20;
    },
    toTop() {
      this.$vuetify.goTo(0);
    },
  },
};
</script>


<style lang="scss">
#app {
  font-family: "Montserrat", sans-serif; //Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #181818;
  // text-align: center;
  // color: #2c3e50;
}
#nav {
  // padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
.theme--dark.v-application {
  background-color: #181818;
}
.theme--dark.v-card,
.theme--dark.v-data-table,
.theme--dark.v-tabs-items,
.theme--dark.v-tabs .v-tabs-bar {
  background-color: #232323;
}
.fade-enter-active,
.fade-leave-active {
  transition-property: opacity;
  transition-duration: 0.25s;
}
.fade-enter-active {
  transition-delay: 0.25s;
}
.fade-enter,
.fade-leave-active {
  opacity: 0;
}
::-webkit-scrollbar {
  width: 8px;
  background-color: #111;
}
::-webkit-scrollbar-thumb {
  background-color: #222;
}
::-webkit-scrollbar-thumb:hover {
  background-color: #444;
}
::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.6);
  background-color: #333;
}
::-webkit-scrollbar-track:hover {
  background-color: #292929;
}
// html {
//   scroll-behavior: smooth;
//   box-sizing: border-box;
// }
// #app {
//   font-family: "Montserrat";
//   background-color: #f5f5f5;
// }
// .lead {
//   font-size: 20px;
//   font-weight: 500;
//   color: #15314b;
//   // color:#2c3e50;
// }
// .line-mf {
//   width: 40px;
//   height: 5px;
//   background-color: #0078ff;
//   margin: 0 auto 15px auto;
// }
// .container_box {
//   padding: 3rem 2rem;
//   background-color: #fff;
//   margin: 50px 0;
//   box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.2);
// }
// .black-overlay {
//   background-color: rgba(0, 0, 0, 0.6);
//   position: absolute;
//   top: 0;
//   left: 0px;
//   padding: 0;
//   height: 100vh;
//   width: 100%;
//   opacity: 0.9;
// }
</style>

<template>
  <div id="nav">
    <nav
      :class="[is_transparent ? 'navbar-trans' : 'navbar-reduce']"
      class="navbar navbar-b navbar-expand-md fixed-top"
      id="mainNav"
      v-on:scroll.prevent="onScroll"
    >
    
      <div class="container">
        <a class="navbar-brand js-scroll" href="/"
          ><img src="@/assets/img/logo.png" alt="Logo" class="logo" />
          MAV
        </a>
        <button
          class="navbar-toggler collapsed"
          type="button"
          data-toggle="collapse"
          data-target="#navbarDefault"
          aria-controls="navbarDefault"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span></span>
          <span></span>
          <span></span>
        </button>
        <div
          class="navbar-collapse collapse justify-content-end"
          id="navbarDefault"
        >
          <ul class="navbar-nav">
            <!-- <li class="nav-item">
              <a class="nav-link js-scroll" href="#about">About</a>
            </li>
            <li class="nav-item">
              <a class="nav-link js-scroll" href="#services">Services</a>
            </li>
            <li class="nav-item">
              <a class="nav-link js-scroll" href="#portfolio">Portfolio</a>
            </li> -->
            <li class="nav-item">
              <a class="nav-link js-scroll" href="#">Welcome, {{ user.username }}</a>
            </li>
            <li class="nav-item" v-if="!isAuthenticated">
            <router-link :to="{ name: 'login' }" class="nav-link"
              >Login</router-link
            >
          </li>
            <li class="nav-item" v-if="isAuthenticated">
            <router-link :to="{ name: 'logout' }" class="nav-link"
              >Logout</router-link
            >
          </li>
          </ul>
        </div>
      </div>
    </nav>
    <!-- <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">Navbar w/ text</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarText"
        aria-controls="navbarText"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <router-link :to="{ name: 'home' }" class="nav-link"
              >Home</router-link
            >
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'about' }" class="nav-link"
              >About</router-link
            >
          </li>
        </ul>
        <ul class="navbar-nav">
          <li class="nav-item" v-if="isAuthenticated">
            <span class="nav-link" v-if="currentUser != null"
              >Welcome, <b>{{ currentUser.username }}</b></span
            >
          </li>
          <li class="nav-item" v-if="!isAuthenticated">
            <router-link :to="{ name: 'login' }" class="nav-link"
              >Login</router-link
            >
          </li>
          <li class="nav-item" v-if="!isAuthenticated">
            <router-link :to="{ name: 'sign-up' }" class="nav-link"
              >Sign up</router-link
            >
          </li>
          <li class="nav-item" v-if="isAuthenticated">
            <router-link :to="{ name: 'logout' }" class="nav-link"
              >Logout</router-link
            >
          </li>
        </ul>
      </div>
    </nav> -->
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import { axiosBase } from "@/api/axiosConfig";
export default {
  data() {
    return {
      drawer: false,
      group: null,
      user: {},
      is_transparent: true,
    };
  },
  computed: {
    ...mapGetters(["isAuthenticated"]),
    currentUser() {
      if (this.isAuthenticated) {
        const crrUser = this.$store.state.user.user;
        return crrUser;
      } else {
        const temp_user = {
          username: "None",
        };
        return temp_user;
      }
    },
  },
  mounted() {
    window.addEventListener("scroll", this.onScroll);
    this.getCurrentUser();
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.onScroll);
  },
  created() {
    this.getCurrentUser();
  },
  methods: {
    onScroll(e) {
      this.is_transparent = !(e.target.documentElement.scrollTop > 0);
      // if(!this.is_transparent){

      // }
    },
    getCurrentUser() {
      if (this.isAuthenticated) {
        axiosBase
          .get("auth/user/", {
            headers: {
              "Content-Type": "application/x-www-form-urlencoded",
              Authorization: `Token ${localStorage.getItem("token")}`,
            },
          })
          .then((res) => {
            this.$store.commit("currentUser", res.data);
            this.user = this.$store.state.user.user;
            console.log("User")
          })
          .catch((err) => console.log(err));
      }
    },
  },
};
</script>
<style scoped>
/* logo */
.logo {
  height: 90px;
  width: 90px;
  margin: 0 0 0 5px;
  padding: 0;
  -webkit-transition: -webkit-transform 1s;
}
.logo:hover {
  -webkit-transform: rotate(360deg) translateZ(0);
}

/*======================================
//--//-->   NAVBAR
======================================*/
nav {
  height: 100px;
}

.navbar-b {
  transition: all 0.5s ease-in-out;
  background-color: transparent;
  padding-top: 1.563rem;
  padding-bottom: 1.563rem;
}

.navbar-b.navbar-reduce {
  transition: all 0.5s ease-in-out;
  box-shadow: 0px 6px 9px 0px rgba(0, 0, 0, 0.06);
  height: auto;
  background-color:#fff;
  width:100%;
}

.navbar-b .nav-item,
.navbar-b.navbar-reduce .nav-item {
  position: relative;
  padding-right: 10px;
  padding-left: 0;
}

.navbar-b .nav-link,
.navbar-b.navbar-reduce .nav-link {
  color: #fff;
  text-transform: uppercase;
  font-weight: 600;
  line-height: 1.6;
  font-size: 17px;
}

.navbar-b .nav-link:before,
.navbar-b.navbar-reduce .nav-link:before {
  content: "";
  position: absolute;
  margin-left: 0px;
  width: 0%;
  bottom: 0;
  left: 0;
  height: 2px;
  transition: all 500ms ease;
}

.navbar-b .nav-link:hover,
.navbar-b.navbar-reduce .nav-link:hover {
  color: #1b1b1b;
}

.navbar-b .nav-link:hover:before,
.navbar-b.navbar-reduce .nav-link:hover:before {
  width: 35px;
}

.navbar-b .show > .nav-link:before,
.navbar-b .active > .nav-link:before,
.navbar-b .nav-link.show:before,
.navbar-b .nav-link.active:before,
.navbar-b.navbar-reduce .show > .nav-link:before,
.navbar-b.navbar-reduce .active > .nav-link:before,
.navbar-b.navbar-reduce .nav-link.show:before,
.navbar-b.navbar-reduce .nav-link.active:before {
  width: 35px;
}

.navbar-b .nav-link:before {
  background-color: #fff;
}

.navbar-b .nav-link:hover {
  color: #fff;
}

.navbar-b .show > .nav-link,
.navbar-b .active > .nav-link,
.navbar-b .nav-link.show,
.navbar-b .nav-link.active {
  color: #fff;
}

.navbar-b.navbar-reduce {
  transition: all 0.5s ease-in-out;
  background-color: #fff;
  /* padding-top: 15px; */
  /* padding-bottom: 15px; */
}

.navbar-b.navbar-reduce .nav-link {
  color: #0078ff;
}

.navbar-b.navbar-reduce .nav-link:before {
  background-color: #0078ff;
}

.navbar-b.navbar-reduce .nav-link:hover {
  color: #0078ff;
}

.navbar-b.navbar-reduce .show > .nav-link,
.navbar-b.navbar-reduce .active > .nav-link,
.navbar-b.navbar-reduce .nav-link.show,
.navbar-b.navbar-reduce .nav-link.active {
  color: #0078ff;
}

.navbar-b.navbar-reduce .navbar-brand {
  color: #0078ff;
}

.navbar-b.navbar-reduce .navbar-toggler span {
  background-color: #1b1b1b;
}

.navbar-b .navbar-brand {
  color: #fff;
  font-size: 1.6rem;
  font-weight: 600;
}

.navbar-b .navbar-nav .dropdown-item.show .dropdown-menu,
.navbar-b .dropdown.show .dropdown-menu,
.navbar-b .dropdown-btn.show .dropdown-menu {
  -webkit-transform: translate3d(0px, 0px, 0px);
  transform: translate3d(0px, 0px, 0px);
  visibility: visible !important;
}

.navbar-b .dropdown-menu {
  margin: 1.12rem 0 0;
  border-radius: 0;
}

.navbar-b .dropdown-menu .dropdown-item {
  padding: 0.7rem 1.7rem;
  transition: all 500ms ease;
}

.navbar-b .dropdown-menu .dropdown-item:hover {
  background-color: #0078ff;
  color: #fff;
  transition: all 500ms ease;
}

.navbar-b .dropdown-menu .dropdown-item.active {
  background-color: #0078ff;
}

/*--/ Hamburger Navbar /--*/

.navbar-toggler {
  position: relative;
}

.navbar-toggler:focus,
.navbar-toggler:active {
  outline: 0;
}

.navbar-toggler span {
  display: block;
  background-color: #fff;
  height: 3px;
  width: 25px;
  margin-top: 4px;
  margin-bottom: 4px;
  -webkit-transform: rotate(0deg);
  transform: rotate(0deg);
  left: 0;
  opacity: 1;
}

.navbar-toggler span:nth-child(1),
.navbar-toggler span:nth-child(3) {
  transition: -webkit-transform 0.35s ease-in-out;
  transition: transform 0.35s ease-in-out;
  transition: transform 0.35s ease-in-out, -webkit-transform 0.35s ease-in-out;
}

.navbar-toggler:not(.collapsed) span:nth-child(1) {
  position: absolute;
  left: 12px;
  top: 10px;
  -webkit-transform: rotate(135deg);
  transform: rotate(135deg);
  opacity: 0.9;
}

.navbar-toggler:not(.collapsed) span:nth-child(2) {
  height: 12px;
  visibility: hidden;
  background-color: transparent;
  /* background-color:#fff; */
}

.navbar-toggler:not(.collapsed) span:nth-child(3) {
  position: absolute;
  left: 12px;
  top: 10px;
  -webkit-transform: rotate(-135deg);
  transform: rotate(-135deg);
  opacity: 0.9;
}

@media (min-width: 768px) {
  .navbar-collapse {
    height: auto;
    /* background-color:#fff; */
    background-color: transparent;
    padding: 8px 0 8px 10px;
  }
  /* .collapse{
    height: auto;
    background-color: #fff;
    width:100%;
  } */
  .navbar {
    height: 70px;
    margin: 0;
    padding: 0 15px;
  }
  .navbar-brand {
    margin: 0;
    padding: 0;
  }
  .box-shadow-full {
    padding: 3rem;
  }

  .navbar-b .nav-item,
  .navbar-b.navbar-reduce .nav-item {
    /* padding-left: 10px; */
  }

  .navbar-b .nav-link:before,
  .navbar-b.navbar-reduce .nav-link:before {
    /* margin-left: 18px; */
  }
}
@media (min-width: 375px) {
  .logo {
    height: 50px;
    width: 50px;
  }
  .navbar-collapse {
    height: auto;
    background-color:transparent;
    /* background-color: #fff; */
    padding: 8px 0 8px 10px;
  }
  /* .collapse{
    height: auto;
    background-color: #fff;
    width:100%;
  } */
  .navbar {
    height: 70px;
    width:100%;
    margin: 0;
    padding: 0 15px;
  }
  .navbar-brand {
    margin: 0;
    padding: 0;
  }
}
</style>
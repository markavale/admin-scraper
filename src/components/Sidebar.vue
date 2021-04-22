<template>
  <!-- <v-container> -->
  <!-- <v-row justify="space-around">
      <v-col cols="12">
        <v-select
          v-model="color"
          :items="colors"
          label="Color"
        ></v-select>
      </v-col>
      <v-switch
        v-model="drawer"
        class="ma-2"
        label="v-model"
      ></v-switch>
      <v-switch
        v-model="permanent"
        class="ma-2"
        label="Permanent"
      ></v-switch>
      <v-switch
        v-model="miniVariant"
        class="ma-2"
        label="Mini variant"
      ></v-switch>
      <v-switch
        v-model="expandOnHover"
        class="ma-2"
        label="Expand on hover"
      ></v-switch>
      <v-switch
        v-model="background"
        class="ma-2"
        label="Background"
      ></v-switch>
      <v-switch
        v-model="right"
        class="ma-2"
        label="Right"
      ></v-switch>
    </v-row> -->
  <div>
    <!-- <v-card height="100vh" class="overflow-hidden"> -->
    <v-app-bar app color="grey darken-4" dark>
      <v-app-bar-nav-icon
        @click.stop="sidebarMenu = !sidebarMenu"
      ></v-app-bar-nav-icon>
      <v-toolbar-title>MMI ADMIN SCRAPER</v-toolbar-title>
      <v-spacer></v-spacer>

      <v-menu offset-y dark outline v-if="isAuthenticated">
        <template v-slot:activator="{ on }">
          <v-btn dark icon v-on="on">
            <v-icon>mdi-account</v-icon>
          </v-btn>
        </template>
        <v-card class="mx-auto" elevation="11" max-width="300" tile>
          <v-list shaped>
            <v-subheader>Hello, {{ user.username }}</v-subheader>
            <v-divider></v-divider>
            <v-list-item-group v-model="item" color="primary">
              <v-list-item
                v-for="(item, i) in userDetails"
                :key="i"
                :to="item.href"
              >
                <v-list-item-icon>
                  <v-icon v-text="item.icon"></v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title v-text="item.text"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-menu>
    </v-app-bar>
    <v-navigation-drawer
      v-model="sidebarMenu"
      app
      floating
      :permanent="sidebarMenu"
      :mini-variant.sync="miniVariant"
      color="grey darken-4"
    >
      <v-list dense>
        <v-list-item>
          <v-list-item-action>
            <v-icon @click.stop="sidebarMenu = !sidebarMenu" dark
              >mdi-chevron-left</v-icon
            >
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-list-item class="px-2" @click="miniVariant = !miniVariant" dark>
        <v-list-item-avatar>
          <v-icon>mdi-account-outline</v-icon>
        </v-list-item-avatar>
        <v-list-item-content class="text-truncate">
          Mark Anthony Vale
        </v-list-item-content>
        <v-btn icon small>
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
      </v-list-item>
      <v-divider color="white"></v-divider>
      <!-- <v-list shaped>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
          :to="item.href"
          active-class="primary--text"
        >
          <v-list-item-icon>
            <v-icon color="primary">{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title class="primary--text">{{
              item.title
            }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list> -->

      <v-list shaped>
        <v-list-item
          v-for="item in items_3"
          :key="item.id"
          active-class="primary--text"
          :to="item.href"
        >
          <v-list-item-icon>
            <v-icon color="primary">{{ item.action }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title
              v-text="item.title"
              class="primary--text"
            ></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-group
          v-for="item in items_2"
          :key="item.title"
          v-model="item.active"
          no-action
          active-class="primary--text"
        >
          <template v-slot:activator>
            <v-list-item-icon>
              <v-icon color="primary">{{ item.action }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title
                v-text="item.title"
                class="primary--text"
              ></v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="child in item.items"
            :key="child.title"
            :to="child.href"
            class="text-decoration-none"
          >
            <v-list-item-content>
              <v-list-item-title
                v-text="child.title"
                class="primary--text text-caption"
              ></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-group>
      </v-list>
    </v-navigation-drawer>
    <!-- <v-content> -->
    <v-main>
      <v-container class="px-4 py-0 fill-height" fluid>
        <v-row class="fill-height">
          <v-col>
            <transition name="fade">
              <router-view />
            </transition>
          </v-col>
        </v-row>
      </v-container>
      <v-footer app color="grey darken-4" class="py-3" dark>
        <span class="ml-auto overline">MMI &copy;2021</span>
      </v-footer>
    </v-main>
    <!-- </v-content> -->

    <!-- <Navbar /> -->
    <!-- </v-card> -->
  </div>

  <!-- </v-container> -->
</template>

<script>
// import Navbar from "@/components/Navbar";
import { mapGetters } from "vuex";
import { axiosBase } from "@/api/axiosConfig";
export default {
  data() {
    return {
      user: {},
      drawer: true,
      items: [
        {
          title: "Dashboard",
          icon: "mdi-view-dashboard",
          href: { name: "dashboard" },
        },
        { title: "Reports", icon: "mdi-table", href: { name: "reports" } },
        { title: "Test View", icon: "mdi-help-box", href: { name: "test" } },
      ],
      items_3: [
        {
          action: "mdi-view-dashboard",
          title: "Dashboard",
          href: { name: "dashboard" },
        },
        {
          action: "mdi-help-box",
          title: "Test View",
          href: { name: "test" },
        },
      ],
      items_2: [
        {
          action: "mdi-spider-web",
          active: true,
          items: [
            { title: "Dashboard Reports", href: { name: "reports" } },
            { title: "Error Reports" , href: { name: "website-errors" } },
            { title: "Download Latency Reports", href: { name: "download-latency-reports" } },
          ],
          title: "Website",
          href: null,
        },
      ],

      color: "primary",
      colors: ["primary", "blue", "success", "red", "teal"],
      right: false,
      sidebarMenu: true,
      miniVariant: false,
      expandOnHover: false,
      background: false,
      item: 1,
      userDetails: [
        { text: "Profile", icon: "mdi-account" },
        { text: "Change Password", icon: "mdi-lock" },
        { text: "Logout", icon: "mdi-logout", href: { name: "logout" } },
      ],
    };
  },
  components: {
    // Navbar,
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
    bg() {
      return this.background
        ? "https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg"
        : undefined;
    },
  },
  mounted() {
    this.getCurrentUser();
    console.log("Navbar Component Mounted");
  },
  methods: {
    getCurrentUser() {
      console.log(this.$store.state.user.user);
      if (this.isAuthenticated) {
        axiosBase
          .get("auth/user/", {
            headers: {
              "Content-Type": "application/x-www-form-urlencoded",
              Authorization: `Token ${localStorage.getItem("token")}`,
            },
          })
          .then((res) => {
            // this.user = res.data;
            this.$store.commit("currentUser", res.data);
            this.user = this.$store.state.user.user;
          })
          .catch((err) => console.log(err));
      }
    },
  },
};
</script>
<style>
</style>

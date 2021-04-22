<template>
  <div>
    <!-- <Navbar /> -->
    <v-container class="mt-10">
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md6>
          <v-card class="elevation-12" :disabled="loading" tile>
            <v-progress-linear
              :active="loading"
              :indeterminate="loading"
              height="5"
            ></v-progress-linear>      
            <v-toolbar dark color="blue">
              <v-toolbar-title> Login Form </v-toolbar-title>
              
            </v-toolbar>
            
            <v-card-text>
              <v-form>
                <v-alert :value="error" color="error" icon="warning" dark>
                  <b>Please correct the following error(s):</b>
                  <ul>
                    <li
                      v-for="error in errors"
                      :key="error.id"
                      class="text-md-left"
                    >
                      {{ error }}
                    </li>
                  </ul>
                </v-alert>
                <v-text-field
                  v-model="username"
                  prepend-icon="person"
                  name="username"
                  label="Username"
                  type="text"
                >
                </v-text-field>
                <!-- <v-text-field
                    v-model="email"
                    prepend-icon="email"
                    name="email"
                    label="Email"
                    type="email"
                    >
                    </v-text-field> -->
                <v-text-field
                  v-model="password"
                  prepend-icon="lock"
                  name="password"
                  label="Password"
                  @keyup.enter="login"
                  :append-icon="value ? 'mdi-eye' : 'mdi-eye-off'"
                  @click:append="() => (value = !value)"
                  :type="value ? 'password' : 'text'"
                >
                </v-text-field>
                <v-card-actions>
                  <router-link to="/sign-up" class="nav-link">
                    <v-btn rounded color="indigo" dark> Sign up </v-btn>
                  </router-link>
                  <v-spacer></v-spacer>
                  <v-btn rounded color="primary" @click.prevent="login"
                    >Login
                    <v-icon> keyboard_arrow_right </v-icon>
                  </v-btn>
                </v-card-actions>
                <v-divider> </v-divider>
                <PasswordReset />
              </v-form>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
// import Navbar from "@/components/Navbar";
import PasswordReset from "@/components/auth/PasswordReset";
export default {
  name: "Login",
  components: {
    // Navbar,
    PasswordReset,
  },
  data() {
    return {
      username: "",
      email: "",
      password: "",
      error: false,
      errorMessage: "",
      value: true,
      loading: false,
      errors: [],
    };
  },
  methods: {
    login() {
      this.loading = true;
      this.$store
        .dispatch("Login", {
          username: this.username,
          password: this.password,
        })
        .then(() => {
          console.log(this.$store.getters.isAuthenticated);
          this.loading = false;
          this.$router.push({ name: "home" });
        })
        .catch((err) => {
          this.errors = [];
          console.log(err);
          console.log(err.response.data);
          this.errorMessage = err.response.data;
          this.error = true;
          let error_data = err.response.data;
          console.log(error_data);
          for (const field_error in error_data) {
            this.errors.push(error_data[field_error]);
          }
          this.$store.commit("destroyToken");
          this.loading = false;
        });
    },
  },
};
</script>

<style>
</style>
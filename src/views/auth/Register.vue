<template>
  <div>
    <!-- <Navbar /> -->
    <v-container  fill-height class="mt-10">
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md6>
          <v-card class="elivation-12" :disabled="loading">
            <v-progress-linear
            :active="loading"
            :indeterminate="loading"
            height="5"
          ></v-progress-linear>
            <v-toolbar dark color="blue">
              <v-toolbar-title>Sign Up Form</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <v-form ref="form">
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
                  :rules="[rules.required, rules.username]"
                >
                </v-text-field>
                <v-text-field
                  v-model="email"
                  prepend-icon="email"
                  name="email"
                  label="Email"
                  :rules="[rules.required, rules.email]"
                  type="email"
                >
                </v-text-field>
                <v-text-field
                  prepend-icon="lock"
                  name="password"
                  label="Password"
                  :rules="[passwordErrors1]"
                  v-model="password1"
                  :error="!valid()"
                  :append-icon="passShow ? 'mdi-eye' : 'mdi-eye-off'"
                  @click:append="() => (passShow = !passShow)"
                  :type="passShow ? 'password' : 'text'"
                >
                </v-text-field>
                <v-text-field
                  prepend-icon="lock"
                  name="password"
                  label="Confirm Password"
                  :rules="[passwordErrors2]"
                  v-model="password2"
                  :error="!valid()"
                  @keyup.enter="RegisterUser"
                  :append-icon="passShow ? 'mdi-eye' : 'mdi-eye-off'"
                  @click:append="() => (passShow = !passShow)"
                  :type="passShow ? 'password' : 'text'"
                >
                </v-text-field>
              </v-form>
            </v-card-text>
            <v-divider light></v-divider>
            <v-card-actions>
              <router-link to="/login" class="nav-link">
                <v-btn rounded color="black" dark>Sign In</v-btn>
              </router-link>
              <v-spacer></v-spacer>
              <v-btn rounded color="success" @click.prevent="RegisterUser"
                >Register
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>

      <v-row justify="center">
        <v-dialog v-model="dialog" persistent max-width="400">
          <v-card>
            <v-card-title class="headline"> Email Verification </v-card-title>
            <v-card-text class="text-left"
              ><p class="subtitle-2">
                We have sent an email to <b>{{ email_verification }}</b
                >. Please verify your account.
              </p></v-card-text
            >
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="secondary" text @click="closeDialog">
                Close
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>

      <!-- <div class="text-start"> -->
      <v-snackbar v-model="snackbar" :timeout="2500" left>
        Redirecting to login page..
        <template v-slot:action="{ attrs }">
          <v-btn color="blue" text v-bind="attrs" @click="snackbar = false">
            Close
          </v-btn>
        </template>
      </v-snackbar>
      <!-- </div> -->
    </v-container>
  </div>
</template>

<script>
// import Navbar from "@/components/Navbar";

export default {
  name: "SignUp",
  components: {
    // Navbar,
  },
  data: () => ({
    errors: [],
    loading: false,
    snackbar: false,
    username: "",
    email: "",
    password1: "",
    password2: "",
    passShow: true,
    dialog: false,
    email_verification: "",
    rules: {
      required: (value) => !!value || "Required",
      username: (value) => {
        const pattern = /^([a-za-z0-9\u0600-\u06FF\u0660-\u0669\u06F0-\u06F9 _.-]+)$/;
        // const pattern = /^[a-za-z0-9]+$/
        return (
          pattern.test(value) ||
          "Username must be alphanumeric or contain numbers and lowercaps."
        );
      },
      email: (value) => {
        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return pattern.test(value) || "Invalid e-mail.";
      },
    },
    error: false,
  }),
  computed: {
    passwordErrors1() {
      if (this.password1 === "") return "Password is required";
      if (this.password1 !== this.password2) {
        return "Password don't match. Please try again.";
      }
      return true;
    },
    passwordErrors2() {
      if (this.password2 === "") return "Password confirmation is required";
      if (this.password1 !== this.password2) {
        return "Password don't match. Please try again.";
      }
      return true;
    },
  },
  created() {},
  methods: {
    closeDialog() {
      this.dialog = false;
      this.snackbar = true;
      setTimeout(() => {
        this.$router.push({ name: "login" });
      }, 3000);
    },
    RegisterUser() {
      this.errors = [];
      this.loading = true;
      this.$store
        .dispatch("Register", {
          username: this.username,
          email: this.email,
          password1: this.password1,
          password2: this.password2,
          // dont add comma (,) at the last of fields
        })
        .then((res) => {
          console.log(res.data);
          this.email_verification = this.email;
          this.loading = false;
          this.dialog = true;
          (this.username = ""),
            (this.email = ""),
            (this.password1 = ""),
            (this.password2 = "");
          this.$refs.form.reset()
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
          let error_data = err.response.data;
          console.log(error_data);
          for (const field_error in error_data) {
            this.errors.push(error_data[field_error][0]);
          }
          this.error = true;
        });
    },
    valid() {
      return this.password1 === this.password2;
    },
  },
};
</script>

<style>
</style>
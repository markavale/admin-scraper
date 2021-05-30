<template>
  <div>
    <Navbar />
    <v-container>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md6>
          <v-card class="elevation-12" :disabled="loading" tile>
            <v-progress-linear
              :active="loading"
              :indeterminate="loading"
              height="5"
            ></v-progress-linear>
            <v-toolbar dark color="blue">
              <v-toolbar-title>Password Reset Form</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <v-form v-model="valid">
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
                  v-model="password1"
                  autocomplete="current-password"
                  :value="password1"
                  prepend-icon="lock"
                  label="Password"
                  hint="Your password passed! Password rules are not meant to be broken!"
                  :append-icon="value ? 'mdi-eye' : 'mdi-eye-off'"
                  @click:append="() => (value = !value)"
                  :type="value ? 'password' : 'text'"
                  :rules="passwordErrors"
                ></v-text-field>

                <v-text-field
                  v-model="password2"
                  @keyup.enter="submitForm"
                  autocomplete="current-password"
                  :value="password2"
                  prepend-icon="lock"
                  label="Confirm Password"
                  hint="Your password passed! Password rules are not meant to be broken!"
                  :append-icon="value ? 'mdi-eye' : 'mdi-eye-off'"
                  @click:append="() => (value = !value)"
                  :type="value ? 'password' : 'text'"
                  :rules="nameErrors"
                ></v-text-field>
                <v-card-actions>
                  <v-btn
                    class="float-right"
                    @click.prevent="submitForm"
                    color="primary"
                    rounded
                    >Reset</v-btn
                  >
                </v-card-actions>
              </v-form>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
    <div class="text-center">
      <v-snackbar :left="true" v-model="snackbar" :timeout="3000">
        Redirecting to login page.
        <template v-slot:action="{ attrs }">
          <v-btn color="blue" text v-bind="attrs" @click="snackbar = false">
            Close
          </v-btn>
        </template>
      </v-snackbar>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import { validationMixin } from "vuelidate";
import { required, maxLength, email } from "vuelidate/lib/validators";
import { axiosBase } from "@/api/axiosConfig";

export default {
  name: "password-confirm",
  mixins: [validationMixin],

  validations: {
    password1: { required, maxLength: maxLength(24) },
    password2: { required, maxLength: maxLength(8) },
    email: { required, email },
    select: { required },
    checkbox: {
      checked(val) {
        return val;
      },
    },
  },
  data: () => ({
    password1: "",
    password2: "",
    snackbar: true,
    error: false,
    valid: true,
    value: true,
    errors: [],
    loading: false,
  }),
  components: {
    Navbar,
  },
  computed: {
    nameErrors() {
      const errors = [];
      if (!this.$v.password1.$dirty) return errors;
      !this.$v.password1.maxLength &&
        errors.push("Password must be at most 8 characters long");
      !this.$v.password1.required && errors.push("Password is required.");
      return errors;
    },
    passwordErrors() {
      const errors = [];
      if (!this.$v.password2.$dirty) return errors;
      if (this.password1 !== this.password2) {
        errors.push("Password don't match. Please try again.");
        return errors;
      }
      !this.$v.password2.required &&
        errors.push("Please Confirm your Password.");
      return errors;
    },
  },
  mounted() {
    // this.getAccessToken()
  },
  methods: {
    submitForm() {
      this.loading = true;
      const uid = this.$route.params.uid;
      const token = this.$route.params.token;
      this.$v.$touch();
      const data = {
        uid: uid,
        token: token,
        password1: this.password1,
        password2: this.password2,
      };
      console.log(data);
      axiosBase
        .post(`auth/password/reset/confirm/${data.uid}/${data.token}/`, {
          new_password1: data.password1,
          new_password2: data.password2,
          uid: data.uid,
          token: data.token,
        })
        .then((res) => {
          
          this.loading = false;
          this.error = false;
          console.log(res.data);
          this.$toast.success({
            title: "Password Reset",
            message: `An email has been reset successfully`,
            type: 'success',
            position: 'top right',
            icon: require('../../assets/icons/check-circle-white.png'),
            closeButton: true,
            timeOut: 3000,
            showDuration: 500,
            hideDuration: 500,
            showMethod: 'fadeIn',
            hideMethod: 'fadeOut',
            color: '#51A351',
          });
          setTimeout(()=>{
            this.snackbar = true
          }, 3500)
          setTimeout(() => {
            this.snackbar = false
            this.$router.push({ name: "login" });
          }, 4500);
        })
        .catch((error) => {
          this.loading = false;
          this.errors = [];
          this.error = true;
          if (error.response) {
            console.log("response");
            console.log(error.response.data);
            console.log(error.response.status);
            console.log(error.response.headers);
            let error_data = error.response.data;
            console.log(error_data);
            for (const field_error in error_data) {
              this.errors.push(error_data[field_error][0]);
            }
          } else if (error.request) {
            console.log("request");
            // The request was made but no response was received
            // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
            // http.ClientRequest in node.js
            console.log(error.request);
          } else {
            console.log("error occured");
            // Something happened in setting up the request that triggered an Error
            console.log("Error", error.message);
          }
          console.log(error.config);
        });
    },
    clear() {
      this.$v.$reset();
    },
  },
};
</script>

<style>
</style>
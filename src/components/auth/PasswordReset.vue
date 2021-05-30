<template>
  <div>
    <v-row justify="center">
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            v-bind="attrs"
            v-on="on"
            color="blue darken-1"
            text
            class="text-left"
            >Forgot password?</v-btn
          >
        </template>
        
        <v-card tile :disabled="loading">
          <v-progress-linear
            :active="loading"
            :indeterminate="loading"
            height="5"        
          ></v-progress-linear>
          <v-card-title>
            <span class="headline">Password Reset</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-alert :value="error" color="error" icon="warning" dark>
                        <b>Please correct the following error(s):</b>
                    <ul>
                      <li v-for="error in errors" :key="error.id"
                      class="text-md-left">{{ error }}</li>
                    </ul>
                    </v-alert>
              <v-form ref="form">
                <v-row>
                <v-col cols="12">
                  <v-text-field
                    prepend-icon="email"
                    v-model="email"
                    label="Email*"
                    type="email"
                    :rules="[rules.required, rules.email]"
                    required
                    @keypress.enter="sendVerification"
                  ></v-text-field>

                </v-col>
                <input type="text" style="display:none;"> <!--keyup.enter always reloads if only one input field wrapped in form -->
              </v-row>
              </v-form>
            </v-container>
            <small class="text-left" left>*indicates required field</small>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="dialog = false">
              Close
            </v-btn>
            <v-btn
              color="blue darken-1"
              text
              @click.prevent="sendVerification"
              :disabled="loading || email.length == 0"
              class="text-center"
            >
             Send
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
import { axiosBase } from "@/api/axiosConfig";
export default {
  name: "ForgatPasswordModal",
  data() {
    return {
      loading: false,
      dialog: false,
      error: false,
      email_reset: "",
      message: "",
      errorMessage: "An error uccured. Please try again.",
      email: "",
      errors: [],
      rules: {
        required: (value) => !!value || "Required",
        email: (value) => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || "Invalid e-mail.";
        },
      },
    };
  },
  methods: {
    closeDialog(){
      this.dialog=false
      this.$refs.form.reset()
    },
    sendVerification() {
      this.loading = true;
      axiosBase
        //.post("rest-auth/password/reset/", { email: this.email })
        .post("auth/password/reset/", { email: this.email })
        .then((res) => {
          console.log("email sent!!");
          console.log(res.data);
          this.email_reset = this.email
          this.email = "";
          this.dialog = false;
          this.error = false,
          this.message = res.data.detail;
          this.loading = false;
          this.$toast.success({
            title: "Password Reset",
            message: `An email has been sent to ${this.email_reset}`,
            type: 'success',
            position: 'top right',
            icon: require('../../assets/icons/check-circle-white.png'),
            closeButton: true,
            timeOut: 3500,
            showDuration: 500,
            hideDuration: 500,
            showMethod: 'fadeIn',
            hideMethod: 'fadeOut',
            color: '#51A351',
          });
        })
        .catch((error) => {
          this.errors = []
          this.error = true;
          console.log(error);
           let error_data = error.response.data
          console.log(error_data)
          for(const field_error in error_data){
            this.errors.push(error_data[field_error][0])
          }
          this.loading = false;
        });
      console.log("sendVerification");
      
      
    },
  },
};
</script>

<style scoped>
</style>
<template>
  <div>
    <!-- <div
    v-if="overlay"
      class="background_img_load"
      v-bind:style="{ backgroundImage: 'url(' + loadingImg + ')' }"
    > -->
    <transition name="fade">
      <div v-if="isLoading">
        <img
      class="background_img_load"
      src="@/assets/img/loading-web.jpg"
      alt="Loading-Img"
    />
    <img
      class="img_mobile"
      src="@/assets/img/loading-mobile.jpg"
      alt="Loading-Img"
    />
    <!-- <div class="overlay__loading" v-if="overlay"></div> -->
    <div class="text-center">
      <v-overlay :z-index="zIndex" :value="isLoading" :opacity="opacity">
        <!-- color="rgba(0, 0, 0, 0.6)" -->
        <!-- <v-progress-circular indeterminate size="64"></v-progress-circular> -->
        <v-card class="mx-auto pa-5" color="#304b64" dark max-width="400">
          <v-card-actions>
            <v-list-item class="">
              <v-row align="center" justify="center">
                <img
                  class="rotate__image"
                  src="@/assets/img/logo.png"
                  alt="Logo"
                />                
              </v-row>
              
            </v-list-item>
           
          </v-card-actions>
           <v-row align="center" justify="center">
                <v-chip
                  class="ma-2"
                  color="blue"
                  
                >
                  Loading...
                </v-chip>
              </v-row>
        </v-card>
      </v-overlay>
    </div>
      </div>
    </transition>

    <!-- </div> -->
    <!-- <v-btn
      color="deep-purple accent-4"
      class="white--text"
      @click="overlay = !overlay"
    >
      Launch Application
      <v-icon right> mdi-open-in-new </v-icon>
    </v-btn> -->
  </div>
</template>

<script>
export default {
  data: () => ({
    overlay: false,
    zIndex: 1500,
    opacity: 0,
  }),
  props:{
    isLoading:Boolean
  },
  // watch: {
  //   overlay(val) {
  //     val &&
  //       setTimeout(() => {
  //         this.overlay = false;
  //       }, 3500);
  //   },
  // },
};
</script>

<style>

.fade-enter-active, .fade-leave-active {
  opacity: 1;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  transition: opacity 0.8s;
  opacity: 0;
}
.background_img_load {
  position: fixed;
  z-index: 1400;
  height: 100vh;
  width: 100%;
  overflow-x: hidden;
  left: 0;
  top: 0;
}
.img_mobile{
  display:none;
  position: fixed;
  z-index: 1400;
  height: 100vh;
  width: 100%;
  overflow-x: hidden;
  left: 0;
  top: 0;
}
.rotate__image {
  height: 150px;
  width: 150px;
  animation: rotation 1s infinite linear;
}

@keyframes rotation {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(359deg);
  }
}
/* On screens that are 600px or less, set the background color to olive */
@media screen and (max-width: 600px) {
  .img_mobile{
    display:block;
    
  }
  .background_img_load{
    display: none;
  }
}
@media screen and (max-width: 992px) {
  .img_mobile{
    display:block;
  }
  .background_img_load{
    display:none;
  }
}
</style>
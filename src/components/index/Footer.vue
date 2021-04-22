<template>
  <v-footer dark padless>
    <v-card flat tile width="100%" color="#15314b" class="darken-4 white--text text-center">
      <v-card-text>
        <v-btn
          class="mx-4 white--text text-decoration-none"
          :href="icons.fbData.url"
          target="new"
          icon
        >
          <v-icon size="24px">
            {{ icons.fbData.icon }}
          </v-icon>
        </v-btn>
         <v-btn
          class="mx-4 white--text text-decoration-none"
          :href="icons.githubData.url"
          target="new"
          icon
        >
          <v-icon size="24px">
            {{ icons.githubData.icon }}
          </v-icon>
        </v-btn>
         <v-btn
          class="mx-4 white--text text-decoration-none"
          :href="icons.linkedinData.url"
          target="new"
          icon
        >
          <v-icon size="24px">
            {{ icons.linkedinData.icon }}
          </v-icon>
        </v-btn>
        <v-btn
          class="mx-4 white--text text-decoration-none"
          :href="icons.instagramData.url"
          target="new"
          icon
        >
          <v-icon size="24px">
            {{ icons.instagramData.icon }}
          </v-icon>
        </v-btn>
        <v-btn
          class="mx-4 white--text text-decoration-none"
          :href="icons.youtubeData.url"
          target="new"
          icon
        >
          <v-icon size="24px">
            {{ icons.youtubeData.icon }}
          </v-icon>
        </v-btn>
      </v-card-text>

      <v-card-text class="white--text pt-0">
        Hello! I'm Mark. Do you want me to build your desired website? <br> Let's Talk.
      </v-card-text>
      <v-card-text>
        <v-icon size="24px" class="">
            {{ icons.location }}
        </v-icon>
        Manila, Philippines
        <v-icon size="24px" class="">
            {{ icons.email }}
        </v-icon>
        markavale1@gmail.com
        <!-- <iframe width="30%" height="280px" src="https://www.youtube.com/embed/-ZC5YaFaLVw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> -->
      </v-card-text>

      <v-divider></v-divider>

      <v-card-text class="white--text">
        <img src="@/assets/img/logo.png" alt="" class="logo__footer" />
        {{ new Date().getFullYear() }} — <strong>Mark Anthony Vale</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  data: () => ({
    icons: {
      fbData: {
        icon: "mdi-facebook",
        url: "https://facebook.com/markavale",
      },
      githubData: {
        icon: "mdi-github",
        url: "https://github.com/markavale/",
      },
      linkedinData: {
        icon: "mdi-linkedin",
        url: "https://www.linkedin.com/in/mark-anthony-vale-b0b169199/",
      },
      instagramData: {
        icon: "mdi-instagram",
        url: "https://instagram.com/markavale_",
      },
      youtubeData: {
        icon: "mdi-youtube",
        url: "https://www.youtube.com/channel/UCxQaGymALC8CBJLJZ7UL34Q?view_as=subscriber",
      },
      location: "mdi-pin",
      email: 'mdi-email'
    },
  }),
};
</script>

<style>
.logo__footer {
  height: 40px;
  width: 40px;
}
</style>
<template>
  <div>
    
    <Navbar />
    <div
      id="home"
      class="img_parralax"
      v-bind:style="{ backgroundImage: 'url(' + backgroundUrl + ')' }"
    >
      <div class="home__text">
        <div class="container">
          <div class="home_contents">
            <h1 class="home_title_header">Hello, I'm Mark!</h1>
            <p class="home_title_subheader">
              <!-- <TextTyping :txtMessages="messages" /> -->
            </p>
          </div>
        </div>
      </div>
      <div class="black-overlay"></div>
    </div>
    <Footer />
  </div>
</template>

<script>
// import TextTyping from "@/components/index/TextTyping";
import Navbar from "@/components/Navbar";
import backgroundUrl from "@/assets/img/homepage.jpg";
import Footer from "@/components/index/Footer";

export default {
  name: "home",
  data() {
    return {
      backgroundUrl,
      messages: [
        "Hey! Thanks for visiting my website!",
        "I want to say something to you.......",
        ".......You are doing great!!!!!",
        "Keep your mind positive ✨",
        "I love playing guitar! 🎸......",
        "Do you love to travel?? If yes,",
        "then we're both travel lovers!!",
        "You can checkout my Youtube to see my travel videos!!",
        "Looks like you're enjoying staying here!!",
        "Thank you for your time visiting my website!",
        "Do you have any desired web application? If yes,",
        "feel free to contact me!!",
        "I'd love to work with you!!",
      ],
    };
  },
  components: {
    Navbar,
    // TextTyping,
    // AboutMe,
    // Services,
    // Porfolio,
    // Contact,
    Footer,
    // MessagePopUp,
  },
  mounted() {
  },
};
</script>

<style>
.img_parralax {
  height: 100vh;
  width: 100%;
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.img_parralax > .home__text {
  text-align: center;
}
.home_contents {
  margin: 200px 0 0 0;
  z-index: 1;
  position: relative;
}
.home_title_header {
  color: #fff;
  font-weight: 700;
  font-size: 3.5rem;
}
.home_title_subheader {
  font-size: 1.5rem;
  font-weight: 300;
  color: #fff;
}
.center {
  text-align: center;
}
@media screen and (max-width: 992px) {
  .home_title_header {
    font-weight: 700;
    font-size: 2.5rem;
  }
  .home_title_subheader {
    font-size: 1rem;
    font-weight: 300;
    color: #fff;
  }
}

/* On screens that are 600px or less, set the background color to olive */
@media screen and (max-width: 600px) {
  .home_contents {
    margin: 250px 0 0 0;
  }
  .home_title_header {
    font-weight: 700;
    font-size: 2rem;
  }
  .home_title_subheader {
    font-size: 1rem;
    font-weight: 300;
    color: #fff;
  }
}
</style>
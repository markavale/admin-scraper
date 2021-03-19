<template>
  <div>
    <v-row>
      <v-col lg="4" cols="sm" class="pb-2">
        <v-card dark color="#232323">
          <v-row class="no-gutters">
            <div class="col-auto">
              <div class="cyan fill-height">&nbsp;</div>
            </div>
            <div class="col pa-3 py-4 cyan--text">
              <h5 class="text-truncate text-uppercase">Total data</h5>
              <h1>
                <!-- {{ getPageViews.total_views }} -->
                5,180
              </h1>
            </div>
          </v-row>
        </v-card>
      </v-col>
      <v-col lg="4" cols="sm" class="pb-2">
        <v-card dark color="#232323">
          <v-row class="no-gutters">
            <div class="col-auto">
              <div class="primary fill-height">&nbsp;</div>
            </div>
            <div class="col pa-3 py-4 primary--text">
              <h5 class="text-truncate text-uppercase">Average Download latency</h5>
              <!-- <h1>{{ getRatings.rating_computed }}</h1> -->
              <h1>8.3</h1>
            </div>
          </v-row>
        </v-card>
      </v-col>
      <v-col lg="4" cols="sm" class="pb-2">
        <v-card dark color="#232323">
          <v-row class="no-gutters">
            <div class="col-auto">
              <div class="success fill-height">&nbsp;</div>
            </div>
            <div class="col pa-3 py-4 success--text">
              <h5 class="text-truncate text-uppercase">Success parsed data</h5>
              <h1>3,464</h1>
            </div>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
    <!-- <v-row>
      <v-col lg="4" cols="md" class="pb-2">
        <v-card class="dark" dark color="#232323">
          <v-card-title class="font-weight-light text-truncate cyan--text">
            Orders
          </v-card-title>
          <v-card-text>
            <v-carousel
              cycle
              height="180"
              interval="2000"
              hide-delimiter-background
              show-arrows-on-hover
            >
              <v-carousel-item>
                <div class="row no-gutters">
                  <div class="col">
                    <div>
                      <h2 class="cyan--text">Randy Sheets</h2>
                      <p class="mt-1">Tutankum, WI 33192</p>
                      <h3 class="mb-0">
                        $217.00
                        <i
                          class="mdi mdi-36px mdi-credit-card-outline float-right"
                        ></i>
                      </h3>
                      <p>Total items: 5</p>
                    </div>
                  </div>
                </div>
              </v-carousel-item>
              <v-carousel-item>
                <div class="row no-gutters">
                  <div class="col">
                    <div>
                      <h2 class="cyan--text">Jose Valdex</h2>
                      <p class="mt-1">Turnup, PA 23192</p>
                      <h3 class="mb-0">
                        $97.00
                        <i class="mdi mdi-36px mdi-paypal float-right"></i>
                      </h3>
                      <p>Total items: 2</p>
                    </div>
                  </div>
                </div>
              </v-carousel-item>
            </v-carousel>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col lg="4" cols="md" class="pb-2">
        <v-card min-height="252" dark color="#232323">
          <v-card-title class="font-weight-light text-truncate primary--text">
            Goals
          </v-card-title>
          <v-card-text>
            <p class="primary--text subtitle-1">Results from last campaign</p>
            <div class="my-5">
              <v-progress-linear
                indeterminate
                height="8"
                color="primary"
              ></v-progress-linear>
              <h6>SINCE JAN 2020</h6>
            </div>
          </v-card-text>
          <v-card-actions>
            <v-btn outlined rounded color="primary"> Details </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col lg="4" cols="md" class="pb-2">
        <v-card min-height="252" dark color="#232323">
          <v-card-title class="font-weight-light text-truncate success--text">
            On-boarding
          </v-card-title>
          <v-card-text>
            <span class="success--text subtitle-1"> Judy Pincus </span>
            <div class="mb-3">
              @jpincus
              <h3>Service Manager</h3>
              <span class="overline">Start date: 5/12/2020</span>
            </div>
          </v-card-text>
          <v-card-actions>
            <v-btn outlined rounded color="success"> View </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row> -->
    <v-row>
      <v-col>
        <v-card class="mx-auto text-center" dark color="#232323">
          <v-card-title class="primary--text">Parsed Data</v-card-title>
          <v-sparkline
            :value="sparklineData"
            :padding="padding"
            label-size="4"
            :gradient="gradient"
            :smooth="radius || false"
            :line-width="width"
            :stroke-linecap="lineCap"
            :gradient-direction="gradientDirection"
            :fill="fill"
            :type="type"
            :auto-line-width="autoLineWidth"
            auto-draw
            show-labels
          >
          <!-- :stroke-linecap="lineCap"
    :gradient-direction="gradientDirection" -->
            <!-- <template v-slot:label="item"> ${{ item.value }} </template> -->
            <template v-slot:label="item"> {{ item.value }} </template>
          </v-sparkline>
          <v-card-actions class="py-4 justify-center">
            <v-btn color="primary" to="/reports">View Report</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
// import { mapGetters } from "vuex";
const gradients = [
    ['#222'],
    ['#42b3f4'],
    ['red', 'orange', 'yellow'],
    ['purple', 'violet'],
    ['#00c6ff', '#F0F', '#FF0'],
    ['#f72047', '#ffd200', '#1feaea'],
    ['#007bff', 'cyan'],
    ['#01FFFF', '#00ECFA', '#00CEF1', '#00B8EA']
  ]
export default {
  name: "dashboard",
  data: () => ({
    // sparklineData: [423, 446, 675, 510, 590, 610, 423],
    sparklineData: [237, 262, 305, 356, 375, 392, 159, 408, 452, 518],
    width: 2,
    radius: 10,
    padding: 8,
    gradient: gradients[5],
    gradientDirection: 'top',
    gradients,
    fill: false,
    type: 'trend',
    autoLineWidth: false,
    lineCap: 'round',
  }),
  computed: {
    // ...mapGetters(["getPageViews", "getRatings"]),
  },
  mounted() {
    this.fetchPageViews();
    this.getRating();
    console.log("mounted");
  },
  methods: {
    fetchPageViews() {
      this.$store.dispatch("fetchPageViews");
      //   .then(() =>console.log("Success"))
      //   .catch(err => console.log(err))
    },
    getRating() {
      this.$store.dispatch("fetchRatings");
      //   .then()
      //   .catch()
    },
  },
};
</script>

<style>
</style>
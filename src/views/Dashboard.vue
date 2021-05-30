<template>
  <div>
    <div v-if="getScraperAnalysis">
      <v-row>
        <v-col lg="4" cols="sm" class="pb-2">
          <v-card dark color="#232323" style="border-left: 5px solid #4719d2 !important;">
            <v-row class="no-gutters">
              <div class="col pa-3 py-4" style="color: #4719d2" >
                <h5 class="text-truncate text-uppercase">Total data</h5>
                <h1>
                  {{ getScraperAnalysis.total_data }}
                </h1>
              </div>
            </v-row>
          </v-card>
        </v-col>
        <v-col lg="4" cols="sm" class="pb-2">
          <v-card dark color="#232323" style="border-left: 5px solid #a419d2 !important;">
            <v-row class="no-gutters">
              <div class="col-auto" style="color: #a419d2">
                <div class="fill-height">&nbsp;</div>
              </div>
              <div class="col pa-3 py-4" style="color: #a419d2">
                <h5 class="text-truncate text-uppercase">Total articles</h5>
                <!-- <h1>{{ getRatings.rating_computed }}</h1> -->
                <h1>{{ getScraperAnalysis.total_articles }}</h1>
              </div>
            </v-row>
          </v-card>
        </v-col>
        <v-col lg="4" cols="sm" class="pb-2">
          <v-card dark color="#232323" style="border-left: 5px solid #1975d2 !important;">
            <v-row class="no-gutters">
              <div class="col-auto" style="color: #1975d2">
                <div class="success fill-height">&nbsp;</div>
              </div>
              <div class="col pa-3 py-4" style="color: #1975d2">
                <h5 class="text-truncate text-uppercase">
                  Average Download latency
                </h5>
                <h1>{{ getScraperAnalysis.average_download_latency }}</h1>
              </div>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col lg="4" cols="sm" class="pb-2">
          <v-card dark color="#232323" class="" style="border-left: 5px solid #4CAF50 !important;">
            <v-row class="no-gutters">
              <div class="col pa-3 py-4 success--text">
                <h5 class="text-truncate text-uppercase">
                  Successful parsed articles
                </h5>
                <h1>
                  <!-- {{ getPageViews.total_views }} -->
                  {{ getScraperAnalysis.successful_parsed_articles }}
                </h1>
              </div>
            </v-row>
          </v-card>
        </v-col>
        <v-col lg="4" cols="sm" class="pb-2">
          <v-card dark color="#232323" style="border-left: 5px solid #F44336 !important;">
            <v-row class="no-gutters">
              <div class="col pa-3 py-4 red--text">
                <h5 class="text-truncate text-uppercase">
                  Errors
                </h5>
                <!-- <h1>{{ getRatings.rating_computed }}</h1> -->
                <h1>{{ getScraperAnalysis.unsuccessful_parse_articles }}</h1>
              </div>
            </v-row>
          </v-card>
        </v-col>
        <v-col lg="4" cols="sm" class="pb-2">
          <v-card dark color="#232323" style="border-left: 5px solid #4cacaf !important;">
            <v-row class="no-gutters">
              <div class="col pa-3 py-4" style="color: #4cacaf">
                <h5 class="text-truncate text-uppercase">Missed articles</h5>
                <h1>{{ getScraperAnalysis.missed_articles }}</h1>
              </div>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-card class="mx-auto text-center" dark color="#232323">
            <!-- <apexchart type="line" height="350" :options="chartOptions" :series="series"></apexchart> -->
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
              :labels="labels"
              show-labels
            >
              <!-- <template v-slot:label="item">{{ item.data }}March 29</template> -->
            </v-sparkline>
            <v-card-actions class="py-4 justify-center">
              <!-- <v-btn color="primary" to="/reports">View Report</v-btn> -->
               <v-btn block color="secondary" dark elevation="4" plain :to="{name: 'reports'}" class="text-decoration-none">REPORTS</v-btn>
            </v-card-actions>
          </v-card>
          
        </v-col>
      </v-row>
    </div>
    <div v-else>
      <v-container>
        <v-row>
          <v-col cols="12" md="12">
            <v-row class="my-1">
              <v-col cols="4" v-for="skeleton in 3" :key="skeleton.id">
                <v-skeleton-loader dark type="image"></v-skeleton-loader>
              </v-col>
            </v-row>
            <v-row class="my-1 pa-0">
              <v-col cols="4" v-for="skeleton in 3" :key="skeleton.id">
                <v-skeleton-loader dark type="image"></v-skeleton-loader>
              </v-col>
            </v-row>
            <v-skeleton-loader
              dark
              type="image"
              class="mt-2"
            ></v-skeleton-loader>
            <v-skeleton-loader
              dark
              type="image"
              class="mt-2"
            ></v-skeleton-loader>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <!-- <div id="chart" style="background-color: white">
      <apexchart
        type="area"
        height="350"
        :options="chartOptions"
        :series="series"
      ></apexchart>
    </div> -->
  </div>
</template>

<script>
import { mapGetters } from "vuex";
// import { VueApexCharts } from "apexcharts";
const gradients = [
  ["#222"],
  ["#42b3f4"],
  ["red", "orange", "yellow"],
  ["purple", "violet"],
  ["#00c6ff", "#F0F", "#FF0"],
  ["#f72047", "#ffd200", "#1feaea"],
  ["#007bff", "cyan"],
  ["#01FFFF", "#00ECFA", "#00CEF1", "#00B8EA"],
];
export default {
  name: "dashboard",
  data: () => ({
    sparklineData: [6805, 17208, 13063, 16493, 17063, 13440],
    labels: [
        'March 24, 2021',
        'March 25, 2021',
        'March 26, 2021',
        'March 27, 2021',
        'March 28, 2021',
        'March 29, 2021',
      ],
    width: 2,
    radius: 10,
    padding: 20,
    gradient: gradients[5],
    gradientDirection: "top",
    gradients,
    fill: false,
    type: "trend",
    autoLineWidth: false,
    lineCap: "round",

    // series: [
    //   {
    //     name: "TEAM A",
    //     type: "column",
    //     data: [23, 11, 22, 27, 13, 22, 37, 21, 44, 22, 30],
    //   },
    //   {
    //     name: "TEAM B",
    //     type: "area",
    //     data: [44, 55, 41, 67, 22, 43, 21, 41, 56, 27, 43],
    //   },
    //   {
    //     name: "TEAM C",
    //     type: "line",
    //     data: [30, 25, 36, 30, 45, 35, 64, 52, 59, 36, 39],
    //   },
    // ],
    // chartOptions: {
    //   chart: {
    //     height: 350,
    //     type: "line",
    //     stacked: false,
    //   },
    //   stroke: {
    //     width: [0, 2, 5],
    //     curve: "smooth",
    //   },
    //   plotOptions: {
    //     bar: {
    //       columnWidth: "50%",
    //     },
    //   },

    //   fill: {
    //     opacity: [0.85, 0.25, 1],
    //     gradient: {
    //       inverseColors: false,
    //       shade: "light",
    //       type: "vertical",
    //       opacityFrom: 0.85,
    //       opacityTo: 0.55,
    //       stops: [0, 100, 100, 100],
    //     },
    //   },
    //   labels: [
    //     "01/01/2003",
    //     "02/01/2003",
    //     "03/01/2003",
    //     "04/01/2003",
    //     "05/01/2003",
    //     "06/01/2003",
    //     "07/01/2003",
    //     "08/01/2003",
    //     "09/01/2003",
    //     "10/01/2003",
    //     "11/01/2003",
    //   ],
    //   markers: {
    //     size: 0,
    //   },
    //   xaxis: {
    //     type: "datetime",
    //   },
    //   yaxis: {
    //     title: {
    //       text: "Points",
    //     },
    //     min: 0,
    //   },
    //   tooltip: {
    //     shared: true,
    //     intersect: false,
    //     y: {
    //       formatter: function (y) {
    //         if (typeof y !== "undefined") {
    //           return y.toFixed(0) + " points";
    //         }
    //         return y;
    //       },
    //     },
    //   },
    // },
  }),

  components: {
    // apexchart: VueApexCharts,
  },
  computed: {
    ...mapGetters(["getScraperAnalysis", "getScraperDates"]),
  },
  mounted() {
    // this.mountCrawlerSets();
    // this.mountScrapers();
    console.log(this.getScraperDates);
    this.mountScraperAnalysis();
    this.mountScraperDates();
    console.log("mounted");
  },
  methods: {
    // mountCrawlerSets() {
    //   this.$store.dispatch("fetchCrawlerSets");
    // },
    // mountScrapers() {
    //   this.$store.dispatch("fetchScrapers");
    // },
    mountScraperAnalysis() {
      this.$store.dispatch("fetchScraperAnalysis");
    },
    mountScraperDates() {
      this.$store.dispatch("fetchScraperByDates");
    },
  },
};
</script>

<style scoped>
.b__left {
  border-left: 5px solid red !important;
}
</style>

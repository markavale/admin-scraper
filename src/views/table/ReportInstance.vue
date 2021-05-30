<template>
  <div>
    <v-row>
        <v-col lg="4" cols="sm" class="pb-2">
          <v-card dark color="#232323">
            <v-row class="no-gutters">
              <div class="col-auto" color="#0b00d4">
                <div class="cyan fill-height" color="#4719d2">&nbsp;</div>
              </div>
              <div class="col pa-3 py-4" style="color: #4719d2">
                <h5 class="text-truncate text-uppercase">Total data</h5>
                <h1>
                  <!-- {{ getPageViews.total_views }} -->
                  {{ getReportInstance.data }}
                </h1>
              </div>
            </v-row>
          </v-card>
        </v-col>
        <v-col lg="4" cols="sm" class="pb-2">
          <v-card dark color="#232323">
            <v-row class="no-gutters">
              <div class="col-auto" style="color: #a419d2">
                <div class="fill-height">&nbsp;</div>
              </div>
              <div class="col pa-3 py-4" style="color: #a419d2">
                <h5 class="text-truncate text-uppercase">Total articles</h5>
                <!-- <h1>{{ getRatings.rating_computed }}</h1> -->
                <h1>{{ getReportInstance.crawler_set.total_articles }}</h1>
              </div>
            </v-row>
          </v-card>
        </v-col>
        <v-col lg="4" cols="sm" class="pb-2">
          <v-card dark color="#232323">
            <v-row class="no-gutters">
              <div class="col-auto" style="color: #1975d2">
                <div class="success fill-height">&nbsp;</div>
              </div>
              <div class="col pa-3 py-4" style="color: #1975d2">
                <h5 class="text-truncate text-uppercase">
                  Average Download latency
                </h5>
                <h1>{{ getReportInstance.crawler_set.average_download_latency }}s</h1>
              </div>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col lg="4" cols="sm" class="pb-2">
          <v-card dark color="#232323">
            <v-row class="no-gutters">
              <div class="col-auto" color="#0b00d4">
                <div class="cyan fill-height" color="#4719d2">&nbsp;</div>
              </div>
              <div class="col pa-3 py-4 success--text">
                <h5 class="text-truncate text-uppercase">
                  Successful parsed articles
                </h5>
                <h1>
                  <!-- {{ getPageViews.total_views }} -->
                  {{ getReportInstance.crawler_set.total_parsed_article  }}
                </h1>
              </div>
            </v-row>
          </v-card>
        </v-col>
        <v-col lg="4" cols="sm" class="pb-2">
          <v-card dark color="#232323">
            <v-row class="no-gutters">
              <div class="col-auto" style="color: #a419d2">
                <div class="fill-height">&nbsp;</div>
              </div>
              <div class="col pa-3 py-4 red--text">
                <h5 class="text-truncate text-uppercase">
                  Errors
                </h5>
                <!-- <h1>{{ getRatings.rating_computed }}</h1> -->
                <h1>{{ getReportInstance.crawler_set.total_error  }}</h1>
              </div>
            </v-row>
          </v-card>
        </v-col>
        <v-col lg="4" cols="sm" class="pb-2">
          <v-card dark color="#232323">
            <v-row class="no-gutters">
              <div class="col-auto" style="color: #1975d2">
                <div class="success fill-height">&nbsp;</div>
              </div>
              <div class="col pa-3 py-4" style="color: #4cacaf">
                <h5 class="text-truncate text-uppercase">Missed articles</h5>
                <h1>{{ getReportInstance.total_missed_articles }}</h1>
              </div>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    <v-card dark color="#232323">
      <v-container>
      <div id="chart">
        <apexchart
          type="pie"
          width="380"
          :options="options"
          :series="series"
          
          class="white--text"
        >
        <template v-slot:series>
          {{ getReportInstance.crawler_set.total_parsed_article }}
        </template>
        </apexchart>
        
      </div>
    </v-container>
    </v-card>
    <v-card dark color="#232323">
      <v-container>
      {{ getReportInstance.crawler_set.total_parsed_article }}
      {{ getReportInstance.crawler_set.total_error }}
      {{ getReportInstance.total_missed_articles }}
    </v-container>
    </v-card>
    
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";
import {mapGetters} from "vuex";
export default {
  name: "report-instance",
  components: {
    apexchart: VueApexCharts,
  },
  data: () => ({
    options: {
      labels: ['Success', "Errors", "Missed"],
    },
    series: [1, 2, 3],
  }),
  computed: {
    ...mapGetters(["getReportInstance"])
  },
  created(){
    this.mountReportInstance();
  },
  mounted() {
    this.mountReportInstance()
    console.log("REPORT INSTANCE")
    console.log(this.series)
  },
  methods: {
    mountReportInstance() {
      if (this.$route.params.id) {
        this.$store.dispatch("reportInstance", this.$route.params.id);
        this.series = [this.getReportInstance.crawler_set.total_parsed_article, this.getReportInstance.crawler_set.total_error, this.getReportInstance.total_missed_articles]

        // this.checkWishStatus(this.$route.params.slug);
      }

    },
  },
};
</script>

<style>
</style>
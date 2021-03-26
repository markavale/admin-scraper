<template>
  <div>
    <v-container
      class="my-10"
      style="background-color: #fff; height: 100vh; width: 100vw"
    >
      <!-- <div v-for="item in getScrapers" :key="item.id">
        {{ item.crawler_set }}
        <div v-for="set in item.crawlersets" :key="set.id">
          {{ set }}
        </div>
      </div> -->
      <tr v-for="scraper in getScrapers" :key="scraper.id">
        <td>
          {{ scraper.data }}
        </td>
        <td>
          {{ scraper.crawler_set.total_parsed_article }}
        </td>
        <td>
          {{ scraper.total_threads }}
        </td>
        <td>29</td>
        <td>
          {{ scraper.crawler_set.average_download_latency }}
        </td>
        <td>
          {{ scraper.time_finished }}
        </td>
        <td>
          {{ scraper.timestamp }}
        </td>
      </tr>
    </v-container>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "test",
  computed: {
    ...mapGetters(["getScrapers", "getCrawlerSets"]),
  },
  mounted() {
    this.mountCrawlerSets();
    this.mountScrapers();
  },
  methods: {
    mountCrawlerSets() {
      this.$store.dispatch("fetchCrawlerSets");
    },
    mountScrapers() {
      this.$store.dispatch("fetchScrapers");
    },
  },
};
</script>

<style>
</style>
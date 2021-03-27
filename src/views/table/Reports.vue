<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="getScrapers"
      sort-by="parse"
      class="elevation-1 mt-10 pt-10"
      show-expand
      :single-expand="true"
      :expanded.sync="expanded"
      dark
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Scraper Logs</v-toolbar-title>
          <!-- <div v-for="item in getCrawlerSets" :key="item.id">
            {{ item }}
          </div> -->

          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <!-- <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
              New Item
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.name"
                      label="Dessert name"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.parse"
                      label="parse"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.spider"
                      label="spider (g)"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.thread_spider"
                      label="thread_spider (g)"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.article"
                      label="article (g)"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close"> Cancel </v-btn>
              <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog> -->
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="headline"
                >Are you sure you want to delete this item?</v-card-title
              >
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDelete"
                  >Cancel</v-btn
                >
                <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                  >OK</v-btn
                >
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>

      <template v-slot:expanded-item="{ headers, item }">
        <td :colspan="headers.length / 2 + 1">
          <v-container>
            <v-card color="#385F73" dark class="mx-auto text--center" height="330px">
              <v-card-title class="headline"
                ><v-icon class="mr-2">info</v-icon>Info logs
              </v-card-title>
                <v-card-text
                  class="pa-0 mx-5"
                  v-for="(text, index) in item.info_log.split(`\\n'`)"
                  :key="index"
                  >{{ text }}</v-card-text
                >

              <v-card-actions>
                <v-btn text> Listen Now </v-btn>
              </v-card-actions>
            </v-card>
          </v-container>
        </td>

        <td :colspan="headers.length / 2 - 1">
          <v-container>
            <v-card color="#db645c" dark height="330px">
              <v-card-title class="headline">
                <v-icon class="mr-2">error</v-icon>Error logs
              </v-card-title>

              <v-card-text
                class="pa-0 mx-5"
                v-for="(text, index) in item.info_log.split(`\\n'`)"
                :key="index"
                >{{ text }}</v-card-text
              >

              <v-card-actions>
                <v-btn text> Listen Now </v-btn>
              </v-card-actions>
            </v-card>
          </v-container>
        </td>

        <!-- </tr> -->
      </template>

      <template v-slot:item.data="{ item }">
        <span>{{ item.data }}</span>
      </template>

      <template v-slot:item.articles="{ item }">
        {{ item.crawler_set.total_articles }}
      </template>

      <template v-slot:item.success_parse="{ item }">
        <v-chip :color="getColor(item.crawler_set.total_parsed_article)" dark>
          {{ item.crawler_set.total_parsed_article }}
        </v-chip>
      </template>

      <template v-slot:item.unsuccess_parse="{ item }">
        {{ item.crawler_set.total_error }}
      </template>

      <template v-slot:item.missed_articles="{ item }">
        {{ item.total_missed_articles }}
      </template>

      <template v-slot:item.download_latency="{ item }">
        {{ item.crawler_set.average_download_latency }}
      </template>

      <template v-slot:item.spiders="{ item }">
        <span>{{ item.workers }}</span>
      </template>

      <template v-slot:item.threads="{ item }">
        <span>{{ item.total_threads }}</span>
      </template>

      <template v-slot:item.time_finished="{ item }">
        <span>{{ item.time_finished }}</span>
      </template>

      <template v-slot:item.date="{ item }">
        <span>{{ item.timestamp | formDate }}</span>
      </template>

      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" color="success" @click="editItem(item)">
          mdi-pencil
        </v-icon>
        <v-icon small @click="deleteItem(item)" color="red">
          mdi-delete
        </v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary"> Reset </v-btn>
      </template>
    </v-data-table>
    <div style="color: white">
      {{ getScrapers.length }}
    </div>
  </div>
</template>
<script>
// import moment from "moment";
import { mapGetters } from "vuex";
export default {
  data: () => ({
    expanded: [],
    dialog: false,
    dialogDelete: false,
    headers: [
      { text: "", value: "data-table-expand" },
      {
        text: "Data",
        align: "center",
        sortable: true,
        value: "data",
      },
      { text: "Articles", align: "center", value: "articles" },
      { text: "Successful parsed articles", value: "success_parse" },
      { text: "Unsuccessful parse articles", value: "unsuccess_parse" },
      { text: "Missed articles", value: "missed_articles" },
      { text: "Average download latency", value: "download_latency" },
      { text: "Spiders", align: "center", value: "spiders" },
      { text: "Threads", align: "center", value: "threads" },
      { text: "Time finished", align: "center", value: "time_finished" },
      { text: "Date", align: "center", value: "date" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    desserts: [],
    editedIndex: -1,
    editedItem: {
      data: 0,
      parse: 0,
      spider: 0,
      thread_spider: 0,
      article: 0,
    },
    defaultItem: {
      data: 0,
      articles: 21,
      success_parse: 0,
      unsuccess_parse: 0,
      missed_articles: 0,
      download_latency: 0,
      spiders: 0,
      threads: 0,
      time_finish: 0,
      date: null,
    },
  }),

  computed: {
    // formDate(value) {
    //   if (value) {
    //     return moment(String(value)).format("MM/DD/YYYY hh:mm");
    //   }
    // },
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },
    ...mapGetters(["getScrapers", "getCrawlerSets"]),
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },
  mounted() {
    this.mountCrawlerSets();
    this.mountScrapers();
  },

  methods: {
    getColor(parse) {
      if (parse < 200) return "red";
      else if (parse > 400) return "green";
      else return "orange";
    },

    editItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      this.desserts.splice(this.editedIndex, 1);
      this.closeDelete();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.desserts[this.editedIndex], this.editedItem);
      } else {
        this.desserts.push(this.editedItem);
      }
      this.close();
    },
    mountCrawlerSets() {
      this.$store.dispatch("fetchCrawlerSets");
    },
    mountScrapers() {
      this.$store.dispatch("fetchScrapers");
    },

    /**
     * In a real application this would be a call to fetch() or axios.get()
     */
    // fakeApiCall () {
    //   return new Promise((resolve, reject) => {
    //     const { sortBy, sortDesc, page, itemsPerPage } = this.options

    //     let items = this.getDesserts()
    //     const total = items.length

    //     if (sortBy.length === 1 && sortDesc.length === 1) {
    //       items = items.sort((a, b) => {
    //         const sortA = a[sortBy[0]]
    //         const sortB = b[sortBy[0]]

    //         if (sortDesc[0]) {
    //           if (sortA < sortB) return 1
    //           if (sortA > sortB) return -1
    //           return 0
    //         } else {
    //           if (sortA < sortB) return -1
    //           if (sortA > sortB) return 1
    //           return 0
    //         }
    //       })
    //     }

    //     if (itemsPerPage > 0) {
    //       items = items.slice((page - 1) * itemsPerPage, page * itemsPerPage)
    //     }

    //     setTimeout(() => {
    //       resolve({
    //         items,
    //         total,
    //       })
    //     }, 1000)
    //   })
    // },
  },
};
</script>

<style scoped>
/* html {
  overflow: hidden !important;
}
.v-card {
  display: flex !important;
  flex-direction: column;
}

.v-card__text {
  flex-grow: 1;
  overflow: auto;
} */
</style>
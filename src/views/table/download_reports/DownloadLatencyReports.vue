<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="getWebsiteDownloadLatency"
      sort-by="parse"
      class="elevation-1 mt-10 pt-10"
      show-expand
      :single-expand="true"
      :expanded.sync="expanded"
      dark
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Website Download Latency</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-tooltip top>
            <template v-slot:activator="{ on, attrs }">
              <download-excel
                
                class=""
                :data="getWebsiteDownloadLatency"
                worksheet="My Worksheet"
                name="website_download_latency.xls"
              >
                <v-btn color="#31BE7D" v-bind="attrs"
                v-on="on" class="ma-2 white--text" fab small>
                  <v-icon dark> mdi-microsoft-excel </v-icon>
                </v-btn>
              </download-excel>
            </template>
            <span>Export to excel file</span>
          </v-tooltip>
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
      <template v-slot:expanded-item="{headers, item }">
        <td :colspan="headers.length">
            <v-container>
              <v-card
                color="#385F73"
                dark
                height="auto"
                max-width="750px"
              >
                <v-card-title class="headline"
                  ><v-icon class="mr-2">mdi-view-list</v-icon>Download Latency List
                </v-card-title>
                <v-card-text
                  >{{ item.download_latency_objects }}</v-card-text
                >
              </v-card>
            </v-container>
        </td>
      </template>

      <template v-slot:item.fqdn="{ item }">
        <span><a :href="'http://www.'+item.fqdn">{{ item.fqdn }}</a></span>
      </template>

      <template v-slot:item.average_download_latency="{ item }">
        {{ item.average_download_latency }}
      </template>

      <template v-slot:item.total_objects="{ item }">
          {{ item.total_objects }}
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" color="primary" @click="viewInstance(item)">
          mdi-eye
        </v-icon>
        <v-icon small class="mr-2" color="success" @click="editItem(item)">
          mdi-pencil
        </v-icon>
        <v-icon small @click="deleteItem(item)" color="red">
          mdi-delete
        </v-icon>
      </template>
      <template v-slot:no-data>
        loading...
        <!-- <v-btn color="primary"> Reset </v-btn> -->
      </template>
    </v-data-table>
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
        text: "Website",
        align: "center",
        sortable: true,
        value: "fqdn",
      },
      { text: "Average Download Latency", align: "center", value: "average_download_latency" },
      { text: "Total Download Latency", align: "center", value: "total_objects" },
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
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },
    ...mapGetters(["getWebsiteDownloadLatency"]),
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
    this.mountWebsiteDownloadLatency();
  },

  methods: {
    viewInstance(item){
      console.log(item.id)
      this.$router.push({name: 'report-instance', params: {id: item.id}})  
    },
    getColor(item) {
      if (item.crawler_set.parser_percentage < 75) return "red";
      else if (item.crawler_set.parser_percentage > 90) return "green";
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
    mountWebsiteDownloadLatency() {
      this.$store.dispatch("websiteDownloadLatency");
    },
  },
};
</script>

<style scoped>
.truncate {
      max-width: 1px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
</style>
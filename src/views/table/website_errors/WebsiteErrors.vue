<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="getArticleErrors"
      :sort-by="[
        'fqdn',
        'total_errors',
        'http_errors',
        'dns_errors',
        'timeout_errors',
        'base_errors',
        'missed_urls',
      ]"
      class="elevation-1 mt-10 pt-10"
      dark
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Website Errors</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-tooltip top>
            <template v-slot:activator="{ on, attrs }">
              <download-excel
                
                class=""
                :data="getArticleErrors"
                worksheet="My Worksheet"
                name="website_errors.xls"
              >
                <v-btn color="#31BE7D" v-bind="attrs"
                v-on="on" class="ma-2 white--text" fab small>
                  <v-icon dark> mdi-microsoft-excel </v-icon>
                </v-btn>
              </download-excel>
            </template>
            <span>Export to excel file</span>
          </v-tooltip>
        </v-toolbar>
      </template>

      <template v-slot:item.fqdn="{ item }">
        <span><a :href="'http://www.'+ item.fqdn" target="new">{{ item.fqdn }}</a></span>
      </template>

      <template v-slot:item.total_errors="{ item }">
        {{ item.total_errors }}
      </template>

      <template v-slot:item.http_errors="{ item }">
        {{ item.total_http_errors }}
      </template>

      <template v-slot:item.dns_errors="{ item }">
        {{ item.total_dns_error }}
      </template>

      <template v-slot:item.timeout_errors="{ item }">
        {{ item.total_timeout_error }}
      </template>

      <template v-slot:item.base_errors="{ item }">
        {{ item.total_base_error }}
      </template>

      <template v-slot:item.missed_urls="{ item }">
        <span>{{ item.total_missed_url }}</span>
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
      {
        text: "Errors",
        align: "center",
        sortable: true,
        value: "total_errors",
      },
      {
        text: "HTTP Errors",
        align: "center",
        sortable: true,
        value: "http_errors",
      },
      {
        text: "DNS Errors",
        align: "center",
        sortable: true,
        value: "dns_errors",
      },
      {
        text: "Timeout Errors",
        align: "center",
        sortable: true,
        value: "timeout_errors",
      },
      {
        text: "Base Errors",
        align: "center",
        sortable: true,
        value: "base_errors",
      },
      {
        text: "Missed URLs",
        align: "center",
        sortable: true,
        value: "missed_urls",
      },
      { text: "Actions", value: "actions", sortable: false },
    ],
    desserts: [],
    editedIndex: -1,
    editedItem: {
      fqdn: 0,
      total_errors: 0,
      http_errors: 0,
      timeout_errors: 0,
      dns_errors: 0,
      base_errors: 0,
      missed_urls: 0,
    },
    defaultItem: {
      fqdn: 0,
      total_errors: 0,
      http_errors: 0,
      timeout_errors: 0,
      dns_errors: 0,
      base_errors: 0,
      missed_urls: 0,
    },
  }),

  computed: {
    ...mapGetters(["getArticleErrors"]),
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
    this.mountWebsiteErrorReports();
  },

  methods: {
    viewInstance(item) {
      console.log(item.id);
      this.$router.push({ name: "report-instance", params: { id: item.id } });
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

    mountWebsiteErrorReports() {
      this.$store.dispatch("websiteErrorReports");
    },

    // custom sorting
    customSort: function (items, index, isDesc) {
      items.sort((a, b) => {
        if (index[0] == "date") {
          if (!isDesc[0]) {
            return new Date(b[index]) - new Date(a[index]);
          } else {
            return new Date(a[index]) - new Date(b[index]);
          }
        } else {
          if (typeof a[index] !== "undefined") {
            if (!isDesc[0]) {
              return a[index]
                .toLowerCase()
                .localeCompare(b[index].toLowerCase());
            } else {
              return b[index]
                .toLowerCase()
                .localeCompare(a[index].toLowerCase());
            }
          }
        }
      });
      return items;
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
<template>
  <v-data-table
    :headers="headers"
    :items="desserts"
    sort-by="parse"
    class="elevation-1 mt-10 pt-10"
    dark
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Reports</v-toolbar-title>
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
    <template v-slot:item.actions="{ item }">
      <v-icon small class="mr-2" color="success" @click="editItem(item)">
        mdi-pencil
      </v-icon>
      <v-icon small @click="deleteItem(item)" color="red"> mdi-delete </v-icon>
    </template>
    <template v-slot:no-data>
      <v-btn color="primary" @click="initialize"> Reset </v-btn>
    </template>
    <template v-slot:item.parse="{ item }">
      <v-chip :color="getColor(item.parse)" dark>
        {{ item.parse }}
      </v-chip>
    </template>
  </v-data-table>
</template>
<script>
export default {
  data: () => ({
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: "Total Articles",
        align: "center",
        sortable: false,
        value: "name",
      },
      { text: "Parse", value: "parse" },
      { text: "Spiders", value: "spider" },
      { text: "Thread spider", value: "thread_spider" },
      { text: "Article", value: "article" },
      { text: "Download latency", value: "download_latency" },
      { text: "Time finish", value: "time_finish" },
      { text: "Date", value: "date" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    desserts: [],
    editedIndex: -1,
    editedItem: {
      name: "",
      parse: 0,
      spider: 0,
      thread_spider: 0,
      article: 0,
    },
    defaultItem: {
      name: "",
      parse: 0,
      spider: 0,
      thread_spider: 0,
      article: 0,
      download_latency: 0,
    },
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },

  created() {
    this.initialize();
  },

  methods: {
    getColor(parse) {
      if (parse < 200) return "red";
      else if (parse > 400) return "green";
      else return "orange";
    },
    initialize() {
      this.desserts = [
        {
          name: 518,
          parse: 159,
          spider: 6,
          thread_spider: 3,
          article: 29,
          download_latency: 3.21,
          time_finish: "00:42:24",
          date: "2021-03-16T10:38:17.488886+08:00",
        },
        {
          name: 518,
          parse: 237,
          spider: 6,
          thread_spider: 3,
          article: 29,
          download_latency: 0.32,
          time_finish: "00:42:24",
          date: "2021-03-16T10:38:17.488886+08:00",
        },
        {
          name: 518,
          parse: 262,
          spider: 6,
          thread_spider: 3,
          article: 29,
          download_latency: 14.42,
          time_finish: "00:42:24",
          date: "2021-03-16T10:38:17.488886+08:00",
        },
        {
          name: 518,
          parse: 305,
          spider: 6,
          thread_spider: 3,
          article: 29,
          download_latency: 0.32,
          time_finish: "00:42:24",
          date: "2021-03-16T10:38:17.488886+08:00",
        },
        {
          name: 518,
          parse: 356,
          spider: 6,
          thread_spider: 3,
          article: 29,
          download_latency: 2.32,
          time_finish: "00:42:24",
          date: "2021-03-16T10:38:17.488886+08:00",
        },
        {
          name: 518,
          parse: 375,
          spider: 6,
          thread_spider: 3,
          article: 29,
          download_latency: 15.52,
          time_finish: "00:42:24",
          date: "2021-03-16T10:38:17.488886+08:00",
        },
        {
          name: 518,
          parse: 392,
          spider: 6,
          thread_spider: 3,
          article: 29,
          download_latency: 1.41,
          time_finish: "00:42:24",
          date: "2021-03-16T10:38:17.488886+08:00",
        },
        {
          name: 518,
          parse: 408,
          spider: 6,
          thread_spider: 3,
          article: 29,
          download_latency: 5.21,
          time_finish: "00:42:24",
          date: "2021-03-16T10:38:17.488886+08:00",
        },
        {
          name: 518,
          parse: 452,
          spider: 6,
          thread_spider: 3,
          article: 29,
          download_latency: 3.12,
          time_finish: "00:42:24",
          date: "2021-03-16T10:38:17.488886+08:00",
        },
        {
          name: 518,
          parse: 518,
          spider: 6,
          thread_spider: 3,
          article: 29,
          download_latency: 19.41,
          time_finish: "00:42:24",
          date: "2021-03-16T10:38:17.488886+08:00",
        },
      ];
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
  },
};
</script>

<style>
</style>
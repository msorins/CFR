<template>
  <v-container>
    <v-card>
      <v-btn
        type="file"
        id="file"
        ref="file"
        style="width: 98%;"
        color="success"
        v-on:change="uploadCV()"
        @click="$refs.file.click()"
      >Upload CV</v-btn>
      <input v-show="false" ref="file" type="file" @change="uploadCV">

      <v-tabs fixed-tabs v-model="tabs">
        <v-tab :key="ok">
          <v-icon>done</v-icon>
        </v-tab>
        <v-tab :key="nok">
          <v-icon>sentiment_dissatisfied</v-icon>
        </v-tab>
      </v-tabs>

      <v-tabs-items v-model="tabs">
        <v-tab-item :key="ok">
          <v-card>
            <v-card-text>
              <!-- #### Positive list #### -->
              <v-list
                v-bind:key="item.evaluator"
                v-for="item in feedbackPositive"
                two-line
                subheader
              >
                <v-subheader inset>{{item[0].evaluator}}</v-subheader>

                <v-list-tile v-for="feedback in item" :key="feedback.message" avatar>
                  <v-list-tile-avatar>
                    <v-icon :class="[item.iconClass]">assignment</v-icon>
                  </v-list-tile-avatar>

                  <v-list-tile-content>
                    <v-list-tile-title>{{ feedback.message }}</v-list-tile-title>
                  </v-list-tile-content>

                  <v-list-tile-action>
                    <v-btn icon ripple>
                      <v-icon color="grey lighten-1">info</v-icon>
                    </v-btn>
                  </v-list-tile-action>
                </v-list-tile>

                <v-divider inset></v-divider>
              </v-list>
            </v-card-text>
          </v-card>
        </v-tab-item>

        <v-tab-item :key="nok">
          <v-card>
            <v-card-text>
              <!-- #### Negative list #### -->
              <v-list
                v-bind:key="item.evaluator"
                v-for="item in feedbackNegative"
                two-line
                subheader
              >
                <v-subheader inset>{{item[0].evaluator}}</v-subheader>

                <v-list-tile v-for="feedback in item" :key="feedback.message" avatar>
                  <v-list-tile-avatar>
                    <v-icon :class="[item.iconClass]">assignment</v-icon>
                  </v-list-tile-avatar>

                  <v-list-tile-content>
                    <v-list-tile-title>{{ feedback.message }}</v-list-tile-title>
                  </v-list-tile-content>

                  <v-list-tile-action>
                    <v-btn icon ripple>
                      <v-icon color="grey lighten-1">info</v-icon>
                    </v-btn>
                  </v-list-tile-action>
                </v-list-tile>

                <v-divider inset></v-divider>
              </v-list>
            </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
    </v-card>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    card_text: "Hello World",
    file: "",
    tabs: null,
    ok: "ok",
    nok: "nok",
    feedbackPositive: [],
    feedbackNegative: []
  }),
  methods: {
    uploadCV() {
      this.file = this.$refs.file.files[0];

      // Create formData and append the file
      let formData = new FormData();
      formData.append("file", this.file);

      // Send the request
      var this2 = this;
      this.axios
        .post("http://127.0.0.1:5000/submit", formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
        .then(function(output) {
          console.log("SUCCESS!!");

          var byCategoryPositive = {};
          var byCategoryNegative = {};

          for (var i = 0; i < output.data.length; i++) {
            if (output.data[i].points != 0) {
              if (!(output.data[i].evaluator in byCategoryPositive)) {
                byCategoryPositive[output.data[i].evaluator] = [];
              }
              byCategoryPositive[output.data[i].evaluator].push(output.data[i]);
            } else {
              if (!(output.data[i].evaluator in byCategoryNegative)) {
                byCategoryNegative[output.data[i].evaluator] = [];
              }
              byCategoryNegative[output.data[i].evaluator].push(output.data[i]);
            }
          }

          console.log("Positive: ", byCategoryPositive);
          this2.$data.feedbackPositive = byCategoryPositive;

          console.log("Negative: ", byCategoryNegative);
          this2.$data.feedbackNegative = byCategoryNegative;
        })
        .catch(function(err) {
          console.log("FAILURE!! ", err);
        });
    }
  }
};
</script>

<style>
</style>

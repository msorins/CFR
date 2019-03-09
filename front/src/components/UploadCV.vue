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
    </v-card>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    card_text: "Hello World",
    file: ""
  }),
  methods: {
    uploadCV() {
      this.file = this.$refs.file.files[0];

      // Create formData and append the file
      let formData = new FormData();
      formData.append("file", this.file);
      console.log(formData.getAll("file"));

      // Send the request
      this.axios
        .post("http://127.0.0.1:5000/submit", formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
        .then(function() {
          console.log("SUCCESS!!");
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

<template>
  <v-container>
    <v-card>
      <v-btn style="width: 98%;" color="success" @click="$refs.inputUpload.click()">Upload CV</v-btn>
      <input v-show="false" ref="inputUpload" type="file" @change="uploadCV">
    </v-card>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    card_text: "Hello World"
  }),
  methods: {
    uploadCV(e) {
      const files = e.target.files;
      if (files[0] !== undefined) {
        const cvName = files[0].name;
        console.log(cvName);

        if (cvName.lastIndexOf(".") <= 0) {
          return;
        }

        const fr = new FileReader();
        fr.readAsDataURL(files[0]);
        fr.addEventListener("load", () => {
          var cvFile = fr.result; // this is the file that can be sent to server...

          // Create formData and append the file
          let formData = new FormData();
          formData.append("file", cvFile);
          console.log(formData.getAll('file'))


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
        });
      } else {
        console.log("Error when receiving the CV");
      }
    }
  }
};
</script>

<style>
</style>

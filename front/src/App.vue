<template>
  <v-app>
    <v-content>
      <UploadCV/>
    </v-content>
  </v-app>
</template>

<script>
import UploadCV from './components/UploadCV'

export default {
  name: 'App',
  components: {
    UploadCV
  },
  data () {
    return {
      //
    }
  }
}
</script>

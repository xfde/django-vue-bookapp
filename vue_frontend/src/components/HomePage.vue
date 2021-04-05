<template>
  <div :style="cssProps"><h1 style="color:#f5f5f5;marginTop:100px;fontSize:7em;">Book Library</h1></div>
</template>

<script>
export default {
  name: "HomePage",
  data() {
    return {
      cssProps: {
        backgroundImage: `url(${require("../assets/background.jpg")})`,
        height: '90vh',
        opacity: '0.8',
      },
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

<template>
  <el-container>
    <el-header>
      <router-link v-if="!this.$store.state.isLoggedin" to="/login" tag="button"
        >Login</router-link
      >
      <router-link
        v-if="!this.$store.state.isLoggedin"
        to="/register"
        tag="button"
        >Register</router-link
      >
      <router-link
        v-if="this.$store.state.isLoggedin"
        to="/mybooks"
        tag="button"
        >Favorite Books</router-link
      >
      <router-link
        v-if="this.$store.state.isLoggedin"
        to="/books"
        tag="button"
        >All Books</router-link
      >
            <router-link
        v-if="this.$store.state.isLoggedin"
        to="/addbook"
        tag="button"
        >Add Book</router-link
      >
      <el-button
        v-on:click="logout"
        type="info"
        round
        v-if="this.$store.state.isLoggedin"
        >Logout</el-button
      >
    </el-header>
    <router-view />
    <el-footer
      >Made by
      <a href="https://alexconstantin.com" target="_blank"
        >Alexandru Constantin</a
      ></el-footer
    >
  </el-container>
</template>

<script>
import axios from "axios";
import { ElContainer, ElHeader, ElFooter, ElButton } from "element-plus";
export default {
  name: "app",
  components: {
    ElContainer,
    ElHeader,
    ElFooter,
    ElButton,
  },
  methods: {
    logout: function () {
      const csrftoken = this.$cookie.getCookie("csrftoken");
      axios.post("http://127.0.0.1:8000/api/logout/",{},            {
              headers: {
                "X-CSRFToken": csrftoken
              },
            }).then((response) => {
        if (response.data == "Logged out") {
          this.$store.commit("setrenderF")
          this.$router.push("/");
          this.$store.commit("logout");
          this.$toast.show(response.data, {
            duration: 3000,
          });
        } else {
          this.$router.push("/");
          this.$toast.show(response.data, {
            duration: 3000,
          });
        }
      });
    },
  },
  mounted() {
    axios.get("http://127.0.0.1:8000/api/checklogin/").then((response) => {
      if (response.data == true) {
        this.$store.commit("login");
        this.$store.commit("setrenderT")
      }
      else{
        this.$store.commit("setrenderF")
      }
    });
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
a.router-link-exact-active {
  color: #43fdc2;
}
a {
  color: #b3c0d1;
  text-decoration: none;
  padding-right: 9px;
}
.el-header {
  background-color: #0b305f;
  color: #333;
  text-align: right;
  line-height: 60px;
}
.el-footer {
  position: fixed;
  bottom: 0%;
  right: 0%;
  left: 0%;
  background-color: #0b305f;
  color: rgb(206, 206, 206);
  text-align: center;
  line-height: 60px;
}
</style>

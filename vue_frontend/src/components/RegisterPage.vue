<template>
  <el-card>
    <h2>Register</h2>
    <el-form
      class="login-form"
      :model="model"
      :rules="rules"
      @submit="submit"
      ref="form"
    >
      <el-form-item prop="username">
        <el-input v-model="model.username" placeholder="Username"></el-input>
      </el-form-item>
      <el-form-item prop="password1">
        <el-input
          v-model="model.password1"
          placeholder="Input Password"
          type="password"
        ></el-input>
      </el-form-item>
      <el-form-item prop="password2">
        <el-input
          v-model="model.password2"
          placeholder="Repeat Password"
          type="password"
        ></el-input>
      </el-form-item>
      <el-form-item>
        <el-button class="login-button" type="primary" block @click="submit"
          >Register</el-button
        >
      </el-form-item>
    </el-form>
  </el-card>
</template>

<script>
import { ElCard, ElInput, ElForm, ElButton, ElFormItem } from "element-plus";
import axios from "axios";
export default {
  name: "LoginPage",
  methods: {
    submit: function () {
      //validation
      const re = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
      if (this.model.username === "") {
        this.$toast.error("Username must not be empty", {
          position: "bottom-right",
          duration: 5000,
        });
        return;
      } else if (!re.test(this.model.password1)) {
        this.$toast.error("Password must be at least 8 characters, have one number and one letter",{
            position: "bottom-right",
            duration: 5000,
          }
        );
        return;
      } else if (this.model.password2 !== this.model.password1) {
        this.$toast.error("Passwords must match", {
          position: "bottom-right",
          duration: 5000,
        });
        return;
      } else {
        const csrftoken = this.$cookie.getCookie("csrftoken");
        axios
          .post(
            "http://127.0.0.1:8000/api/register/",
            {
              username: this.model.username,
              password1: this.model.password1,
              password2: this.model.password2,
            },
            {
              headers: {
                "X-CSRFToken": csrftoken,
                "Content-Type": "application/x-www-form-urlencoded",
              },
            }
          )
          .then((response) => {
            if (response.data === "authentication successful") {
              this.$store.commit("login");
              this.$store.commit("setrenderT")
              this.$toast.success(response.data, {
                position: "bottom-right",
                duration: 5000,
              });
              this.$router.push("/");
            } else {
              this.$toast.error(response.data, {
                position: "bottom-right",
                duration: 5000,
              });
            }
          });
      }
    },
  },
  data() {
    return {
      model: {
        username: "",
        password1: "",
        password2: "",
      },
      rules: {
        username: [
          {
            required: true,
            message: "Username is required",
            trigger: "blur",
          },
          {
            min: 4,
            message: "Username length should be at least 5 characters",
            trigger: "blur",
          },
        ],
        password1: [
          { required: true, message: "Password is required", trigger: "blur" },
          {
            min: 5,
            message: "Password length should be at least 5 characters",
            trigger: "blur",
          },
        ],
      },
    };
  },
  components: {
    ElCard,
    ElInput,
    ElForm,
    ElButton,
    ElFormItem,
  },
};
</script>

<style scoped>
.login {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-button {
  width: 100%;
  margin-top: 40px;
}
.login-form {
  width: 290px;
  display: flex;
  flex-direction: column;
  margin: auto;
  width: 50%;
}
.el-card__body {
  align-content: center;
  justify-content: center;
  align-items: center;
}
</style>

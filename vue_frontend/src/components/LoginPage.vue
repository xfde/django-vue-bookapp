<template>
  <el-card>
    <h2>Login</h2>
    <el-form class="login-form" :model="model" :rules="rules" ref="form">
      <el-form-item prop="username">
        <el-input
          v-model="model.username"
          placeholder="Username"
        ></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input
          v-model="model.password"
          placeholder="Password"
          type="password"
        ></el-input>
      </el-form-item>
      <el-form-item>
        <el-button
          class="login-button"
          type="primary"
          @click="submit"
          block
          >Login</el-button
        >
      </el-form-item>
    </el-form>
  </el-card>
</template>

<script>
import { ElCard, ElInput, ElForm, ElButton,ElFormItem } from "element-plus";
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
      } else if (!re.test(this.model.password)) {
        this.$toast.error("Password must be at least 8 characters, have one number and one letter",{
            position: "bottom-right",
            duration: 5000,
          }
        );
        return;
      } else {
        const csrftoken = this.$cookie.getCookie("csrftoken");
        axios
          .post(
            "http://127.0.0.1:8000/api/login/",
            {
              username: this.model.username,
              password: this.model.password,
            },
            {
              headers: {
                "X-CSRFToken": csrftoken,
                "Content-Type": "application/x-www-form-urlencoded",
              },
            }
          )
          .then((response) => {
            if (response.data === "Login successful") {
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
    }
  },
  data() {
    return {
      model: {
        username: "",
        password: "",
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
        password: [
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
.el-card__body{
    align-content: center;
    justify-content: center;
    align-items: center;
}
</style>

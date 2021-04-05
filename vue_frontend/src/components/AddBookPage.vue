<template>
  <el-container>
    <el-col v-if="!render">
        <h1>Permission Denied</h1>
    </el-col>
    <el-col v-if="render">
      <h1>Add a book to the database</h1>
        <el-card>
      <el-form class="login-form" :model="model" ref="form">
        <el-form-item  prop="title" label="Title">
            <el-input type="textarea" v-model="model.title"></el-input>
        </el-form-item>
        <el-form-item  label="Author" prop="author">
            <el-input type="textarea" v-model="model.author"></el-input>
        </el-form-item>
        <el-form-item label="Description" prop="description">
            <el-input type="textarea" v-model="model.description"></el-input>
        </el-form-item>
        <input type="file" name="file" @change="handleUpload($event)"/>
        <div class="el-upload__tip">jpg/png files with a size less than 500kb</div>
        <el-button type="primary" @click="addBook">Add</el-button>
      </el-form>
        </el-card>
      <div style="height: 60px; marginBottom: 60px;"><h1></h1></div>
    </el-col>
  </el-container>
</template>

<script>
import { ElContainer, ElButton, ElCol, ElForm, ElFormItem, ElInput,ElCard} from "element-plus";
import axios from "axios";
export default {
  name: "BooksPage",
  components: {
    ElContainer,
    ElButton,
    ElCol,
    ElCard,
    ElForm, ElFormItem, ElInput
  },
  data() {
    return {
      render:this.$store.state.render,
      model: {
        title: "",
        author: "",
        description: "",
        image: null,
      }
    };
  },
  methods: {
    handleUpload: function(event){
       let file = event.target.files[0]
       this.model.image = file
    }, 
    addBook: function(){
        const csrftoken = this.$cookie.getCookie("csrftoken");
        const formdata = new FormData()
        formdata.append('title',this.model.title)
        formdata.append('author',this.model.author)
        formdata.append('description', this.model.description)
        formdata.append('poster_image', this.model.image)

        axios.post("http://127.0.0.1:8000/api/addbook/",
          formdata,
          {
            headers: {
              "X-CSRFToken": csrftoken,
              "Content-Type": "application/x-www-form-urlencoded",
            }
          })
        .then((response) => {
          if(response.data =="Book successfully added."){
              this.$toast.show(response.data,{
              duration: 4000
            });
            this.$router.push("/");
          }
          
        });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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

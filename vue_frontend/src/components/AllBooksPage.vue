<template>
  <el-container>
    <el-col v-if="!render">
        <h1>Permission Denied</h1>
    </el-col>
    <el-col v-if="render">
      <h1>All books</h1>
      <el-row style="marginLeft: 30px;">
        <el-card
          v-for="item in arr"
          :body-style="{ padding: '0px', width: '300px', height: '750px' }"
          v-bind:key="item['title']"
        >
          <img
            v-bind:src="item['poster_image']"
            style="maxHeight: 400px;"
            class="image"
          />
          <div style="padding: 14px;">
            <h4>{{ item["title"] }}</h4>
            <h5>{{ item["author"] }}</h5>
            <span
              style="
                fontSize: 11px;
                overflow: hidden;
                text-overflow: ellipsis;
                maxHeight: 250px;
              "
              >{{ item["description"] }}</span
            >
            <div class="bottom">
              <el-button
                type="text"
                :style="{ color: '	#32CD32' }"
                @click="addFavourites(item['title'])"
                class="button"
                >Add to Favourties</el-button
              >
            </div>
          </div>
        </el-card>
      </el-row>
      <div style="height: 60px; marginBottom: 60px;"><h1></h1></div>
    </el-col>
  </el-container>
</template>

<script>
import { ElContainer, ElButton, ElCard, ElRow, ElCol } from "element-plus";
import axios from "axios";
export default {
  name: "BooksPage",
  components: {
    ElContainer,
    ElButton,
    ElCard,
    ElRow,
    ElCol,
  },
  data() {
    return {
      arr: this.$store.state.array,
      render: this.$store.state.render,
    };
  },
  methods: {
    addFavourites: function (title_s) {
    console.log(typeof(title_s))
      const csrftoken = this.$cookie.getCookie("csrftoken");
      axios
        .post("http://127.0.0.1:8000/api/addfavourites/",
          { title:title_s },
          {
            headers: {
              "X-CSRFToken": csrftoken,
              "Content-Type": "application/x-www-form-urlencoded",
            }
          })
        .then((response) => {
          this.$toast.show(response.data,{
              duration: 4000
          });
        });
    },
  },
  mounted(){
      axios
      .get("http://127.0.0.1:8000/api/books/")
      .then((response) => {
        if(response.data == "Permission Denied"){
          this.$store.commit("setrenderF")
        }else{
          this.$store.commit("arraydata",response.data)
          this.arr = response.data
        }
      });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.button {
  padding: 0;
  min-height: auto;
}

.image {
  width: 100%;
  display: block;
}
</style>

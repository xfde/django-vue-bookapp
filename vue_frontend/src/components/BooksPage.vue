<template>
  <el-container>
    <el-col v-if="!render">
        <h1>Permission Denied</h1>
    </el-col>
    <el-col v-if="render">
      <h1>My Favourite Books</h1>
      <el-row style="marginLeft: 30px;">
        <el-card v-for="item in arr" :body-style="{ padding: '0px', width: '300px', height: '750px' }" v-bind:key="item['title']">
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
                fontsize: 11px;
                overflow: hidden;
                text-overflow: ellipsis;
                maxHeight: 250px;
              "
              >{{ item["description"] }}</span
            >
            <div class="bottom">
              <el-button
                type="text"
                :style="{ color: '#E3242B' }"
                @click="removeFavBook(item['title'])"
                class="button"
                >Remove from Favourties</el-button
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
      arr: this.$store.state.favarr,
      render:this.$store.state.render,
    };
  },
  methods: {
      removeFavBook: function(title_s){
      const csrftoken = this.$cookie.getCookie("csrftoken");
      axios
        .post("http://127.0.0.1:8000/api/removefavourites/",
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
          //fetch the books again
        axios.get("http://127.0.0.1:8000/api/listfavorites/",{},
        {
        headers: {
            "X-CSRFToken": csrftoken,
            "Content-Type": "application/x-www-form-urlencoded",
        }
        })
        .then((response) => {
        this.$store.commit("favarr",response.data)
        this.arr = response.data
        })
        });

      }
  },
  mounted(){
    const csrftoken = this.$cookie.getCookie("csrftoken");
    axios.get("http://127.0.0.1:8000/api/listfavorites/",{},
    {
        headers: {
            "X-CSRFToken": csrftoken,
            "Content-Type": "application/x-www-form-urlencoded",
        }
    })
    .then((response) => {
        if(response.data != "Permission Denied"){
            this.$store.commit("favarr",response.data)
            this.arr = response.data
        }

    })
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

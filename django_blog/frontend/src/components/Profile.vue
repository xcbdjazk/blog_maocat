<template>
  <div id="profile">
    <div class="profile">
    <div class="image">
      <!--偷得自己在码云上的头像····-->
      <img src="https://avatar.gitee.com/uploads/68/1972268_xcbdja.png!avatar100?1550021108" alt="">
    </div>
    <div class="introduce">
      <span>{{ user.name }}</span>
      <p v-if="user.email">Email: {{ user.email }}</p>
      <p v-if="user.desc">{{ user.desc }}</p>
    </div>
    </div>
    <div class="tags">
      <template v-for="tag in tags">
        <span @click="toTagDetail(tag.name)" :style="get_high()">
          {{ tag.name }}
        </span>
      </template>
    </div>
  </div>
</template>

<script>
  import {getUserProfile} from '../api/user'
  import {getTags} from '../api/tag'
  export default {

    name: "profile",
    data() {
      return {
        user: {},
        tags:[]
      }
    },

    created() {
      getUserProfile().then(
        (data) => {
          this.user = data
        }
      )
      getTags().then(
        (data) => {
          this.tags = data
        }
      )
    },
    methods:{
        toTagDetail(tagName){
            this.$router.push({name:'tag', params:{tag: tagName}})

        },
      randomNum(minNum, maxNum) {
          switch (arguments.length) {
              case 1:
                  return parseInt(Math.random() * minNum + 1, 10);
              case 2:
                  return parseInt(Math.random() * ( maxNum - minNum + 1 ) + minNum, 10);
                  //或者 Math.floor(Math.random()*( maxNum - minNum + 1 ) + minNum );
              default:
                  return 0;

          }
      },
  get_high(){
            let num = this.randomNum(15,30)
          return {'text-decoration':'none',
                  "color":"black",
                  "display":"Inline ",
                  "font-size":`${num}px`,
                  "margin-left":"5px",
                  "margin-right":"5px"}
        }
    }
  }
</script>

<style scoped>
  .image, .introduce {
    margin: 0 auto;
    text-align: center;
  }

  .profile {
    background-color: #fff;
  }

  .introduce p {
    margin-top: 20px;
  }
  .tags{
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #fff;
  }
  .tags span:hover{
    color:red!important;
    cursor:pointer;
  }
</style>

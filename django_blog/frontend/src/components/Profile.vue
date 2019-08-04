<template>
  <div id="profile">
    <div class="image">
      <!--偷得自己在码云上的头像 嘻嘻····-->
      <img src="https://avatar.gitee.com/uploads/68/1972268_xcbdja.png!avatar100?1550021108" alt="">
    </div>
    <div class="introduce">
      <span>{{ user.name }}</span>
      <p v-if="user.desc">{{ user.desc }}啊啊啊</p>
    </div>
    <div class="tags">
      <template v-for="tag in tags">
        <!--<router-link>-->
          {{ tag.name }}
        <!--</router-link>-->
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
    }
  }
</script>

<style scoped>
  .image, .introduce {
    margin: 0 auto;
    text-align: center;
  }

  #profile {
    background-color: #fff;
  }
  p {
    font-family: Helvetica;
  }
  .introduce p {
    margin-top: 20px;
  }
  .tags{

  }
</style>

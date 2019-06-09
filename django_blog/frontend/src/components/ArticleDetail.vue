<template>
  <div>
    <bar></bar>
    123213
  </div>

</template>

<script>
  import {getArticles} from '../api/article'
  import Bar from './Bar'
  import Profile from './Profile'
  export default {
    name: 'Articles',
    data() {
      return {
        articles: []
      }
    },
    components:{
      bar:Bar,
      profile:Profile
    },



  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  hr {
    margin: 0 auto;
    width: 80%;
  }
  h4 {
    font-size: 30px;
  }
  .article {
    padding: 20px 30px;
  }
  .articles {
    max-width: 1000px;
    height: 2000px;
    border-bottom: 1px;
    /*border-top: 1px solid #2c3e50;*/
    margin: 0 auto;
    padding-top: 10px;
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
</style>

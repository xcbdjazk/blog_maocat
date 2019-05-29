<template>
  <div class="articles">
    <el-row :gutter="10">
      <el-col :xs="24" :sm="18" :md="18" :lg="18" :xl="18">
        <div class="grid-content bg-purple-light">
           <div v-for="(article, index) in articles" :key="index">
             {{ article.id }}
             {{ article.title }}
             {{ article.desc_txt }}
           </div>
         </div>
      </el-col>
      <el-col :xs="0" :sm="6" :md="6" :lg="6" :xl="6">
        <div class="grid-content bg-purple hidden-xs-only">

        </div>
      </el-col>

    </el-row>

  </div>
</template>

<script>
  import {getArticles} from '../api/article'

  export default {
    name: 'Articles',
    data() {
      return {
        articles: []
      }
    },
    created() {
      getArticles().then((data) => {
        this.articles = data
      })
    }


  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .articles {
    max-width: 1000px;
    border-bottom: 1px;
    margin: 0 auto;
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

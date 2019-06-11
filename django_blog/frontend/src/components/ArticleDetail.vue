<template>
  <div>
    <bar></bar>
    <div class="article">
      <el-row :gutter="10">
        <el-col :xs="24" :sm="18" :md="18" :lg="18" :xl="18">
          <div class="article-detail">
            <div class="article-title">
              <h4>{{article.title}}</h4>
            </div>
            <div class="article-desc">
              <span class="el-icon-user">MaoCat</span>

              <span class="el-icon-time">{{article.create_time | formatDate}}</span>
            </div>
            <div class="article-content" v-html="article.desc">

            </div>
          </div>
        </el-col>
        <el-col :xs="0" :sm="6" :md="6" :lg="6" :xl="6">
          <div class="hidden-xs-only">
            <profile></profile>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import {getArticleById} from '../api/article'
import Bar from './Bar'
import Profile from './Profile'
export default {
  name: 'Articles',
  data() {
    return {
      article: {}
    }
  },
  components:{
    bar:Bar,
    profile:Profile
  },
  created() {
    getArticleById(this.$route.params.id).then((data) => {
      this.article = data
    })
  },
  filters:{
  cutOutDesc(desc){
    return desc.length > 100?desc.substring(0, 100) + '...': desc
  },
  formatDate(datetime){
    let date = new Date(datetime)
    return `${date.getFullYear()}年${date.getMonth() + 1}月${date.getDate()}日`;

  }
}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  hr {
    margin: 0 auto;
    width: 80%;
  }
  h4 {
    font-size: 30px;
  }
  .article {
    max-width: 1000px;
    height: 2000px;
    border-bottom: 1px;
    /*border-top: 1px solid #2c3e50;*/
    margin: 0 auto;
    padding-top: 10px;
  }
  .article-detail{
    padding: 20px 10%;
  }
  .article-detail > div {
    margin-top: 20px;
  }
  .article-content{
    margin-top: 50px;
  }
</style>

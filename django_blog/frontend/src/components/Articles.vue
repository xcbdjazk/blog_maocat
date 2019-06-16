<template>
  <div>
    <bar></bar>
    <div class="articles">
      <el-row :gutter="10">
        <el-col :xs="24" :sm="18" :md="18" :lg="18" :xl="18">
          <div class="grid-content bg-purple-light">
            <div v-for="(article, index) in articles" :key="index">
              <div class="article">
                <div class="article-title">
                  <h4>
                    <router-link :to="{name:'detail',params:{id:article.id}}">
                      {{ article.title }}
                    </router-link>
                  </h4>
                </div>
                <!--{{ article.id }}-->
                <div class="article-desc">
                  <span class="el-icon-user">MaoCat</span>

                  <span class="el-icon-time">{{article.create_time | formatDate}}</span>
                </div>
                <div class="article-desc-txt">
                  {{ article.desc_txt | cutOutDesc }}
                </div>
                <div>
                  <router-link :to="{name:'detail',params:{id:article.id}}">
                    <el-button  class="el-icon-reading"> Continue reading →</el-button>
                  </router-link>
                </div>
                <div class="article-tag">
                  <span class="el-icon-s-flag">
                      <template v-for="tag in article.tag"> {{tag.name}} </template>
                  </span>
                </div>
              </div>
              <hr>
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

<script >
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
    created() {
      getArticles().then((data) => {
        this.articles = data
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
<style scoped>
  hr {
    border:0;
    background-color: #ebebeb;
    height:1px;
    margin: 0 auto;
    width: 80%;
  }
  h4 {
    font-size: 30px;
  }
  h4 a {
    color: #323e4e;
    text-decoration: none;
  }
  h4 a:hover {
    color: rgba(127, 255, 212, 0.66);
  }
  .article {
    padding: 20px 10%;
  }
  .articles {
    max-width: 1000px;
    border-bottom: 1px;
    margin: 0 auto;
    padding-top: 10px;
  }
  .article-desc-txt {
    margin: 20px 0;
    color: #323e4e;
    font-family: sans-serif;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .article > div{
    color: #323e4e;
    margin-top: 20px;
  }
  .article-desc > span, .article-tag > span{
    display: inline-block;
    margin-left: 10px;
    font-size: 14px;
  }
</style>

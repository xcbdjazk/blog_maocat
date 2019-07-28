<template>
  <div>
    <header>
      <bar></bar>
    </header>
      <el-row :gutter="10" id="body">
        <el-col :xs="24" :sm="18" :md="18" :lg="18" :xl="18">
          <section>
            <template v-for="article, index in articles">
              <article>
                <header class="article-title">
                  <h4>
                    <router-link :to="{name:'detail',params:{id:article.id}}">
                      {{ article.title }}
                    </router-link>
                  </h4>
                </header>
                <!--{{ article.id }}-->
                <nav>
                  <span class="el-icon-user">MaoCat</span>

                  <span class="el-icon-time">{{article.create_time | formatDate}}</span>
                </nav>
                <div class="article-desc">
                  {{ article.desc_txt | cutOutDesc }}
                </div>
                <div>
                  <router-link :to="{name:'detail', params:{id:article.id}}">
                    <el-button  class="el-icon-reading"> Continue reading →</el-button>
                  </router-link>
                </div>
                <footer class="article-tag">
                  <span class="el-icon-s-flag">
                      <template v-for="tag in article.tag"> {{tag.name}} </template>
                  </span>
                </footer>
                <br>
                <hr>
              </article>

            </template>
          </section>
        </el-col>
        <el-col :xs="0" :sm="6" :md="6" :lg="6" :xl="6" class="hidden-xs-only">
            <profile></profile>
        </el-col>
      </el-row>
    </div>
</template>

<script >
  import {getArticles} from '../api/article'
  import Bar from '../components/Bar'
  import Profile from '../components/Profile'
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
    font-size: 25px;
  }
  h4 a {
    color: #323e4e;
    text-decoration: none;
  }
  h4 a:hover {
    color: rgba(127, 255, 212, 0.66);
  }
  article {
    padding: 20px 10%;
  }
  #body {
    max-width: 1000px;
    border-bottom: 1px;
    margin: 0 auto!important;
    padding-top: 10px;
  }
  .article-desc {
    margin: 20px 0;
    color: #323e4e;
    font-family: sans-serif;
  }
  section {
    border-radius: 4px;
    min-height: 36px;
  }
  article > div{
    color: #323e4e;
    margin-top: 20px;
  }
  nav, footer{
    margin: 10px 0 ;
  }
  .nav > span, footer > span{
    display: inline-block;
    margin-left: 10px;
    font-size: 14px;
  }
</style>

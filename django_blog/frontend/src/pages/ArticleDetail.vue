<template>
  <div>
    <header>
      <bar></bar>
    </header>
      <el-row :gutter="10" id="body">
        <el-col :xs="24" :sm="18" :md="18" :lg="18" :xl="18">
          <article class="article-detail">
            <header class="article-title">
              <h2>{{article.title}}</h2>
            </header>
            <nav class="article-desc">
              <span class="el-icon-user">MaoCat</span>

              <span class="el-icon-time">{{article.create_time | formatDate}}</span>
            </nav>
            <div class="article-content" v-html="mark(article.desc)" v-highlight>
            </div>
          </article>
        </el-col>
        <el-col :xs="0" :sm="6" :md="6" :lg="6" :xl="6" class="hidden-xs-only">
            <profile></profile>
        </el-col>
      </el-row>
  </div>
</template>

<script>

  import showdown from 'showdown'
  import {getArticleById} from '../api/article'
  import Bar from '../components/Bar'
  import Profile from '../components/Profile'

  export default {
    name: 'Articles',
    data() {
      return {
        article: {}

      }
    },
    components: {
      bar: Bar,
      profile: Profile,
    },
    created() {
      getArticleById(this.$route.params.id).then((data) => {
        this.article = data
      })
    },
    methods:{
      mark(desc) {
        let converter = new showdown.Converter()
        return converter.makeHtml(desc)
      },
    },
    filters: {
      cutOutDesc(desc) {
        return desc.length > 100 ? desc.substring(0, 100) + '...' : desc
      },
      mark(desc) {
        let converter = new showdown.Converter()
        return converter.makeHtml(desc)
      },
      formatDate(datetime) {
        let date = new Date(datetime)
        return `${date.getFullYear()}年${date.getMonth() + 1}月${date.getDate()}日`;

      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #body {
    max-width: 1000px;
    border-bottom: 1px;
    margin: 0 auto!important;
    padding-top: 10px;
  }
  article {
    padding: 30px 40px;
  }
  .article-detail > div {
    margin-top: 20px;
  }
  nav {
    margin:15px 0 ;
  }
</style>

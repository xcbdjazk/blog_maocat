<template>
  <div id='detail'>
    <div class="lay-image hidden">
      <img src="" alt="" width="50%">
    </div>
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
              <ul>
                <li>
                  <span class="el-icon-user">MaoCat</span>
                </li>
                <li>
                  <span class="el-icon-time">{{article.create_time | formatDate}}</span>
                </li>
              </ul>

            </nav>
            <div class="article-content" v-html="mark(article.desc)" v-highlight v-imgBig>
            </div>
          </article>
        </el-col>
        <el-col :xs="0" :sm="6" :md="6" :lg="6" :xl="6" class="hidden-xs-only">
            <profile></profile>
        </el-col>
      </el-row>
      <goback></goback>
  </div>
</template>

<script>

  import showdown from 'showdown'
  import {getArticleById} from '../api/article'
  import Bar from '../components/Bar'
  import Profile from '../components/Profile'
  import GoBack from '../components/GoBack'

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
      goback: GoBack,
    },
    created() {
      getArticleById(this.$route.params.id).then((data) => {
        this.article = data

      })
    },
    watch:{
      article(newVal, oldVal){
        document.title = this.article.title
      }
    },
    methods:{
      mark(desc) {
        let converter = new showdown.Converter()
        return converter.makeHtml(desc)
      },
    },
    mounted(){
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
    },
    directives:{
        imgBig:{
          componentUpdated:(el)=>{
            var objs = el.querySelectorAll(".article-detail img");
            var layImg = document.querySelector('.lay-image');
            var Img = document.querySelector('.lay-image img');

            layImg.onclick=function () {
              this.className='lay-image hidden'
            }

            for(var i=0;i<objs.length;i++)
            {
              objs[i].onclick = function(){
                let width = 0
                layImg.className='lay-image'
                Img.style.width = `${width}%`
                Img.src=this.src
                if(window.innerWidth > 700){
                  let Intervalid = setInterval(()=>{
                  width += 5
                  Img.style.width = `${width}%`
                  if(width === 50){
                    clearInterval(Intervalid)
                  }
                },20)
                }else{
                  Img.style.left = 0
                  let Intervalid = setInterval(()=>{
                  width += 5
                  Img.style.width = `${width}%`
                  if(width === 100){
                    clearInterval(Intervalid)
                  }
                },10)
                }


              }

              objs[i].style.cursor = "pointer";
            }
        }
        }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
 #detail {
    background-color: rgb(241, 241, 241);
   min-height: 80vh;

  }
  #body {
    max-width: 1000px;
    min-height: 100vh;

    border-bottom: 1px;
    margin: 0 auto!important;
    padding-top: 10px;
  }
  article {
    background-color: #fff;
    padding: 30px 40px;
    min-height: 80vh;

  }
  .article-detail > div {
    margin-top: 20px;
  }
  nav {
    margin:15px 0 ;
  }
  nav li {
    display: inline-block;
    margin-right: 15px;
  }
  .hidden {
    display: none;
  }
  .lay-image{
    position: fixed;
    z-index: 99999;
    background-color: rgba(46, 46, 46, 0.61);
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
  }
  .lay-image img {
    position: absolute;
    left: 25vw;
    top: 50vh;
    transform: translateY(-50%)

  }
</style>

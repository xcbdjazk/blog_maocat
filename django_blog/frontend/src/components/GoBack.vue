<template>
  <div>
    <div class="el-icon-s-home home" @click="home()" v-imgRight v-show="this.$route.path !== '/'"></div>
    <div class="top el-icon-top" @click="backTop()" v-imgRight v-show="scrollTop!==0"></div>
  </div>
</template>

<script>
    export default {
        name: "GoBack",
        data(){
            return {
                timer:null,
                scrollTop:0,
                doscrolled:false
            }
        },
        mounted () {

            window.addEventListener('scroll', this.scrollToTop)
        },
        destroyed () {
            window.removeEventListener('scroll', this.scrollToTop)
        },
        methods: {
            home(){
                this.$router.push('/')
            },
            // 点击图片回到顶部方法，加计时器是为了过渡顺滑
            backTop () {
                if(this.timer){
                    clearInterval(this.timer)
                    this.timer=''
                }
                this.doscrolled = true
                this.timer = setInterval(() => {
                    let ispeed = Math.floor(-this.scrollTop / 5)
                    document.documentElement.scrollTop = document.body.scrollTop = this.scrollTop + ispeed
                    if (this.scrollTop === 0) {
                        clearInterval(this.timer)
                        this.doscrolled = false
                    }
                }, 16)
            },
            scrollToTop () {
                let now_top =  window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
                if(this.scrollTop < now_top){
                    clearInterval(this.timer)
                    this.timer=''
                }
                this.scrollTop = now_top

        }},

        directives:{
        imgRight:{
            bind(el){
                if(window.innerWidth < 700){
                    el.style.right = "10%"
                    el.style.fontSize = "20px"
                }
            }
        }
    }

    }
</script>

<style scoped>
  .home,.top{
    width: 20px;
    height: 35px;
    position:fixed;
    line-height: 35px;
    right:30%;
    text-align: center;
    font-size: 30px;
    border-radius: 50%;
    cursor:pointer;
    -webkit-user-select:none;
    -moz-user-select:none;
    -ms-user-select:none;
    user-select:none;
    -webkit-tap-highlight-color: rgba(0,0,0,0)
  }
  .home {
    bottom: 30px;
  }
  .top {
    bottom: 60px;
  }
</style>

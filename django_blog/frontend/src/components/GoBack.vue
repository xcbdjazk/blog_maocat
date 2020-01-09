<template>
  <div>
    <div class="el-icon-s-home home" @click="home()"></div>
    <div class="top el-icon-top" @click="backTop()"></div>
  </div>
</template>

<script>
    export default {
        name: "GoBack",

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
                const that = this
                let timer = setInterval(() => {
                    let ispeed = Math.floor(-that.scrollTop / 5)
                    document.documentElement.scrollTop = document.body.scrollTop = that.scrollTop + ispeed
                    if (that.scrollTop === 0) {
                        clearInterval(timer)
                    }
                }, 16)
            },

            // 为了计算距离顶部的高度，当高度大于60显示回顶部图标，小于60则隐藏
            scrollToTop () {
                const that = this
                let scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
                that.scrollTop = scrollTop
                if (that.scrollTop > 60) {
                    that.btnFlag = true
                } else {
                    that.btnFlag = false
                }
            }
        }

    }
</script>

<style scoped>
  .home,.top{
    width: 35px;
    height: 35px;
    position:fixed;
    line-height: 35px;
    right:30%;
    text-align: center;
    font-size: 30px;
    background-color: #fdfdfd;
    border-radius: 50%;
    cursor:pointer
  }
  .home {
    bottom: 100px;
  }
  .top {
    bottom: 150px;
  }
</style>

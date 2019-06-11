<template>
  <div>
    <div class="progress-bar" id="bar" style="height: 2px;background-color: #000;position: fixed;z-index: 1999">
    </div>

  </div>
</template>

<script>
    export default {
        name: "bar",
      data(){
          return {
            scroll:0,
            window:window,
            document:document
          }
      },
      mounted() {
//监听页面滚动事件
        window.addEventListener('scroll', this.barScroll)
//注意：如果由于自己的vue中的样式导致监听不到，可以尝试监听body或者'#app-root'的滚动事件
      },
      watch:{
        scroll(newVal,oldVal) {
          document.getElementById('bar').style['width'] = `${newVal}%`;
        }
      },
      methods:{
        barScroll:function(event){
          // 滚动条的位置
          let scrollHeight = this.getScrollTop()//原生兼容
          // window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
          let windowHeight = this.getWindowHeight()
          let documentHeight = this.getScrollHeight()
          this.scroll = parseFloat(scrollHeight / (documentHeight-windowHeight)*100).toFixed(2)
        },
        getScrollTop:function (){
          var scrollTop = 0, bodyScrollTop = 0, documentScrollTop = 0;
          if(document.body){
            bodyScrollTop = document.body.scrollTop;
          }
          if(document.documentElement){
            documentScrollTop = document.documentElement.scrollTop;
          }
          scrollTop = (bodyScrollTop - documentScrollTop > 0) ? bodyScrollTop : documentScrollTop;
          return scrollTop;
        },

        //文档的总高度

        getScrollHeight:function (){
          var scrollHeight = 0, bodyScrollHeight = 0, documentScrollHeight = 0;
          if(document.body){
            bodyScrollHeight = document.body.scrollHeight;
          }
          if(document.documentElement){
            documentScrollHeight = document.documentElement.scrollHeight;
          }
          scrollHeight = (bodyScrollHeight - documentScrollHeight > 0) ? bodyScrollHeight : documentScrollHeight;
          return scrollHeight;
        },

        //浏览器视口的高度

        getWindowHeight:function (){
          var windowHeight = 0;
          if(document.compatMode == "CSS1Compat"){
            windowHeight = document.documentElement.clientHeight;
          }else{
            windowHeight = document.body.clientHeight;
          }
          return windowHeight;
        }
      },
      destroyed () {
        window.removeEventListener('scroll', this.barScroll)
      }
    }
</script>

<style scoped>

</style>

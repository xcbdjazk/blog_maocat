import Vue from 'vue'
import Articles from '@/components/Articles';
import ArticleDetail from '@/components/ArticleDetail';
import VueRouter from "vue-router";
import Router from "vue-router";
Vue.use(Router)

let router = new VueRouter(
  {
    routes:[{path : "/" ,name:'base', component:Articles, meta:{title:'blog in maocat'}},
      {path : "/:id" ,name:'detail', component:ArticleDetail, meta:{title:'blog in maocat'}},]
}

)

router.beforeEach((to, from, next)=>{
  if (to.meta.title){
    document.title = to.meta.title
  }
  next();
})
export default router

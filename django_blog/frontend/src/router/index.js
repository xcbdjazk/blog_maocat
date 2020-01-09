import Vue from 'vue'
import Articles from '@/pages/Articles';
import ArticleDetail from '@/pages/ArticleDetail';
import VueRouter from "vue-router";
import Router from "vue-router";
Vue.use(Router)

let router = new VueRouter(
  {
    routes:[{path : "/" ,name:'base', component:Articles, meta:{title:'blog in maocat'}},
      {path : "/:id" ,name:'detail', component:ArticleDetail, meta:{title:'blog in maocat'}},
      {path : "/tag/:tag" ,name:'tag', component:Articles, meta:{title:'blog in maocat'}},
    ]
}

)

// router.beforeEach((to, from, next)=>{
//   if (to.meta.title){
//     document.title = to.meta.title
//   }
//   next();
// })
export default router

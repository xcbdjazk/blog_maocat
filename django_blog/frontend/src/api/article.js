import request from '../utils/request'


function getArticles(){
  return request.get('/articles/')
}

function getArticleById(id){
  return request.get(`/article/${id}`)
}
export {
  getArticles,
  getArticleById
}
// or
/*
* export {
*    getArticles
* }
*
* */

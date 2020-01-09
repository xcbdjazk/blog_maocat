import request from '../utils/request'


function getArticles(tag,page=1){
  return request.get('/articles/',{
    params: {
      'size': 10,
      tag,
     page
    }
  })
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

import request from '../utils/request'


export function getArticles(){
  return request.get('/articls/')
}

// or
/*
* export {
*    getArticles
* }
*
* */

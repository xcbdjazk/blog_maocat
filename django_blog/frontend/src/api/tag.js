import request from '../utils/request'

function getTags() {
  return request.get('/tags')
}

export {
  getTags
}

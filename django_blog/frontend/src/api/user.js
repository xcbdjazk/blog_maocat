import request from '../utils/request'

function getUserProfile() {
  return request.get('/user/profile')
}

export {
  getUserProfile
}

import axios from 'axios'

let service = axios.create(
  {
    baseURL:'http://127.0.0.1:8000/api',
    timeout: 50000
  }
)

//request 拦截器
service.interceptors.request.use(config => {
  return config
}, error => {
})

// respone拦截器
service.interceptors.response.use(
  response => {
    return response.data
  },
  error => {
    if (error.response.status === 401) {
    } else if (error.response.status === 422) {
    } else if (error.response.status === 404) {
    } else {
    }
    return Promise.reject(error)
  }
)

export default service


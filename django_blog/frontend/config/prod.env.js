'use strict'

const DJANGO_CONFIG_ENV = process.env.DJANGO_CONFIG

var DEVELOP_CONFIG = {
  API_HOST: '"http://127.0.0.1/api"',
  STATIC_HOST: '/'
}
var DJ_CONFIG = {
  API_HOST: '"http://maocatooo.cn/api"',
  STATIC_HOST: 'http://upload.maocatooo.cn/frontend/'
}
let web_config = DEVELOP_CONFIG

if (DJANGO_CONFIG_ENV === 'DEV') {
  web_config = DJ_CONFIG
}
module.exports = {
  NODE_ENV: '"production"',
  API_HOST: web_config.API_HOST,
  STATIC_HOST: web_config.STATIC_HOST
}

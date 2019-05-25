# django_blog

flask实在太熟悉了,想着使用django CBV 开发一套,以前学习过,现在加深加深

 记得要在utils/qiniu_conf.py 填写七牛的AK, SK
 
一些脚本

`python manage.py startapp api` 新建app

数据库迁移/创建

`python manage.py makemigrations backend`

`python manage.py migrate`

创建 vue frontend

`vue init webpack frontend`
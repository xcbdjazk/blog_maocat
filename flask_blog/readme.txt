#创建后台管理员
python manager.py create admin -u xxx  -m xxxxx -p xxx -e xxx
("-u", "--username", dest="username") len gte 6
("-m", "--mobile", dest="mobile")  len is 11
("-p", "--password", dest="password") len gte 6
("-e", "--email", dest="email") email
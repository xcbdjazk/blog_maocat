from app.blog import current_app as blog_app1
from app.other import current_app as blog_other1
from flask_script import Manager,Server,Shell
from flask import Flask
blog_app = blog_app1()
blog_manager = Manager(blog_app)
blog_manager.add_command("runserver",Server(host="0.0.0.0",port=5001) )

blog_other = blog_other1()
other_manager = Manager(blog_other)
other_manager.add_command("runserver",Server(host="0.0.0.0",port=5002) )

app = blog_app1()
def make_shell_context():
    return dict(app=app)
manager = Manager(app)
manager.add_command("blog", blog_manager)
manager.add_command("other", other_manager)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(host='0.0.0.0'))
if __name__ == "__main__":
    manager.run()
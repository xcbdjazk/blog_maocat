from app import blog
from app import other
from flask_script import Manager, Server,Shell
from script.command import SubServer
from script.other import CreateAdministrators
blog_app = blog.current_app()
blog_manager = Manager(blog_app)
blog_manager.add_command("runserver", SubServer(blog_app, host="0.0.0.0",port=5001) )

blog_other = other.current_app()
other_manager = Manager(blog_other)
other_manager.add_command("runserver", SubServer(blog_other, host="0.0.0.0",port=5002) )

app = blog.current_app()


def make_shell_context():
    return dict(app=app)


manager = Manager(app)
manager.add_command("blog", blog_manager)
manager.add_command("createadmin", CreateAdministrators())
manager.add_command("other", other_manager)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(host='0.0.0.0'))
if __name__ == "__main__":
    manager.run()
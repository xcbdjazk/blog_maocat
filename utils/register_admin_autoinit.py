# -*- coding:utf8 -*-
from config import config
from models.blog.blog import *
from models.user import LoginPattern


def register_endpoint(app):
    @app.before_first_request
    def update_action_url():
        login_patt = LoginPattern.objects.first()
        if not login_patt:
            login_patt = LoginPattern() #导入登录方式
            login_patt.save()
        endpoints = app.url_map.iter_rules()
        navigations = NavigationBlog.objects.all()
        nav_end = [nav.endpoint for nav in navigations]
        app_end = []
        if navigations:
            for endpoint in endpoints:
                for i in config.endpoint:
                    if endpoint.endpoint.find(i) == 0:
                        break
                else:
                    app_end.append(endpoint.endpoint)
                    navigation = NavigationBlog.objects(endpoint=endpoint.endpoint,url=endpoint.rule).first()
                    if navigation:
                        pass
                    else:
                        navig = NavigationBlog()
                        navig.name = endpoint.rule
                        navig.url = endpoint.rule
                        navig.endpoint = endpoint.endpoint
                        navig.save()
            old_endpoints = [i for i in nav_end if i not in app_end]
            for old_endpoint in old_endpoints:
                print "=====delete old endpoint=====", old_endpoint
                old_navigation = NavigationBlog.objects(endpoint=old_endpoint).first()
                old_navigation.delete()

        else:
            for endpoint in endpoints:
                for i in config.endpoint:
                    if endpoint.endpoint.find(i) == 0:
                        break
                else:
                    print("===first add navigation===")
                    navig = NavigationBlog()
                    navig.name = endpoint.rule
                    navig.url = endpoint.rule
                    navig.endpoint = endpoint.endpoint
                    navig.save()






if __name__ == "__main__":
    for i in [1,2,3,4,5]:
        if i == 6:
            break
    else:
        print("sb")
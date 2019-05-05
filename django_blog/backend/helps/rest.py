from django.http import JsonResponse

__all__ = ['success',
           'unauth_error',
           'params_error',
           'server_error',
           ]


class HttpCode(object):
    ok = 200
    un_auth_error = 401
    params_error = 400
    server_error = 500


def restful_result(code, message, data):
    """所有json返回的base"""
    return JsonResponse({"code": code, "message": message, "data": data})


def success(message="", data=None):
    """code:200,成功返回数据"""
    return restful_result(code=HttpCode.ok, message=message, data=data)


def unauth_error(message=""):
    """code:401,没有权限or未登录or未认证"""
    return restful_result(
        code=HttpCode.un_auth_error,
        message=message,
        data=None)


def params_error(message=""):
    """code:400,参数错误"""
    return restful_result(
        code=HttpCode.params_error,
        message=message,
        data=None)


def server_error(message=""):
    """code:500,服务器error"""
    return restful_result(
        code=HttpCode.server_error,
        message=message,
        data=None)
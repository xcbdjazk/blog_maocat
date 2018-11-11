from flask import jsonify

__all__ = ["success", "unauth_error", 'params_error', 'server_error']


class HttpCode(object):
    ok =200
    unauth_error = 401
    params_error = 400
    server_error = 500


def restful_result(code,message,data):
    return jsonify({"code":code,"message":message,"data":data})


def success(message="", data=None):
    return restful_result(HttpCode.ok, message, data)


def unauth_error(message="", data=None):
    return restful_result(HttpCode.unauth_error, message, data)


def params_error(message="", data=None):
    return restful_result(HttpCode.params_error, message, data)


def server_error(message="", data=None):
    return restful_result(HttpCode.server_error, message, data)
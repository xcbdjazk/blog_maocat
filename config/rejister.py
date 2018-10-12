
__all__ = ['register_jinja']


def register_jinja(app, has_menu=False):
    result = {}

    def menus():
        return ""

    def permission(endpoint):

        return ""

    result['static'] = static
    result['enumerate'] = enumerate
    result['len'] = len
    show_anaytics_script = True
    if app.debug or app.testing:
        show_anaytics_script = False
    result['show_anaytics_script'] = show_anaytics_script
    if has_menu:
        result['permission'] = permission
        result['menus'] = menus

    @app.context_processor
    def register_context():
        return result


def static(filename, is_default=False):
    pass
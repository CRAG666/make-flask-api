from routes.api_template import MethodsApi


def create_routes(**kwargs):
    view_func = MethodsApi.as_view(
        f"{kwargs.get('noun')}_api",
        kwargs.get('table'),
        kwargs.get('table_schema'),
        kwargs.get('customize_login')
    )

    endpoints = kwargs.get(
        'endpoints',
        get_endpoints(
            kwargs.get('noun'),
            kwargs.get('login_endpoint', False)))

    for i in endpoints:
        kwargs.get('blueprint').add_url_rule(
            i[0],
            methods=i[1],
            view_func=view_func)


def get_endpoints(noun: str, login: bool) -> list:
    endpoint_list = [
        [f'/api/{noun}/', ['POST', 'GET']],
        [f'/api/{noun}/<int:id>', ['GET', 'PUT', 'DELETE']]]
    if login:
        endpoint_list.insert(0, [f'/api/{noun}/login', ['POST']])
    return endpoint_list

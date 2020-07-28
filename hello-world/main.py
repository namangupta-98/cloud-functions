def hello_world(request):
    request_args = request.args
    request_json = request.get_json(silent=True)
    if request_args and 'name' in request_args and request_args and 'last_name' in request_args:
        name = request_args['name']
        last_name = request_args['last_name']
    elif request_json and 'name' in request_json and request_json and 'last_name' in request_json:
        name = request_json['name']
        last_name = request_json['last_name']
    else:
        name = 'Bruce'
        last_name = 'Wayne'

    return f'Hello {name} {last_name}'
def application(environ,start_response):
    start_response('200 ok',[('content-type','text/html')])
    return [b'<h1>hello,web</h1>']
#!/usr/bin/python
#coding=utf-8  

#from flup.server.fcgi import WSGIServer  
  
#def naiveloafer_app(environ, start_response):  
#    start_response('200 OK', [('Content-Type', 'text/plain')])  
#    content = "Hello World!chenyun"  
#    return [content]  
  
#if __name__  == '__main__':  
#   WSGIServer(naiveloafer_app).run()


def myapp(environ, start_response):
    r = ''
    for x in environ:
        r+="%s\t%s\n" % (x, environ[x])
    print r
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello World!\n']
 
if __name__ == '__main__':
    from flup.server.fcgi import WSGIServer
    WSGIServer(myapp).run()


"""from django.shortcuts import render
from django.http import HttpResponse
def main(request):
    html = "<html><body><table><tr><td border='1'>hello world</td></tr></table><body></html>"
    <!doctype html><html lang=¥"en¥"><head><meta charset=¥"utf-8¥"><title>jQuery UI Draggable - Default functionality</title><link rel=¥"stylesheet¥" href=¥"//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css¥"><script src=¥"//code.jquery.com/jquery-1.10.2.js¥"></script><script src=¥"//code.jquery.com/ui/1.11.4/jquery-ui.js¥"></script><link rel="stylesheet¥" href=¥"/resources/demos/style.css¥"><style></style><script>$(function() {$( ¥"#draggable¥" ).draggable();});</script></head><body><div id=¥"draggable¥" class=¥"ui-widget-content¥">  <p>Drag me around</p></div></body></html>
    return HttpResponse(html)
# Create your views here.
"""
from django.http import HttpResponse, HttpRequest
from django.template import loader, RequestContext
import subprocess

def main(req):
    contexts = RequestContext(req, {
        'title' : 'hello django!',
        'test11' : 'tenant1' ,
        'test12' : 'tenant2' ,
        'test13' : 'tenant3' ,
        'test14' : 'tenant4' ,
        'test21' : '1' ,
        'test22' : '2' ,
        'test23' : '3' ,
        'test24' : '4' ,
        'test211' : 'tenant_id1' ,
        'test221' : 'tenant_id2' ,
        'test231' : 'tenant_id3' ,
        'test241' : 'tenant_id4' ,
    })
    template = loader.get_template('test2/test.html')
    return HttpResponse(template.render(contexts))


def send(req):
    com = 'export OS_AUTH_URL="http://localhost:35357/v2.0" && export OS_USERNAME="admin" && export OS_PASSWORD="admin" && export OS_TENANT_NAME="admin" && '

    com = com + req.GET['command']
    print(com)
    result = subprocess.Popen(com, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    """
    print('result stdout:' + str(result.stdout.readlines()))
    print('result stderr:' + str(result.stderr.readlines()))
    """

    print(req.GET['tenant_id'])

    contexts = RequestContext(req, {
        'title' : 'result test!',
        'result1' : str(result.stdout.readlines()),
    })
    template = loader.get_template('test2/res.html')
    return HttpResponse(template.render(contexts))

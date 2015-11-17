from django.http import HttpResponse, HttpRequest
from django.template import loader, RequestContext
import subprocess
import pprint
import requests

def main(req):

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



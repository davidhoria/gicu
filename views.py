from django.http import Http404, HttpResponse
from django.template import Template, Context
from django.views.decorators.csrf import csrf_protect
import datetime

@csrf_protect
def informatii(request):
    fp = open('e:/_work/python/p1/gicu/web/informatii.html')
    t = Template(fp.read())
    fp.close()
    if "ECODBARE" in request.session:
        request.session["EDESCRIERE"]="ECODBARE"
        c = RequestContext(request, {request.session})
    else:
        request.session["EDESCRIERE"]="blabla"
        c = Context({request.session})
    html = t.render(c)
    return HttpResponse(html)


def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()

    if "count" in request.session:
        request.session["count"]=int(request.session["count"])+1
    else:
        request.session["count"]=1
    html = ":"+str(request.session["count"])+":"
    html = html + "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        a = "22"
#        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
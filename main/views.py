from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Url
import nanoid
# Create your views here.


def index(request):
    linkId = nanoid.generate("qwertyuiopasdfghjklzxcvbnm", 6)
    if request.method == "POST":
        try:
            url = request.POST.get("url")
            shorelink = Url(slug=linkId, site=url)
            shorelink.save()
            return render(request, "main/index.html", {"link": shorelink})
        except Exception:
            return render(request, "main/index.html", {"error": "slug has been used"})

    else:
        return render(request, "main/index.html", {})


def findLink(request, slug):
    try:
        url = Url.objects.get(slug=slug)
        print(slug)
        return HttpResponseRedirect(url.site)

    except Exception:
        return render(request, "main/index.html", {})

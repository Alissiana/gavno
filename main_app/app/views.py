from django.core.files.storage import FileSystemStorage
from .predictor import prep_img, predict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def simple_upload_html(request):
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        preped = prep_img(filename)
        pred = predict(preped)
        return HttpResponse(pred[0])

@csrf_exempt
def simple_upload_json(request):
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        preped = prep_img(filename)
        pred = predict(preped)
        return JsonResponse(pred[1])



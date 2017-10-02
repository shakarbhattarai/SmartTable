from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ResturantInfo .models import ResturantInfo
from ResturantInfo.serializers import ResturantSerializer

def ResturantLists(request):
    """
    List all code snippets, or create a new snippet.
    """


    if request.method == 'GET':
        resturants = ResturantInfo.objects.all()
        serializer = ResturantSerializer(resturants, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ResturantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def Resturant_Details(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """


    try:

        resturants = ResturantInfo.objects.get(pk=pk)
    except ResturantInfo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ResturantSerializer(resturants)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ResturantSerializer(resturants, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        resturants.delete()
        return HttpResponse(status=204)
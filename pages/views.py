from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from rest_framework.response import Response
from .models import RoadSignType, RoadSign
from .serializers import RoadSignTypeSerializer, RoadSignSerializer

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)

    return Response({'token': token.key},
                    status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
def create_type(request):
    name = request.data.get("name")
    description = request.data.get("description")

    type = RoadSignType.objects.create(name=name, description=description)
    serializer = RoadSignTypeSerializer(type)
    response = {'success': True, 'result' : serializer.data}

    return Response(response, status=HTTP_201_CREATED)

@csrf_exempt
@api_view(["GET"])
def get_type_by_id(request, type_id):
    try:
        type = RoadSignType.objects.get(id=type_id)

        serializer = RoadSignTypeSerializer(type)
        response = {"result": serializer.data}
    except:
        response = {"result": None}

    return Response(response)

@csrf_exempt
@api_view(["GET"])
def get_types(request):
    types = RoadSignType.objects.all()

    serialized_types = []
    for sign_type in types:
       serialized_types.append(RoadSignTypeSerializer(sign_type).data)

    return Response({"result": serialized_types})


@csrf_exempt
@api_view(["POST"])
def create_sign(request):
    id = request.data.get("id")
    name = request.data.get("name")
    description = request.data.get("description")
    important_info = request.data.get("important_info")
    type = request.data.get("type")
    type = RoadSignType.objects.get(name=type)

    sign = RoadSign.objects.create(id=id, 
                                   name=name, 
                                   description=description, 
                                   important_info=important_info, 
                                   type_id=type.id)

    serializer = RoadSignSerializer(sign)
    response = {'success': True, 'result' : serializer.data}

    return Response(response, status=HTTP_201_CREATED)

@csrf_exempt
@api_view(["GET"])
def get_sign_by_id(request, sign_id):
    try:
        sign = RoadSign.objects.get(id=sign_id)
        type = RoadSignType.objects.get(id=sign.type_id)
        sign.type_id = type.name

        serializer = RoadSignSerializer(sign)
        response = {"result": serializer.data}
    except:
        response = {"result": None}

    return Response(response)

@csrf_exempt
@api_view(["GET"])
def get_signs(request):
    signs = RoadSign.objects.all()

    serialized_signs = []
    for sign in signs:
       type = RoadSignType.objects.get(id=sign.type_id)
       sign.type_id = type.name
       serialized_signs.append(RoadSignSerializer(sign).data)

    return Response({"result": serialized_signs})

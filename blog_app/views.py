from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Blog, Keywords
from .serializer import BlogSerializer, KeywordsSerializer
import json
from django.core import serializers

# -----------------------
# ListBlog
# -----------------------

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def ListPubs(request):
    """
        ----------------------------------------------------------------
        Name: ListPub - API lista todas as publicações
        Método: GET
        Descrição: Essa API lista todas as publicações inseridas no blog
        Autor: Marcelo Maccaferri
        Data: 19-10-2021
        ----------------------------------------------------------------
    """

    postagens = Blog.objects.all()
    serializer = BlogSerializer(postagens, many=True)

    return Response(serializer.data)


# -----------------------
# InsertPubKeys
# -----------------------

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def InsertPubKeys(request):
    """
        ----------------------------------------------------------------
        Name: InsertPubKeys - API insere publicação
        Método: POST
        Descrição: Essa API insere uma publicação no cadastro do blog e
                    inclui ao mesmo ao mesmo tempo palavras chave do texto
        Autor: Marcelo Maccaferri
        Data: 19-10-2021
        ----------------------------------------------------------------
    """

    try:

        data = request.data
        key_request = data.pop('keyword_set', "")

        serializer_pub = BlogSerializer(data=request.data)

        if serializer_pub.is_valid():

            id_pub = serializer_pub.save()

            if key_request != "":

                for key in key_request:

                    serializer_keys = KeywordsSerializer(data={
                        "id_pub": int(id_pub.id),
                        "keyword": key["name"]
                    })

                    if serializer_keys.is_valid():
                        serializer_keys.save()

            return Response(data, status=status.HTTP_201_CREATED)

    except Exception as e:
        print(e)
        return Response({"msg": 'erro'}, status=status.HTTP_400_BAD_REQUEST)


# -----------------------
# DeleteBlog
# -----------------------

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def DeletePub(request, pk):
    """
        ----------------------------------------------------------------
        Name: DeletePub - API delete publicação
        Método: POST
        Descrição: Essa API deleta uma publicação no cadastro a partir do id da publicação
        Autor: Marcelo Maccaferri
        Data: 19-10-2021
        ----------------------------------------------------------------
    """

    try:
        pub = Blog.objects.get(pk=pk)
        pub.delete()

        return Response({"msg": "pk"}, status=status.HTTP_201_CREATED)

    except:
        return Response({"msg": "erro"}, status=status.HTTP_400_BAD_REQUEST)

        return HttpResponseRedirect(reverse('pages_list'))


# -----------------------
# getBlog
# -----------------------

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def getPubID(request):
    """
        ----------------------------------------------------------------
        Name: getPubID - API get publicação ID
        Método: GET
        Descrição: Essa API recupera a publicação através do ID
        Autor: Marcelo Maccaferri
        Data: 19-10-2021
        ----------------------------------------------------------------
    """

    id = request.query_params.get('id')

    try:
        pub = Blog.objects.get(id=id)
        serializer = BlogSerializer(pub)
        data_pub = serializer.data

        key = Keywords.objects.filter(id_pub=id)
        # data_key = serializer_key.data

        data_list = []

        for k in key:
            serializer_key = KeywordsSerializer(k)
            data_key = serializer_key.data
            data_list.append({"name": data_key["keyword"]})

        data_pub["keyword_set"] = data_list

        return Response(data_pub, status=status.HTTP_201_CREATED)

    except Blog.DoesNotExist:
        pub = None
        return Response({"msg": "nao encontrado"}, status=status.HTTP_400_BAD_REQUEST)


# -----------------------
# index
# -----------------------

def index(request):
    return render(request, 'index.html')

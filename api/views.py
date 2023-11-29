from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework import serializers, status
from .customeResponse import ApiResponse


# Create your views here.
@api_view(['GET'])
def ApiOverView(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_item(request):
    item = ItemSerializer(data=request.data)

    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('item already exists')
    if item.is_valid():
        item.save()
        return ApiResponse('Item saved', item.data, status.HTTP_201_CREATED)
    else:
        return ApiResponse('somethin went wrong', [], status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_items(request):

    if request.query_params:
        items = Item.objects.filter(**request.query_params.dict())
    else:
        items = Item.objects.all()

    if items:
        serializer = ItemSerializer(items, many=True)
        return ApiResponse('items fetuched', serializer.data)

    else:
        return ApiResponse('no item was found', [], status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_item(request, pk):
    item = Item.objects.get(pk=pk)
    data = ItemSerializer(data=request.data)

    if data.is_valid():
        data.save()
        return ApiResponse("Item successfully updated", data.data, status.HTTP_200_OK)
    else:
        return ApiResponse("Something wenth wrong", None, status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return ApiResponse("Item succesfully deleted", None, status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def get_by_id(request, pk):
    try:
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item)  # Serialize the item object
        return ApiResponse('Item fetched', serializer.data, status=status.HTTP_200_OK)
    except Item.DoesNotExist:
        return ApiResponse(f'Item not found with id: {pk}', None, status=status.HTTP_404_NOT_FOUND)

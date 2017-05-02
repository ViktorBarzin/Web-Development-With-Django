from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, GenericAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from website.models import Offer, Category
from .serializers import OfferSerializer, CategorySerializer


class ListOffersView(APIView):
    def get(self, request):
        data = [OfferSerializer(x).data for x in Offer.objects.all()]
        return Response(data=data)

    def post(self, request):
        serializer = OfferSerializer(data=request.POST)

        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            status = 201
        else:
            status = 400
        return Response(data=serializer.data, status=status)


class OfferDetailView(APIView):
    def get(self, request, pk):
        offer = get_object_or_404(Offer, pk=pk)
        serializer = OfferSerializer(offer)
        return Response(data=serializer.data)

    def patch(self, request, pk):
        offer = get_object_or_404(Offer, pk=pk)
        data = request.data
        serializer = OfferSerializer(data=data, partial=True)
        if serializer.is_valid():
            serializer.update(offer, serializer.validated_data)
        return Response(request.data)

    # If it works, it's fine
    def put(self, request, pk):
        return self.patch(request, pk)

    def delete(self, request, pk):
        # Need some sort of authorization to prevent deleting other authors' offers
        offer = get_object_or_404(Offer, pk=pk)
        offer.delete()
        return Response(status=202)


class ListCategoriesView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveModelMixin,
                         UpdateModelMixin,
                         DestroyModelMixin,
                         GenericAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request)

    def patch(self, request, pk):
        return self.partial_update(request)

    def delete(self, request, pk):
        return self.destroy(request)

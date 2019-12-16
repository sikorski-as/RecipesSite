from django.shortcuts import render
from rest_framework import status, filters
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from Recipes.models import Recipe, Ingredient, Category, Comment, Rating, User
from Recipes.serializer import RecipeSerializer, IngredientSerializer, CategorySerializer, CommentSerializer, \
    RatingSerializer, UserSerializer


class IndexView(APIView):

    def get(self, request):
        list_of_urls = ['recipes', 'recipes/<int:pk>', 'ingredients', 'categories', 'ratings', 'comments', 'users']
        return Response(list_of_urls, status=status.HTTP_200_OK)


class AllRecipes(ListAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    # def get(self, request, pk, format=None):
    #     try:
    #         recipe = Recipe.objects.get(pk=pk)
    #         serializer = RecipeSerializer(recipe)
    #         return Response(serializer.data)
    #     except:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)


class IngredientsView(ListAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name']

    def post(self, request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IngredientView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class CategoriesView(ListAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['^name']

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentsView(ListAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RatingsView(ListAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializer

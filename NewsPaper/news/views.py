from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import *


class PostList(ListView):
    model = Post
    ordering = 'author'
    template_name = 'news.html'
    context_object_name = 'poste'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Распродажа в среду!"
        return context


class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'new.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'
    pk_url_kwarg = 'id'


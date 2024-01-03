from django.urls import path
from .views import ParserFormView

urlpatterns = [
    path('parser_book/', ParserFormView.as_view(), name='parser_book'),

]

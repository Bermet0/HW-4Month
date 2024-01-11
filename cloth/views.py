from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views import View
from . import models, forms


class ClothList(generic.ListView):
    model = models.ProductCl
    template_name = 'clothes/cloth_list.html'


class ClothListMale(generic.ListView):
    model = models.ProductCl
    template_name = 'clothes/male_list.html'

    def queryset(self):
        return self.model.objects.filter(tags__name='для_мужчин')


class ClothListFemale(generic.ListView):
    model = models.ProductCl
    template_name = 'clothes/female_list.html'

    def queryset(self):
        return self.model.objects.filter(tags__name='для_женщин')


class ClothListKids(generic.ListView):
    model = models.ProductCl
    template_name = 'clothes/kids_list.html'

    def queryset(self):
        return self.model.objects.filter(tags__name='для_детей')


class ClothListUni(generic.ListView):
    model = models.ProductCl
    template_name = 'clothes/forall_list.html'

    def queryset(self):
        return self.model.objects.filter(tags__name='универсальное')


class CreateOrderView(View):
    template_name = 'clothes/create_order.html'
    form_class = forms.OrderForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, self.template_name, {'form': form})

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.forms import models
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from myshop.models import Product, Purchase, Return, MyUser
from myshop.forms import UserRegisterForm, PurchaseCreateForm, ReturnCreateForm


class ProductView(ListView):
    model = Product
    template_name = 'home.html'


class Register(CreateView):
    form_class = UserRegisterForm
    template_name = 'signup.html'
    success_url = '/login/'


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = '/login'


def site(request):
    site_product = Product.objects.all ()
    return render(request, 'index.html', {'site_product': site_product})


class ProductCreateView (CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'image', 'quantity']
    template_name = 'new_product.html'
    success_url = reverse_lazy ('new_product')


class ProductUpdateView (UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'image', 'quantity']
    template_name = 'new_product.html'
    success_url = reverse_lazy ('home')


class PurchasesCreateView (CreateView):
    model = Purchase
    form_class = PurchaseCreateForm
    template_name = 'home.html'
    # success_url = reverse_lazy('purchase')


class PurchaseListView (ListView):
    model = Purchase
    template_name = 'purchase.html'
    # extra_context = {'form': PurchaseCreateForm}
    extra_context = {'create_form': PurchaseCreateForm()}

    def get_queryset(self):
        user_id = self.request.user.id
        if self.request.user.is_superuser:
            queryset = Purchase.objects.all ()
        else:
            queryset = Purchase.objects.filter (user_id=user_id)
        return queryset


class ReturnCreateView (CreateView):
    model = Return
    form_class = ReturnCreateForm
    template_name = 'purchase.html'
    # success_url = reverse_lazy('return')

    def form_valid(self, form):
        object = form.save(commit=False)
        purchase_id = Purchase.objects.get(id=self.request.POST.get('delete_id'))
        object.delete_id = purchase_id
        object.save()
        return super().form_valid(form=form)




class ReturnListView (ListView):
    model = Return
    template_name = 'return.html'
    success_url = reverse_lazy ('add/return/')

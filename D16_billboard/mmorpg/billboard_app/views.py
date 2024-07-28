from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView, )
from .models import Advertisement, UserResponse, User
from .filters import AdvertisementFilter, UserResponseFilter
from .forms import AdvertisementForm, UserResponseForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render


class AdvertisementsList(ListView):
    """Все объявления"""
    model = Advertisement
    ordering = '-time_in'
    template_name = "callboard/advertisements.html"
    context_object_name = 'advertisements'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdvertisementFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class Search(AdvertisementsList):
    raise_exception = True
    model = Advertisement
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 5

class AdvertisementDetail(DetailView):
    """Подробно об объявлении"""
    model = Advertisement
    template_name = "callboard/advertisement_detail.html"
    context_object_name = 'advertisement'


class AdvertisementCreate(LoginRequiredMixin, CreateView):
    """Добавление объявления"""
    form_class = AdvertisementForm
    model = Advertisement
    template_name = "callboard/advertisement_create.html"

    # создание объявления с автосохранением автора для объявления
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        form = AdvertisementForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                new_advertisement = form.save(commit=False)
                new_advertisement.author = request.user
                new_advertisement.save()
                return redirect('/advertisements/')
        return render(request, 'advertisement_create.html', locals())


class AdvertisementUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Редактирование объявления пользователя"""
    permission_required = ('board_app.change_advertisement',)
    form_class = AdvertisementForm
    model = Advertisement
    template_name = "callboard/advertisement_update.html"
    context_object_name = 'advertisement'


class AdvertisementDelete(LoginRequiredMixin, DeleteView):
    """Удаление объявления пользователя"""
    model = Advertisement
    template_name = "callboard/advertisement_delete.html"
    context_object_name = 'advertisement'
    success_url = reverse_lazy('advertisement_list')


class AuthorAdvertisementsList(ListView):
    """Все отклики пользователя"""
    model = Advertisement
    ordering = '-time_in'
    template_name = "callboard/advertisements_of_author.html"
    context_object_name = 'authoradvertisement'
    paginate_by = 10

    def get_queryset(self):
        self.author = get_object_or_404(User, id=self.kwargs['pk'])
        queryset = Advertisement.objects.filter(author=self.author)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        return context


class ResponseCreate(PermissionRequiredMixin, CreateView):
    """Добавление отклика"""
    form_class = UserResponseForm
    model = UserResponse
    template_name = "callboard/response_create.html"

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        form = UserResponseForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                new_response = form.save(commit=False)
                new_response.advertisement_id = self.kwargs.get('pk')
                new_response.commentator = request.user
                new_response.save()
                return redirect(f'/advertisements/{new_response.advertisement_id}')
        return render(request, 'response_create.html', locals())


class ResponseList(ListView):
    """Список откликов"""
    model = UserResponse
    ordering = '-time_create'
    template_name = "callboard/response_list.html"
    context_object_name = 'response_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = UserResponseFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ResponseDetail(DetailView):
    """Подробно об откликах"""
    model = UserResponse
    template_name = "callboard/response_detail.html"
    context_object_name = 'response_detail'




class ResponseAccept(UpdateView):
    """Принять отклик"""
    model = UserResponse
    template_name = "callboard/response_accept.html"
    context_object_name = 'response_accept'


class UpdateResponseForm:
    pass


class ResponseUpdate(UpdateView):
    """Редактирование отклика"""
    form_class = UpdateResponseForm
    model = UserResponse
    template_name = "callboard/response_edit.html"

    @login_required
    def confirm(self, request, *args, **kwargs):
        UserResponse.objects.filter(id=self.kwargs.get('pk')).update(status=True)
        UserResponse.save()
        return redirect(f'/advertisements/response_edit/{UserResponse.id}')


class ResponseDelete(DeleteView):
    """Удаление отклика"""
    model = UserResponse
    template_name = "callboard/response_delete.html"
    context_object_name = 'response'
    success_url = reverse_lazy('response_list')


class CommentatorresponsesList(ListView):
    model = UserResponse
    ordering = '-time_in'
    template_name = "callboard/responses_of_commentator.html"
    context_object_name = 'commentatorresponses'
    paginate_by = 10

    def get_queryset(self):
        self.commentator = get_object_or_404(User, id=self.kwargs['pk'])
        queryset = UserResponse.objects.filter(commentator=self.commentator)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentator'] = self.commentator
        return context


class AdvertisementsResponsesList(ListView):
    model = UserResponse
    ordering = '-time_in'
    template_name = "callboard/responses_of_advertisement.html"
    context_object_name = 'advertisementsresponses'
    paginate_by = 10

    def get_queryset(self):
        self.advertisement = get_object_or_404(Advertisement, id=self.kwargs['pk'])
        queryset = UserResponse.objects.filter(advertisement=self.advertisement)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisement'] = self.advertisement
        return context



# Create your views here.

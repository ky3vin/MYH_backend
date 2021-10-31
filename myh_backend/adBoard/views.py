from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Photo, Apply


from django.http import HttpResponseRedirect

from django.contrib import messages


class adBoardList(ListView):
    model = Photo
    template_name_suffix = '_list'



class adBoardCreate(CreateView):
    model = Photo
    fields = ['category', 'club_name', 'text', 'image', 'on_going', 'due_date', 'keep_going', 'tags' ]
    template_name_suffix = '_create'
    success_url = '/'

    # 관리자 권한이 없을경우 공지글 작성 권한 X
    def user_valid(request):
        if "manager" not in request.user.groups.all():
            return redirect("/")
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            # 올바르다면
            form.instance.save()
            return redirect('/')
        else:
            # 올바르지 않다면
            return self.render_to_response({'form': form})


class adBoardApply(CreateView):
    model = Apply
    fields = ['applicant', 'apply_club_name',  'apply_text']
    template_name_suffix = '_apply'
    success_url = '/'

    def form_valid(self, form):
        form.instance.applicant_id = self.request.user.id
        if form.is_valid():
            # 올바르다면
            form.instance.save()
            return redirect('/')
        else:
            # 올바르지 않다면
            return self.render_to_response({'form': form})

class ApplyList(ListView):
    model = Apply
    #template_name_suffix = '_list'

class ApplyDetail(ListView):
    model = Apply
    #template_name_suffix = '_list'

class adBoardUpdate(UpdateView):
    model = Photo

    fields = ['category', 'club_name', 'text', 'image']
    template_name_suffix = '_update'
    # success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '수정할 권한이 없습니다.')
            return HttpResponseRedirect('/')
        else:
            return super(adBoardUpdate, self).dispatch(request, *args, **kwargs)

class adBoardDelete(DeleteView):
    model = Photo

    template_name_suffix = '_delete'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '삭제할 권한이 없습니다.')
            return HttpResponseRedirect('/')
        else:
            return super(adBoardDelete, self).dispatch(request, *args, **kwargs)


class adBoardDetail(DetailView):
    model = Photo

    template_name_suffix = '_detail'


from django.views.generic.base import View
from django.http import HttpResponseForbidden
from urllib.parse import urlparse





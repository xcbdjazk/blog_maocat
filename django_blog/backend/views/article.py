# -*-  coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
import re
from django.shortcuts import redirect
from ..helps import rest
from django.views.decorators.http import require_http_methods
from ..models.admin import Admin
from ..models.article import Article
from utils.login_manage import login_require
from ..models.article import Tag


@require_http_methods(["GET", 'POST'])
@login_require
def index(request):
    if request.method == 'POST':
        article = Article()
        tags = Tag.objects.filter(id__in=request.POST.getlist('tag[]')).all()

        article.title = request.POST.get('title')
        article.desc = request.POST.get('content')
        # 去掉p标签
        content_text1 = article.desc.replace('<p>', '').replace('</p>', '').replace('\'', '')
        # 去掉图片链接
        content_text2 = re.sub('!\[\]\((.*?)\)', '', content_text1)
        # 去掉markdown标签
        pattern = '[\\\`\*\_\[\]\#\+\-\!\>]'
        content_text3 = re.sub(pattern, '', content_text2)
        article.desc_txt = content_text3
        article.save()
        article.tag.set(tags)
        return rest.success('添加成功', data={'url': redirect('index').url})
    return render(request, 'article/index.html')


@require_http_methods(["GET", 'POST'])
@login_require
def article_edit(request, id):
    art = Article.objects.get(id=id)
    if request.method == 'POST':
        tags = Tag.objects.filter(id__in=request.POST.getlist('tag[]')).all()

        art.title = request.POST.get('title')
        art.desc = request.POST.get('content').strip() # 去掉p标签
        content_text1 = art.desc.replace('<p>', '').replace('</p>', '').replace('\'', '')
        # 去掉图片链接
        content_text2 = re.sub('!\[\]\((.*?)\)', '', content_text1)
        # 去掉markdown标签
        pattern = '[\\\`\*\_\[\]\#\+\-\!\>]'
        content_text3 = re.sub(pattern, '', content_text2)
        art.desc_txt = content_text3
        art.save()
        art.tag.set(tags)
        return rest.success('添加成功', data={'url': redirect('index').url})

    tags = Tag.objects.all()
    content = dict(
        art=art,
        tags=tags
    )
    return render(request, 'article/article_edit.html', content)


@require_http_methods(["GET", 'POST'])
@login_require
def article_active(request, id):
    art = Article.objects.get(id=id)
    art.is_active = not art.is_active
    art.save()
    return redirect('index')


@require_http_methods(["GET", 'POST'])
@login_require
def tag_add(request):
    if request.method == 'POST':
        tag_name = request.POST.get('tag')
        if not tag_name:
            return rest.params_error('不能爲空')
        else:
            if Tag.objects.filter(name=tag_name).first():
                return rest.params_error('tag 已經存在')
            tag = Tag()
            tag.name = tag_name
            tag.save()
            return rest.success('添加成功')
    else:
        
        return render(request, 'article/tag_add.html')


@require_http_methods(["GET", 'POST'])
@login_require
def tag_list(request):

    tags = Tag.objects.all()
    content = dict(
        tags=tags
    )
    return render(request, 'article/tag_list.html', content)


@require_http_methods(["GET", 'POST'])
@login_require
def tag_edit(request, id):
    tag = Tag.objects.get(id=id)
    if request.method == 'POST':
        print(request.POST)
        tag_name = request.POST.get('tag')
        if not tag_name:
            return rest.params_error('不能爲空')
        else:
            if Tag.objects.filter(name=tag_name).first():
                return rest.params_error('tag 已經存在')
            tag.name = tag_name
            tag.save()
            return rest.success('修改成功')
    content = dict(
        tag=tag
    )
    return render(request, 'article/tag_edit.html', content)


@require_http_methods(["GET", 'POST'])
@login_require
def tag_ajax(request):
    tags = Tag.objects.all()
    data = []
    for tag in tags:
        data.append({'id': tag.id, 'text':tag.name})
    return rest.success(data=data)

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Article, History, User

from random import choice as rand_choice
import random
import string



@csrf_exempt
def main_page(request):
    articles = Article.objects.all()
    history = History.objects.all()
    try:
        user = User.objects.filter(session_id=request.COOKIES["session_id"])
        username = user.username
        username = user.status
    except Exception:
        username = "Username"
        user_status = "Common"
    return render(request, 'index.html', context={
        "articles": articles,
        "history": history,
        "username": username,
        "user_status": user_status
    })

@csrf_exempt
def login(request):
    if request.method == "POST":
        if request.POST.get("action") == "login":
            try:
                user = User.objects.filter(username=request.POST.get("username"))
                if request.POST.get("password") == user.password:
                    page = HttpResponse(f'<b>status: "okey"</b>')
                    session_id = ''.join(rand_choice('1234567890QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm') for i in range(15))
                    user.session_id = session_id
                    user.save()
                    request.session["session_id"] = session_id
            except Exception:
                page = HttpResponse(f'<b>status: "error"<br><i>Login or password not correct</i></b>')
            return page
        elif request.POST.get("action") == "register":
            try:
                user = User(
                    user_id = ''.join(rand_choice('1234567890') for i in range(10)),
                    status = "Common",
                    username = request.POST.get("username"),
                    password = request.POST.get("password"),
                    interest1 = request.POST.get("interest1"),
                    interest2 = request.POST.get("interest2"),
                    interest3 = request.POST.get("interest3"),
                    interest4 = request.POST.get("interest4"),
                    interest5 = request.POST.get("interest5")
                ).save()
                if request.POST.get("password") == user.password:
                    page = HttpResponse(f'<b>status: "okey"</b>')
                    session_id = ''.join(rand_choice('1234567890QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm') for i in range(15))
                    user.session_id = session_id
                    user.save()
                    page.set_cookie(key="session_id", value=session_id, path="/")
            except Exception as error:
                page = HttpResponse(f'<b>status: "error"<br><i>{print(error)}</i></b>')
            return page
        else:
            return render(request, 'error.html')
    return render(request, 'error.html')

@csrf_exempt
def articles_page(request):
    if request.method == "POST":
        article_id = request.POST.get("id")
        data = get_object_or_404(Article, article_id=article_id)
        if History.objects.filter(article_id=article_id).exists() == False:
            if len(data.preview) <= 35:
                previewText = data.preview
            else:
                previewText = data.preview[:35] + "..."
            History(article_id=article_id, title=data.title, preview=previewText).save()
        return JsonResponse({"data": {
            "id": data.article_id,
            "title": data.title,
            "text": data.text
        }})

@csrf_exempt
def api_page(request):
    if request.method == "POST":
        if request.POST.get("secure") == "SECURE_KEY":
            if request.POST.get("action") == "create_article":
                try:
                    article_id = ''.join(rand_choice('1234567890') for i in range(10))
                    print(article_id)
                    Article(
                        article_id = article_id,
                        title = request.POST.get("title"),
                        preview = request.POST.get("previewText"),
                        text = request.POST.get("text"),
                        interest = request.POST.get("interest")
                    ).save()
                    print("All good!")
                    return JsonResponse({"status": "okey", "id": article_id})
                except Exception as err:
                    return JsonResponse({"status":"error"})
            else:
                return JsonResponse({"status": "error"})
        else:
            return JsonResponse({"status":"error"})
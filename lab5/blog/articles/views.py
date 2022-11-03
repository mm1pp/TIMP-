from .models import Article
from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages 

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404




def create_post(request):
    if not request.user.is_anonymous:
    # Здесь будет основной код представления 
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': str(request.POST["text"]).strip(), 
                'title': str(request.POST["title"]).strip(),
                }
                # в словаре form будет храниться информация, введенная пользователем
            
            #проверка на уникальность названия
            for post in Article.objects.all():
                if str(form["title"]) == str(post.title):
                    form["errors"] = u"Название статьи не уникально!\nПридумайте новое название"
                    return render(request, 'createpost.html', {'form': form})


            if form["text"] and form["title"]:
                # если поля заполнены без ошибок
                article=Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return redirect('get_article', article_id=article.id)
                # перейти на страницу поста
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'createpost.html', {'form': form})
        else:
        # просто вернуть страницу с формой, если метод GET
            return render(request, 'createpost.html', {})
    else:
        raise Http404

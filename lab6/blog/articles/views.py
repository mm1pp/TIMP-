from .models import Article
from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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
        messages.error(request, "Войдите в аккаунт для добавления записей")
        return redirect('archive')


def deauth (request):
    if request.user.is_anonymous:
        messages.error(request, "Вы не вошли в аккаунт")
        return redirect("archive")#возвращаем главную страницу
    else:
        logout(request)
        messages.error(request, "Вы вышли из аккаунта")
        return redirect("archive")#возвращаем главную страницу

def auth_login (request):
    if request.user.is_anonymous: #если пользователь не вошёл в систему
        if request.method == "POST": #если метод пост
            form = {
                'username': str(request.POST["username"]).strip(), 
                'password': str(request.POST["password"]).strip(),
            }

            try:
                User.objects.get(username=str(form["username"])) #проверяем есть ли такой пользователь в базе, если есть код обойдёт except
            except User.DoesNotExist:
                form["errors"] = u"Такого пользователя не существует!\nЗарегистрируйтесь!"
                form['password'] = u""
                return render(request, 'register.html', {'form': form})

            user = authenticate(request, username=form["username"], password=form["password"]) #проверяем данные для входа

            if user is not None:
                login(request, user) #авторизуем пользователя
                messages.error(request, "Вы успешно вошли в аккаунт, как "+ str(form['username']))
                return redirect('archive')
            else:
                form["errors"] = u"Неверный пароль!"
                form['password'] = u""
                return render(request, 'login.html', {'form': form})

        else: #если кнопку ещё не нажимали
            return render(request, 'login.html', {}) 
    else:
        messages.error(request, "Вы уже вошли в аккаунт")
        return redirect("archive")#возвращаем главную страницу


def register_user(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            form = {
            'username': str(request.POST["username"]).strip(), 
                'password': str(request.POST["password"]).strip(),
                'email': str(request.POST["email"]).strip(),
                }
            try:
                User.objects.get(username=str(form["username"]))
                form["errors"] = u"Пользователь с таким именем уже есть"
                return render(request, 'register.html', {'form': form})
            except User.DoesNotExist:
                User.objects.create_user(form['username'], form['email'], form['password']) 
                return redirect('archive')
        else:
            return render(request, 'register.html', {})
    else:
        messages.error(request, "Вы уже вошли в аккаунт")
        return redirect("archive")
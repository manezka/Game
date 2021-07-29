from django.contrib.auth.models import User
from news.models import Author, Category, Post, Comment

# Пользователи
u1 = User.objects.create_user(username='Artem')
u2 = User.objects.create_user(username='Nick')

# Авторы
author = Author.objects.create(authorUser=u1)
author2 = Author.objects.create(authorUser=u2)

# Категории
Category.objects.create(name='IT')
Category.objects.create(name='Sport')
Category.objects.create(name='Politics')
Category.objects.create(name='Food')

# 2 статьи и 1 новость
Post.objects.create(author=author, categoryType='NW', title='sometitle', text='somebigtext')
Post.objects.create(author=author, categoryType='AR', title='Sport', text='blablabla')
Post.objects.create(author=author2, categoryType='AR', title='Politics', text='sometext again')
p1 = Post.objects.get(pk=1)
p2 = Post.objects.get(pk=2)
p3 = Post.objects.get(pk=3)


# Присвоение категорий
c1 = Category.objects.get(name = 'IT')
c2 = Category.objects.get(name = 'Sport')
c3 = Category.objects.get(name = 'Food')
c4 = Category.objects.get(name = 'Politics')
p1.postCategory.add(c1, c3)
p2.postCategory.add(c1, c2, c4)
p3.postCategory.add(c3, c4)

# Комментарии
Comment.objects.create(commentUser=User.objects.get(username='Artem'), commentPost=Post.objects.get(pk=1), text='comment1')
Comment.objects.create(commentUser=User.objects.get(username='Artem'), commentPost=Post.objects.get(pk=2), text='comment2')
Comment.objects.create(commentUser=User.objects.get(username='Nick'), commentPost=Post.objects.get(pk=3), text='comment3')
Comment.objects.create(commentUser=User.objects.get(username='Nick'), commentPost=Post.objects.get(pk=2), text='comment4')


# Лайки/дислайки
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).dislike()
Comment.objects.get(id=1).dislike()
Comment.objects.get(id=1).dislike()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=3).dislike()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=2).like()

Post.objects.get(id=1).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).dislike()
Post.objects.get(pk=3).dislike()
Post.objects.get(pk=3).dislike()

# Обновить рейтинги
Author.objects.get(authorUser=User.objects.get(username='Artem')).update_rating()
Author.objects.get(authorUser=User.objects.get(username='Nick')).update_rating()

# Вывести рейтинг лучшего пользователя
best = Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor')[0]
print(best)

# Вывести дату, имя, рейтинг, заголовок и превью лучшей статьи
a = Post.objects.all().order_by('-rating').values('author__authorUser__username', 'rating','dateCreation', 'title')[0]
print(a)

# Вывести все комментарии
for i in Comment.objects.filter(commentPost = Post.objects.all().order_by('-rating')[0]):
     print(i)

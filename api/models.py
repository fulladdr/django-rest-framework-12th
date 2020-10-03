from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('C', 'Custom'),
    ]
    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(blank=True, max_length=255)
    gender = models.CharField(blank=True, choices=GENDER_CHOICES, max_length=2)


# data가 만들어진 time을 기록하기 위해 만듬
class TimeStamp(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 별도의 테이블을 생성하지 않게 함
    class Meta:
        abstract = True


# 제품 포스트란
class Post(TimeStamp):
    image = models.ImageField(blank=True)
    caption = models.TextField(blank=True)


# 제품란
class Product(TimeStamp):
    name = models.CharField(blank=True, max_length=255)
    price = models.IntegerField()


# 제품 포스트에 달리는 댓글란
class Comment(TimeStamp):
    # model의 사용자 이름을 fk로 갖는다
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    # 댓글은 post를 fk로 갖는다
    post = models.ForeignKey(
        Post,
        null=True,
        on_delete=models.CASCADE,
        related_name='comment_post'
    )
    contents = models.TextField(blank=True)


class Order(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    name = models.ForeignKey(
        Product,
        null=True,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    amount = models.PositiveIntegerField(verbose_name='결제금액')
    order_date = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    data_added = models.DateField(auto_now_add=True, verbose_name="cart_date")


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_item_date")
    number = models.IntegerField()

    def total(self):
        return self.product.price * self.number

    def __str__(self):
        return self.product





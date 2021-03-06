# django-rest-framework-12th

## 유의사항
* 본 레포지토리는 백엔드 스터디 2-3주차의 과제를 위한 레포입니다.
* 따라서 해당 레포를 fork 및 clone 후 local에서 본인의 깃헙 ID 브랜치로 작업한 후 커밋/푸시하고,
PR 보낼 때도 `본인의 브랜치-> 본인의 브랜치`로 해야 합니다.
 
## 2주차 과제 (기한: 9/26 토요일까지)
노션 링크 (https://www.notion.so/2-Django-ORM-c46e2d2f88ac4d948d012c07605d8e03)

### 서비스 설명
쇼핑몰 서비스를 만들었습니다
간단한 기능 구현을 중심으로 했습니다.
기능은 제품 정보, 장바구니, 구매내역 3가지로 이루어졌습니다.

### 모델 설명
1.  /api 
    User model은 api 디렉토리 안에 설정되어 있으며 기존 User 모델에서 몇가지 정보를 추가했다.

2. /posts
   Posts 디렉토리는 제품 정보, 즉 포스팅 기능이 구현되어 있다
   포스팅에는 제품 정보를 나타내는 칸과 댓글 다는 칸으로 구성했다.
   제품 정보는 독립된 class이며 다른 class들과의 관계는 없다.
   댓글은 제품과 1:1 기능을 가지며, User와는 1:n 기능을 갖게 설정했다.
   추가적으로 timestamp 기능을 구현해 각각의 제품 및 댓글이 언제 달렸는지 추적할 수 있도록 만들었다.

3. /cart
    class를 Cart를 담은 사람과 CartItem 즉 카트에 담긴 제품으로 나누었으며
    Cartitem이 Cart를 FK로 1:n 관계로 참조하게 만들었다.
    CartItem은 product이름과 number 즉 구매 수량의 정보를 담고 있다.
    total 함수를 정의했는데 이는 제품 가격과 구매 수량을 곱한 총지불가격을 의미한다.
    Cart Class는 하나의 cart_id와 담긴 날짜를 갖고 있는다.
    
 4. /order
    주문기능입니다. Order class를 만들어 주문서를 작성해보고자 했으나 이부분에서 모델 구축의 어려움이 있었습니다.ㅇ
    일단 user와 product name을 fk로 만들었고, 수량, 총금액, 주문 날짜 기능을 담았습니다.
    이부분에서.. 장바구니 기능과 연동을 시켜야하는지 연동을 시킨다면 어떻게 연동을 시켜야할지,
    amount부분을 어떻게 구현해야할지 등의 어려움이 있었습니다.
    
### ORM 적용해보기
>>> Product.objects.create(name="apple",price=1200)
<Product: Product object (1)>
>>> Product.objects.create(name="pear",price=2500)
<Product: Product object (2)>
>>> Product.objects.create(name="watermelon",price=13200)
<Product: Product object (3)>
>>> Product.objects.all()
<QuerySet [<Product: Product object (1)>, <Product: Product object (2)>, <Product: Product object (3)>]>
>>> Product.object.filter(name="pear")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'Product' has no attribute 'object'
>>> Product.objects.filter(name="pear")
<QuerySet [<Product: Product object (2)>]>
>>>

### 간단한 회고 

===================================================================================
3주차

1. 선택한 모델

# 제품란
class Product(TimeStamp):
    name = models.CharField(blank=True, max_length=255, null=True)
    price = models.IntegerField()


# 제품 포스트란
class Post(TimeStamp):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True)
    caption = models.TextField(blank=True)
    
2. 모델 데이터
(1) Product
>>> Product.objects.values()
<QuerySet [{'id': 1, 'create_at': datetime.datetime(2020, 10, 3, 21, 18, 16, 488690), 'updated_
at': datetime.datetime(2020, 10, 3, 21, 18, 16, 488690), 'name': 'potato', 'price': 1000}, {'id
': 2, 'create_at': datetime.datetime(2020, 10, 3, 21, 18, 26, 696604), 'updated_at': datetime.d
atetime(2020, 10, 3, 21, 18, 26, 696604), 'name': 'watermelon', 'price': 4900}, {'id': 3, 'crea
te_at': datetime.datetime(2020, 10, 3, 21, 18, 34, 388276), 'updated_at': datetime.datetime(202
0, 10, 3, 21, 18, 34, 388276), 'name': 'pear', 'price': 3700}, {'id': 4, 'create_at': datetime.
datetime(2020, 10, 3, 21, 18, 45, 116818), 'updated_at': datetime.datetime(2020, 10, 3, 21, 18,
 45, 116818), 'name': 'peach', 'price': 7200}, {'id': 5, 'create_at': datetime.datetime(2020, 1
0, 3, 21, 18, 52, 154106), 'updated_at': datetime.datetime(2020, 10, 3, 21, 18, 52, 154106), 'n
ame': 'banana', 'price': 4900}, {'id': 6, 'create_at': datetime.datetime(2020, 10, 3, 21, 19, 4
, 755430), 'updated_at': datetime.datetime(2020, 10, 3, 21, 19, 4, 755430), 'name': 'mango', 'p
rice': 29200}, {'id': 7, 'create_at': datetime.datetime(2020, 10, 3, 21, 19, 40, 515138), 'upda
ted_at': datetime.datetime(2020, 10, 3, 21, 19, 40, 515138), 'name': 'orange', 'price': 8400}]>

(2) Post 데이터
>>> Post.objects.values()
<QuerySet [{'id': 1, 'create_at': datetime.datetime(2020, 10, 3, 21, 27, 5, 733914), 'up
dated_at': datetime.datetime(2020, 10, 3, 21, 27, 59, 501248), 'product_id': 1, 'image':
 '', 'caption': 'peach from California, low price'}, {'id': 2, 'create_at': datetime.dat
etime(2020, 10, 3, 21, 29, 35, 955463), 'updated_at': datetime.datetime(2020, 10, 3, 21,
 30, 21, 810793), 'product_id': 7, 'image': '', 'caption': '오렌지 먹은지 얼마나 오랜지'
}, {'id': 3, 'create_at': datetime.datetime(2020, 10, 3, 21, 39, 16, 720784), 'updated_a
t': datetime.datetime(2020, 10, 3, 21, 42, 32, 448990), 'product_id': None, 'image': '',
 'caption': 'watermelon from Russia, tasteful'}]>

3. API
(1) 모든 Post의 list를 갖고 오는 API
![api1](./image/api1.PNG)

(2) 특정 데이터를 가져오는 API
![api2](./image/api2.PNG)

(3) 새로운 데이터를 create 하도록 요청하는 API
![api3](./image/api3.PNG)
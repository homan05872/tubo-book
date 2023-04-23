from django.db import models
from .consts import MAX_RATE


CATEGORY = (('bussines', 'ビジネス'), ('life', '生活'), ('other', 'その他'))


class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.CharField(
        max_length=100,
        choices=CATEGORY
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # 管理画面でデータベースの名前を「verbose_name」へ変更できる※Metaクラスでは実装に関係のない情報を書く際に定義するもの
    # class Meta:
    #     verbose_name = '本のデータ'


RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

# レビュー用データ


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

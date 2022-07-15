from django.db import models
from django.utils import timezone

from common.models import CustomUser


class Feed(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author_f', verbose_name='게시글 작성자')
    content = models.TextField()
    image = models.ImageField(verbose_name='게시글 이미지', upload_to='image/%Y/%m/%d/', default='default.jpg')
    voter = models.ManyToManyField(CustomUser, verbose_name='추천인', related_name='voter_f')
    create_date = models.DateTimeField(verbose_name='생성일', default=timezone.now)
    modify_date = models.DateTimeField(verbose_name='수정일', null=True, blank=True)

    def __str__(self):
        return self.author

    class Meta:
        db_table = 'feeds'

from django.db import models
from django.utils import timezone

from common.models import CustomUser


class Feed(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author_f', verbose_name='게시글 작성자')
    content = models.TextField()
    image = models.TextField()
    profile_image = models.TextField()
    voter = models.ManyToManyField(CustomUser, related_name='voter_f', verbose_name='추천인')
    create_date = models.DateTimeField(verbose_name='생성일', default=timezone.now)
    modify_date = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.author

    class Meta:
        db_table = 'feeds'

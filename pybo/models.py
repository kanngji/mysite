from django.db import models
from django.contrib.auth.models import User

# 질문과 답변에 해당되는 모델을 파일에 정의해 보자.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    # id 값대신 제목을 표시
    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,null=True)
    content = models.TextField()
    create_date = models.DateTimeField()


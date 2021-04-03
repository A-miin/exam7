from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.TextField(max_length=256, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Вопрос"
        verbose_name_plural="Вопросы"

    def __str__(self):
        return self.question

class Choice(models.Model):
    option = models.TextField(max_length=256, null=False, blank=False)
    poll = models.ForeignKey('polls.Poll', on_delete=models.CASCADE, related_name="choices", verbose_name="Ответы")

    class Meta:
        verbose_name="Ответ"
        verbose_name_plural="Ответы"

    def __str__(self):
        return f'{self.poll.question}:{self.option}'

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
    poll = models.ForeignKey('polls.Poll', on_delete=models.CASCADE, related_name="choices", verbose_name="Вариант")

    class Meta:
        verbose_name="Вариант"
        verbose_name_plural="Варианты"

    def __str__(self):
        return f'{self.option}'

    def get_stat(self):
        if self.poll.answers.count()>0:
            return '{:.1f}'.format(self.answers.count()/self.poll.answers.count()*100)
        return 0

class Answer(models.Model):
    poll = models.ForeignKey('polls.Poll', on_delete=models.CASCADE, related_name='answers', verbose_name="Ответ")
    created_at = models.DateTimeField(auto_now_add=True)
    choice = models.ForeignKey('polls.Choice', on_delete=models.CASCADE, related_name='answers', verbose_name="Ответ")

    class Meta:
        verbose_name='Ответ'
        verbose_name_plural='Ответы'

    def __str__(self):
        return f'{self.poll.question}:{self.choice.option}'

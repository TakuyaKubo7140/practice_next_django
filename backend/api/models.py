from django.db import models


class Task(models.Model):
    title = models.CharField("タスク名", max_length=200)
    completed = models.BooleanField("完了済み", default=False)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    class Meta:
        ordering = ['-created_at']  # Order by creation date, newest first
        verbose_name = 'タスク'  # Custom plural name for the model
        verbose_name_plural = 'タスク一覧' # Custom plural name for the model

    def __str__(self):
        return f"{self.title} - {'完了' if self.completed else '未完了'}"

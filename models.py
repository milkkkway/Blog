from django.db import models
class Post(models.Model):
    #данные о посте

    title=models.CharField("Заголовок Записи",max_length=100)
    description=models.TextField("Текст записи")
    author=models.CharField("Имя автора",max_length=50)
    date=models.DateField("Дата публикации")
    img=models.ImageField("Изображение", upload_to="image/%Y")
    def __str__(self):
        return f"{self.title},{self.author}"
    class Meta:
        verbose_name="Запись"
        verbose_name_plural="Записи"

# Create your models here.

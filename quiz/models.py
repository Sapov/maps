from django.db import models


class InfoObjects(models.Model):
    pic = models.ImageField(upload_to='pic/', verbose_name="Условное обозначение")
    title = models.CharField(max_length=200, verbose_name="Название")
    descriptions = models.TextField(verbose_name="Описание", null=True, blank=True)
    example = models.ImageField(upload_to='example/', verbose_name='Примеры на карте', null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return f'{self.id}  {self.title}'

    class Meta:
        verbose_name_plural = 'Условные знаки'
        verbose_name = 'Условные знаки'


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return f' {self.id} {self.name}'

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

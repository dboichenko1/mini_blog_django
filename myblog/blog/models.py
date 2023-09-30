from django.db import models

# Create your models here.

class Post(models.Model):
    '''данные о посте все классы наследу.тся от models'''
    title = models.CharField("header", max_length=100) #поле которое хранит строку из n символов
    description = models.TextField("body") #Большое текстовое поле
    author = models.CharField("author",max_length=100)

    date = models.DateField("date")

    def __str__(self): #для красивого отображения в админ панели 
        return f'{self.title}, {self.author}'
    
    # class Meta:
    #     verbous_name = "Запись" #определение удобочитаемого единственного имени модели 
    #     verbous_name_plural = "Записи" 


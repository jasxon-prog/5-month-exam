from django.db import models

PRODUCT_TYPE = [
    ('docs', ".docs"),
    ('pptx', ".pptx"),
]

MATERIAL_TYPE = [
    ('document', 'Document materiallar'),
    ('audio', 'Audio materiallar'),
    ('shablon', 'Shablon materiallar'),
    ('video', 'Video materiallar'),
]


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')
    updated_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan sana")

    class Meta:
        abstract = True


class ProductImage(BaseModel): 
    images = models.ImageField(upload_to='product_images/')


class Category(BaseModel):  
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images/')


class Salesman(BaseModel):  
    name = models.CharField(max_length=255)
    total_sell_product = models.ManyToManyField("Product")
    income = models.IntegerField()
    material = models.CharField(max_length=255, choices=MATERIAL_TYPE)


class Product(BaseModel):  
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Salesman, on_delete=models.CASCADE) 
    image = models.ManyToManyField(ProductImage)  
    price = models.IntegerField()
    pages_count = models.IntegerField()
    size = models.FloatField()
    type = models.CharField(max_length=20, choices=PRODUCT_TYPE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
from django.db import models

PRODUCT_TYPE = [
    ('docs', ".docs"),
    ('pptx', ".pptx"),
    ('pdf', ".pdf")
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
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True, related_name="childrens/")

    def __str__(self):
        return self.name


class Tag(BaseModel):
    title = models.CharField(max_length=200)


class Salesman(BaseModel):  
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="seller_image", null=True, blank=True)
    backgroud_image = models.ImageField(upload_to="media/Seller_backgroud_image",null=True,blank=True)
    sold_products_count = models.ManyToManyField("Product")
    total_income = models.IntegerField()
    last_active = models.DateTimeField(null=True)
    material = models.CharField(max_length=255, choices=MATERIAL_TYPE)

    def __str__(self):
        return self.full_name


class Product(BaseModel):  
    title = models.CharField(max_length=255)
    seller = models.ForeignKey(Salesman, on_delete=models.CASCADE, related_name="products/") 
    images = models.ManyToManyField(ProductImage)  
    price = models.IntegerField()
    pages = models.IntegerField()
    file_size = models.FloatField()
    file_type = models.CharField(max_length=20, choices=PRODUCT_TYPE)
    file = models.FileField(upload_to="products/")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    poster = models.ImageField(upload_to="product_poster/")
    tags = models.ManyToManyField(Tag)
    body = models.TextField()
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
from django.db import models
  
class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)
    #auto_field = models.AutoField(primary_key=False)
    big_auto_field = models.BigAutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    # comma_separated_field = models.CharField(
    #     validators=[comma_separated_validator],
    #     max_length=255
    # )
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    file_field = models.FileField(upload_to='files/')
    img = models.ImageField(upload_to = "images/")
    #foreign_key = models.ForeignKey(OtherModel, on_delete=models.CASCADE)
    # many_to_many_field = models.ManyToManyField(OtherModel)
    # null_boolean_field = models.NullBooleanField()
    # one_to_one_field = models.OneToOneField(OtherModel, on_delete=models.CASCADE)
    # positive_big_integer_field = models PositiveBigIntegerField()
    slug_field = models.SlugField()
    url_field = models.URLField()
    uuid_field = models.UUIDField()
        
    def __str__(self):
        return self.title

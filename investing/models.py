from django.db import models


class Price(models.Model):
    class Meta:
        unique_together = ['name', 'date']
        ordering = ['-date']

    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    bid = models.FloatField()
    ask = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()


class Model(models.Model):
    TYPE = (
        ('T', 'Test'),
        ('P', 'Production'),
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    name = models.CharField(null=False, max_length=255)
    script = models.FileField(upload_to='uploads/models/')

    type = models.CharField(max_length=1, choices=TYPE, default='T')
    run_model = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Prediction(models.Model):
    class Meta:
        ordering = ['-created_on']

    model = models.ForeignKey(Model, null=False, on_delete=models.CASCADE)
    parameters = models.TextField(null=True, blank=True)
    predictor = models.IntegerField()
    value = models.FloatField()

    exec_time = models.DecimalField(max_digits=19, decimal_places=5)
    created_on = models.DateTimeField(auto_now_add=True)

    def get_outcome(self):
        return self.outcome.value if self.outcome else None

    def __str__(self):
        return f"{self.model}:{self.predictor} = {self.value}"


class Outcome(models.Model):
    class Meta:
        ordering = ['-created_on']

    prediction = models.OneToOneField(Prediction, null=False, on_delete=models.CASCADE)
    value = models.FloatField()

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.prediction)


class Run(models.Model):
    class Meta:
        ordering = ['-created_on']

    model = models.ForeignKey(Model, null=False, on_delete=models.CASCADE)
    parameters = models.TextField(null=True, blank=True)

    rmse = models.DecimalField(max_digits=19, decimal_places=5)
    mae = models.DecimalField(max_digits=19, decimal_places=5)
    r2 = models.DecimalField(max_digits=19, decimal_places=5)
    profit = models.DecimalField(max_digits=19, decimal_places=5)
    accuracy = models.DecimalField(max_digits=8, decimal_places=5)
    exec_time = models.DecimalField(max_digits=19, decimal_places=5)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.model)

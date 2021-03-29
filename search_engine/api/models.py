from django.db import models

class SearchEngineUser(models.Model):
    user_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


    def __str__(self):
        return self.user_name



class SearchHistory(models.Model):
    user= models.ForeignKey(SearchEngineUser,on_delete=models.CASCADE)
    search_keyword = models.CharField(max_length=250)
    search_result = models.CharField(max_length=250)
    search_at = models.DateField(auto_now_add=True)

    

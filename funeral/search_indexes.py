from haystack import indexes

from .models import Funeral


class FuneralIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    create_date = indexes.DateTimeField(model_attr='create_date')

    def get_model(self):
        return Funeral

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

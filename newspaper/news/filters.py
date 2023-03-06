import django_filters
from django.forms import DateTimeInput
from .models import Post, Category


class NewsFilter(django_filters.FilterSet):
    headline = django_filters.CharFilter(lookup_expr='icontains')
    body_text = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    pub_date_after = django_filters.DateTimeFilter(
        field_name='pub_date',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = ['headline', 'body_text', 'category', ]

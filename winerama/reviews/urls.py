from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /wine/
    url(r'^wine/$', views.wine_list, name='wine_list'),
    # ex: /wine/5/
    url(r'^wine/(?P<wine_id>[0-9]+)/$', views.wine_detail, name='wine_detail'),

    url(r'^add_review/(?P<wine_id>[0-9]+)/$', views.add_review, name='add_review'),

    url(r'^user/$', views.user_review_list, name='user_review_list'),
    url(r'^user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),

    url(r'^recommendation/$', views.user_recommendation_list, name='user_recommendation_list'),
]
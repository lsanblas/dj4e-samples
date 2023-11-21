from django.urls import path, reverse_lazy
from . import views
from . import models
from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

app_name='wellcopy'
urlpatterns = [
    path('', views.PostListView.as_view(), name='all'),
    path('brandall', views.BrandListView.as_view(), name='brandall'),
    path('guitarall', views.GuitarListView.as_view(), name='guitarall'),
    path('reviewall', views.ReviewListView.as_view(), name='reviewall'),

    path('post/<int:pk>', 
        OwnerDetailView.as_view(
            model = models.Postcopy,
            template_name = app_name+"/detail.html"), 
        name='post_detail'),

    path('post/create', 
        OwnerCreateView.as_view(
            success_url=reverse_lazy(app_name+':all'),
            model = models.Postcopy,
            template_name = app_name+"/form.html",
            fields = ['title', 'text']
         ), name='post_create'),

    path('post/<int:pk>/update', 
        OwnerUpdateView.as_view(
            success_url=reverse_lazy(app_name+':all'),
            model = models.Postcopy,
            fields = ['title', 'text'],
            template_name = app_name+"/form.html"
        ), name='post_update'),

    path('post/<int:pk>/delete', 
        OwnerDeleteView.as_view(
            success_url=reverse_lazy(app_name+':all'),
            model = models.Postcopy,
            template_name = app_name+"/delete.html"
        ), name='post_delete'),

    #Brand
    path('brand/<int:pk>', 
        OwnerDetailView.as_view(
            model = models.Brand,
            template_name = app_name+"/brand/detail.html"), 
        name='brand_detail'),

    # path('brand/create', 
    #     OwnerCreateView.as_view(
    #         success_url=reverse_lazy(app_name+':brandall'),
    #         model = models.Brand,
    #         template_name = app_name+"/brand/form.html",
    #         fields = ['name', 'description', 'url', 'picture']
    #      ), name='brand_create'),

    # path('brand/<int:pk>/update', 
    #     OwnerUpdateView.as_view(
    #         success_url=reverse_lazy(app_name+':brandall'),
    #         model = models.Brand,
    #         fields = ['name', 'description', 'url', 'picture'],
    #         template_name = app_name+"/brand/form.html"
    #     ), name='brand_update'),
    
    path('brand/create', 
         views.BrandCreateView.as_view(success_url=reverse_lazy(app_name+':brandall')), name='brand_create'),

    path('brand/<int:pk>/update', 
         views.BrandUpdateView.as_view(success_url=reverse_lazy(app_name+':brandall')), name='brand_update'),

    path('brand/<int:pk>/delete', 
        OwnerDeleteView.as_view(
            success_url=reverse_lazy(app_name+':brandall'),
            model = models.Brand,
            template_name = app_name+"/brand/delete.html"
        ), name='brand_delete'),
    path('brand_picture/<int:pk>', views.stream_brandfile, name='brand_picture'),

    #Guitar
    path('guitar/<int:pk>', 
        OwnerDetailView.as_view(
            model = models.Guitar,
            template_name = app_name+"/guitar/detail.html"), 
        name='guitar_detail'),

    # path('guitar/create', 
    #     OwnerCreateView.as_view(
    #         success_url=reverse_lazy(app_name+':guitarall'),
    #         model = models.Guitar,
    #         template_name = app_name+"/guitar/form.html",
    #         fields = ['name', 'specs', 'picture', 'brand']
    #      ), name='guitar_create'),

    # path('guitar/<int:pk>/update', 
    #     OwnerUpdateView.as_view(
    #         success_url=reverse_lazy(app_name+':guitarall'),
    #         model = models.Guitar,
    #         fields = ['name', 'specs', 'picture', 'brand'],
    #         template_name = app_name+"/guitar/form.html"
    #     ), name='guitar_update'),

    path('guitar/create', 
         views.GuitarCreateView.as_view(success_url=reverse_lazy(app_name+':guitarall')), name='guitar_create'),

    path('guitar/<int:pk>/update', 
         views.GuitarUpdateView.as_view(success_url=reverse_lazy(app_name+':guitarall')), name='guitar_update'),

    path('guitar/<int:pk>/delete', 
        OwnerDeleteView.as_view(
            success_url=reverse_lazy(app_name+':guitarall'),
            model = models.Guitar,
            template_name = app_name+"/guitar/delete.html"
        ), name='guitar_delete'),
    path('guitar_picture/<int:pk>', views.stream_guitarfile, name='guitar_picture'),

    #Review
    path('review/<int:pk>', 
        OwnerDetailView.as_view(
            model = models.Review,
            template_name = app_name+"/review/detail.html"), 
        name='review_detail'),

    path('review/create', 
        OwnerCreateView.as_view(
            success_url=reverse_lazy(app_name+':reviewall'),
            model = models.Review,
            template_name = app_name+"/review/form.html",
            fields = ['content', 'score', 'guitar']
         ), name='review_create'),

    path('review/<int:pk>/update', 
        OwnerUpdateView.as_view(
            success_url=reverse_lazy(app_name+':reviewall'),
            model = models.Review,
            fields = ['content', 'score', 'guitar'],
            template_name = app_name+"/review/form.html"
        ), name='review_update'),

    path('review/<int:pk>/delete', 
        OwnerDeleteView.as_view(
            success_url=reverse_lazy(app_name+':reviewall'),
            model = models.Review,
            template_name = app_name+"/review/delete.html"
        ), name='review_delete'),

]


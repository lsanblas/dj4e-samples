from django.shortcuts import render, get_object_or_404, redirect
from wellcopy.models import Postcopy, Brand, Guitar, Review, Comment
from django.views import View
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.db.models import Q
from wellcopy.forms import CreateBrandForm, CreateGuitarForm, CommentForm
from myarts.owner import OwnerDeleteView, OwnerDetailView

class PostListView(View):
    template_name = "wellcopy/list.html"

    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            # Simple title-only search
            # objects = Post.objects.filter(title__contains=strval).select_related().order_by('-updated_at')[:10]

            # Multi-field search
            # __icontains for case-insensitive search
            query = Q(title__icontains=strval) 
            query.add(Q(text__icontains=strval), Q.OR)
            post_list = Postcopy.objects.filter(query).select_related().order_by('-updated_at')[:10]
        else :
            post_list = Postcopy.objects.all().order_by('-updated_at')[:10]

        # Augment the post_list
        for obj in post_list:
            obj.natural_updated = naturaltime(obj.updated_at)

        ctx = {'post_list' : post_list, 'search': strval}
        return render(request, self.template_name, ctx)
    
class BrandListView(View):
    template_name = "wellcopy/brand/list.html"

    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            query = Q(name__icontains=strval) 
            query.add(Q(description__icontains=strval), Q.OR)
            brand_list = Brand.objects.filter(query).select_related().order_by('-updated_at')[:10]
        else :
            brand_list = Brand.objects.all().order_by('-updated_at')[:10]

        # Augment the brand_list
        for obj in brand_list:
            obj.natural_updated = naturaltime(obj.updated_at)

        ctx = {'brand_list' : brand_list, 'search': strval}
        return render(request, self.template_name, ctx)
    
class BrandCreateView(LoginRequiredMixin, View):
    template_name = 'wellcopy/brand/form.html'
    success_url = reverse_lazy('wellcopy:brandall')

    def get(self, request, pk=None):
        form = CreateBrandForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateBrandForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)
    
class BrandUpdateView(LoginRequiredMixin, View):
    template_name = 'wellcopy/brand/form.html'
    success_url = reverse_lazy('wellcopy:brandall')

    def get(self, request, pk):
        pic = get_object_or_404(Brand, id=pk, owner=self.request.user)
        form = CreateBrandForm(instance=pic)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        pic = get_object_or_404(Brand, id=pk, owner=self.request.user)
        form = CreateBrandForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.save()

        return redirect(self.success_url)
    
class GuitarListView(View):
    template_name = "wellcopy/guitar/list.html"

    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            query = Q(name__icontains=strval) 
            query.add(Q(specs__icontains=strval), Q.OR)
            guitar_list = Guitar.objects.filter(query).select_related().order_by('-updated_at')[:10]
        else :
            guitar_list = Guitar.objects.all().order_by('-updated_at')[:10]

        # Augment the guitar_list
        for obj in guitar_list:
            obj.natural_updated = naturaltime(obj.updated_at)

        ctx = {'guitar_list' : guitar_list, 'search': strval}
        return render(request, self.template_name, ctx)

class GuitarCreateView(LoginRequiredMixin, View):
    template_name = 'wellcopy/guitar/form.html'
    success_url = reverse_lazy('wellcopy:guitarall')

    def get(self, request, pk=None):
        form = CreateGuitarForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateGuitarForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)
    
class GuitarUpdateView(LoginRequiredMixin, View):
    template_name = 'wellcopy/guitar/form.html'
    success_url = reverse_lazy('wellcopy:guitarall')

    def get(self, request, pk):
        pic = get_object_or_404(Guitar, id=pk, owner=self.request.user)
        form = CreateGuitarForm(instance=pic)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        pic = get_object_or_404(Guitar, id=pk, owner=self.request.user)
        form = CreateGuitarForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.save()

        return redirect(self.success_url)
    
class ReviewListView(View):
    template_name = "wellcopy/review/list.html"

    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            query = Q(content__icontains=strval) 
            #query.add(Q(text__icontains=strval), Q.OR)
            review_list = Review.objects.filter(query).select_related().order_by('-updated_at')[:10]
        else :
            review_list = Review.objects.all().order_by('-updated_at')[:10]

        # Augment the review_list
        for obj in review_list:
            obj.natural_updated = naturaltime(obj.updated_at)

        ctx = {'review_list' : review_list, 'search': strval}
        return render(request, self.template_name, ctx)
    
class ReviewDetailView(OwnerDetailView):
    model = Review
    template_name = "wellcopy/review/detail.html"
    def get(self, request, pk) :
        x = get_object_or_404(Review, id=pk)
        comments = Comment.objects.filter(review=x).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'review' : x, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)
    
class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Review, id=pk)
        comment = Comment(content=request.POST['comment'], owner=request.user, review=f)
        comment.save()
        return redirect(reverse('wellcopy:review_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "wellcopy/review/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        review = self.object.review
        return reverse('wellcopy:review_detail', args=[review.id])
    
def stream_brandfile(request, pk):
    pic = get_object_or_404(Brand, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response

def stream_guitarfile(request, pk):
    pic = get_object_or_404(Guitar, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response

# csrf exemption in class based views
# https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

@method_decorator(csrf_exempt, name='dispatch')
class AddLikeView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Add PK",pk)
        t = get_object_or_404(Review, id=pk)
        t.likes = t.likes + 1
        try:
            t.save()  # In case of duplicate key
        except IntegrityError as e:
            pass
        return HttpResponse()

# References

# https://docs.djangoproject.com/en/4.2/topics/db/queries/#one-to-many-relationships

# Note that the select_related() QuerySet method recursively prepopulates the
# cache of all one-to-many relationships ahead of time.

# sql “LIKE” equivalent in django query
# https://stackoverflow.com/questions/18140838/sql-like-equivalent-in-django-query

# How do I do an OR filter in a Django query?
# https://stackoverflow.com/questions/739776/how-do-i-do-an-or-filter-in-a-django-query

# https://stackoverflow.com/questions/1074212/how-can-i-see-the-raw-sql-queries-django-is-running

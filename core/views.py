from django.views.generic import TemplateView
from django.shortcuts import render

class Home(TemplateView):
    template_name = "index.html"

class About(TemplateView):
    template_name = 'about.html'

class BlogArticle(TemplateView):
    template_name = 'blog-article.html'

class BlogPage(TemplateView):
    template_name = 'blog.html'

class Fundraising(TemplateView):
    template_name = 'fundraising-causes.html'

class Gallery3(TemplateView):
    template_name = 'gallery-3-columns.html'

class Instagram3(TemplateView):
    template_name = 'gallery-instagram-3-columns.html'

# Error handling
def page_not_found_view(request, exception):
    return render(request, 'errors/404.html', status=404)

def error_view(request, exception=None):
    return render(request, 'errors/500.html', status=500)

def permission_denied_view(request, exception):
    return render(request, 'errors/403.html', status=403)

def bad_request_view(request, exception):
    return render(request, 'errors/400.html', status=400)
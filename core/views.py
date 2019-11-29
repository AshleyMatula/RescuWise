from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "index.html"

class DynamicStaticPages(TemplateView):

    def get_template_names(self, **kwargs):
        if self.kwargs.get('template_name'):
            # favicons load first so with out this this dynamic view doesn't work.
            if self.kwargs.get('template_name') == "favicon.ico":
                pass
            else:
                return self.kwargs.get('template_name')
        #if there is no url default it index.html
        return "index.html"

# Error handling
def page_not_found_view(request, exception):
    return render(request, 'errors/404.html', status=404)

def error_view(request, exception=None):
    return render(request, 'errors/500.html', status=500)

def permission_denied_view(request, exception):
    return render(request, 'errors/403.html', status=403)

def bad_request_view(request, exception):
    return render(request, 'errors/400.html', status=400)
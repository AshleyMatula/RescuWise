from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from core.models import Animal

class AnimalIndex(ListView):
    model = Animal
    template_name = 'animals.html'

class browsecompanies(TemplateView):
      template_name = 'browse-companies.html'

class dashboardbookmarks(TemplateView):
      template_name = 'dashboard-bookmarks.html'

class dashboardmanagebidders(TemplateView):
      template_name = 'dashboard-manage-bidders.html'

class dashboardmanagecandidates(TemplateView):
      template_name = 'dashboard-manage-candidates.html'

class dashboardmanagejobs(TemplateView):
      template_name = 'dashboard-manage-jobs.html'

class dashboardmanagetasks(TemplateView):
      template_name = 'dashboard-manage-tasks.html'

class dashboardmessages(TemplateView):
      template_name = 'dashboard-messages.html'

class dashboardmyactivebids(TemplateView):
      template_name = 'dashboard-my-active-bids.html'

class dashboardpostajob(TemplateView):
      template_name = 'dashboard-post-a-job.html'

class dashboardpostatask(TemplateView):
      template_name = 'dashboard-post-a-task.html'

class dashboardreviews(TemplateView):
      template_name = 'dashboard-reviews.html'

class dashboardsettings(TemplateView):
      template_name = 'dashboard-settings.html'

class dashboard(TemplateView):
      template_name = 'dashboard.html'

class documentation(TemplateView):
      template_name = 'documentation.html'

class freelancersgridlayoutfullpage(TemplateView):
      template_name = 'freelancers-grid-layout-full-page.html'

class freelancersgridlayout(TemplateView):
      template_name = 'freelancers-grid-layout.html'

class freelancerslistlayout1(TemplateView):
      template_name = 'freelancers-list-layout-1.html'

class freelancerslistlayout2(TemplateView):
      template_name = 'freelancers-list-layout-2.html'

class index2(TemplateView):
      template_name = 'index-2.html'

class index3(TemplateView):
      template_name = 'index-3.html'

class indexloggedout(TemplateView):
      template_name = 'index-logged-out.html'

class index(TemplateView):
      template_name = 'index.html'

class jobsgridlayoutfullpagemapOpenStreetMap(TemplateView):
      template_name = 'jobs-grid-layout-full-page-map-OpenStreetMap.html'

class jobsgridlayoutfullpagemap(TemplateView):
      template_name = 'jobs-grid-layout-full-page-map.html'

class jobsgridlayoutfullpage(TemplateView):
      template_name = 'jobs-grid-layout-full-page.html'

class jobsgridlayout(TemplateView):
      template_name = 'jobs-grid-layout.html'

class jobslistlayout1OpenStreetMap(TemplateView):
      template_name = 'jobs-list-layout-1-OpenStreetMap.html'

class jobslistlayout1(TemplateView):
      template_name = 'jobs-list-layout-1.html'

class jobslistlayout(TemplateView):
      template_name = 'jobs-list-layout-2.html'

class jobslistlayoutfullpagemapOpenStreetMap(TemplateView):
      template_name = 'jobs-list-layout-full-page-map-OpenStreetMap.html'

class jobslistlayoutfullpagemap(TemplateView):
      template_name = 'jobs-list-layout-full-page-map.html'

class pages404(TemplateView):
      template_name = 'pages-404.html'

class pagesblogpost(TemplateView):
      template_name = 'pages-blog-post.html'

class pagesblog(TemplateView):
      template_name = 'pages-blog.html'

class pagescheckoutpage(TemplateView):
      template_name = 'pages-checkout-page.html'

class pagescontactOpenStreetMap(TemplateView):
      template_name = 'pages-contact-OpenStreetMap.html'

class pagescontact(TemplateView):
      template_name = 'pages-contact.html'

class pagesiconscheatsheet(TemplateView):
      template_name = 'pages-icons-cheatsheet.html'

class pagesinvoicetemplate(TemplateView):
      template_name = 'pages-invoice-template.html'

class pageslogin(TemplateView):
      template_name = 'pages-login.html'

class pagesorderconfirmation(TemplateView):
      template_name = 'pages-order-confirmation.html'

class pagespricingplans(TemplateView):
      template_name = 'pages-pricing-plans.html'

class pagesregister(TemplateView):
      template_name = 'pages-register.html'

class pagesuserinterfaceelements(TemplateView):
      template_name = 'pages-user-interface-elements.html'

class singlecompanyprofileOpenStreetMap(TemplateView):
      template_name = 'single-company-profile-OpenStreetMap.html'

class singlecompanyprofile(TemplateView):
      template_name = 'single-company-profile.html'

class singlefreelancerprofile(TemplateView):
      template_name = 'single-freelancer-profile.html'

class singlejobpageOpenStreetMap(TemplateView):
      template_name = 'single-job-page-OpenStreetMap.html'

class singlejobpage(TemplateView):
      template_name = 'single-job-page.html'

class singletaskpage(TemplateView):
      template_name = 'single-task-page.html'

class tasksgridlayoutfullpage(TemplateView):
      template_name = 'tasks-grid-layout-full-page.html'

class tasksgridlayout(TemplateView):
      template_name = 'tasks-grid-layout.html'

class taskslistlayout1(TemplateView):
      template_name = 'tasks-list-layout-1.html'

class taskslistlayout2(TemplateView):
      template_name = 'tasks-list-layout-2.html'

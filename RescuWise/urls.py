"""RescuWise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from RescuWise.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('animals/', AnimalIndex.as_view(), name='animals'),
    path('admin/', admin.site.urls),
    path('browse-companies.html', browsecompanies.as_view(), name='browsecompanies'),
    path('dashboard-bookmarks.html', dashboardbookmarks.as_view(), name='dashboardbookmarks'),
    path('dashboard-manage-bidders.html', dashboardmanagebidders.as_view(), name='dashboardmanagebidders'),
    path('dashboard-manage-candidates.html', dashboardmanagecandidates.as_view(), name='dashboardmanagecandidates'),
    path('dashboard-manage-jobs.html', dashboardmanagejobs.as_view(), name='dashboardmanagejobs'),
    path('dashboard-manage-tasks.html', dashboardmanagetasks.as_view(), name='dashboardmanagetasks'),
    path('dashboard-messages.html', dashboardmessages.as_view(), name='dashboardmessages'),
    path('dashboard-my-active-bids.html', dashboardmyactivebids.as_view(), name='dashboardmyactivebids'),
    path('dashboard-post-a-job.html', dashboardpostajob.as_view(), name='dashboardpostajob'),
    path('dashboard-post-a-task.html', dashboardpostatask.as_view(), name='dashboardpostatask'),
    path('dashboard-reviews.html', dashboardreviews.as_view(), name='dashboardreviews'),
    path('dashboard-settings.html', dashboardsettings.as_view(), name='dashboardsettings'),
    path('dashboard.html', dashboard.as_view(), name='dashboard'),
    path('documentation.html', documentation.as_view(), name='documentation'),
    path('freelancers-grid-layout-full-page.html', freelancersgridlayoutfullpage.as_view(), name='freelancersgridlayoutfullpage'),
    path('freelancers-grid-layout.html', freelancersgridlayout.as_view(), name='freelancersgridlayout'),
    path('freelancers-list-layout-1.html', freelancerslistlayout1.as_view(), name='freelancerslistlayout1'),
    path('freelancers-list-layout-2.html', freelancerslistlayout2.as_view(), name='freelancerslistlayout2'),
    path('index-2.html', index2.as_view(), name='index2'),
    path('index-3.html', index3.as_view(), name='index3'),
    path('index-logged-out.html', indexloggedout.as_view(), name='indexloggedout'),
    path('', index.as_view(), name='index'),
    path('jobs-grid-layout-full-page-map-OpenStreetMap.html', jobsgridlayoutfullpagemapOpenStreetMap.as_view(), name='jobsgridlayoutfullpagemapOpenStreetMap'),
    path('jobs-grid-layout-full-page-map.html', jobsgridlayoutfullpagemap.as_view(), name='jobsgridlayoutfullpagemap'),
    path('jobs-grid-layout-full-page.html', jobsgridlayoutfullpage.as_view(), name='jobsgridlayoutfullpage'),
    path('jobs-grid-layout.html', jobsgridlayout.as_view(), name='jobsgridlayout'),
    path('jobs-list-layout-1-OpenStreetMap.html', jobslistlayout1OpenStreetMap.as_view(), name='jobslistlayout1OpenStreetMap'),
    path('jobs-list-layout-1.html', jobslistlayout1.as_view(), name='jobslistlayout1'),
    path('jobs-list-layout-2.html', jobslistlayout.as_view(), name='jobslistlayout'),
    path('jobs-list-layout-full-page-map-OpenStreetMap.html', jobslistlayoutfullpagemapOpenStreetMap.as_view(), name='jobslistlayoutfullpagemapOpenStreetMap'),
    path('jobs-list-layout-full-page-map.html', jobslistlayoutfullpagemap.as_view(), name='jobslistlayoutfullpagemap'),
    path('pages-404.html', pages404.as_view(), name='pages404'),
    path('pages-blog-post.html', pagesblogpost.as_view(), name='pagesblogpost'),
    path('pages-blog.html', pagesblog.as_view(), name='pagesblog'),
    path('pages-checkout-page.html', pagescheckoutpage.as_view(), name='pagescheckoutpage'),
    path('pages-contact-OpenStreetMap.html', pagescontactOpenStreetMap.as_view(), name='pagescontactOpenStreetMap'),
    path('pages-contact.html', pagescontact.as_view(), name='pagescontact'),
    path('pages-icons-cheatsheet.html', pagesiconscheatsheet.as_view(), name='pagesiconscheatsheet'),
    path('pages-invoice-template.html', pagesinvoicetemplate.as_view(), name='pagesinvoicetemplate'),
    path('pages-login.html', pageslogin.as_view(), name='pageslogin'),
    path('pages-order-confirmation.html', pagesorderconfirmation.as_view(), name='pagesorderconfirmation'),
    path('pages-pricing-plans.html', pagespricingplans.as_view(), name='pagespricingplans'),
    path('pages-register.html', pagesregister.as_view(), name='pagesregister'),
    path('pages-user-interface-elements.html', pagesuserinterfaceelements.as_view(), name='pagesuserinterfaceelements'),
    path('single-company-profile-OpenStreetMap.html', singlecompanyprofileOpenStreetMap.as_view(), name='singlecompanyprofileOpenStreetMap'),
    path('single-company-profile.html', singlecompanyprofile.as_view(), name='singlecompanyprofile'),
    path('single-freelancer-profile.html', singlefreelancerprofile.as_view(), name='singlefreelancerprofile'),
    path('single-job-page-OpenStreetMap.html', singlejobpageOpenStreetMap.as_view(), name='singlejobpageOpenStreetMap'),
    path('single-job-page.html', singlejobpage.as_view(), name='singlejobpage'),
    path('single-task-page.html', singletaskpage.as_view(), name='singletaskpage'),
    path('tasks-grid-layout-full-page.html', tasksgridlayoutfullpage.as_view(), name='tasksgridlayoutfullpage'),
    path('tasks-grid-layout.html', tasksgridlayout.as_view(), name='tasksgridlayout'),
    path('tasks-list-layout-1.html', taskslistlayout1.as_view(), name='taskslistlayout1'),
    path('tasks-list-layout-2.html', taskslistlayout2.as_view(), name='taskslistlayout2'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
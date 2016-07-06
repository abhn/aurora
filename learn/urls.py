from django.conf.urls import url
from learn import views

urlpatterns = [
   url(r'^$', views.hello),
   # layout page
   url(r'domain/(?P<domain_slug>.+)$', views.get_domain_resources_view),
   url(r'technology/(?P<tech_slug>.+)$', views.get_tech_resources_view),
   # extract info from wiki
   url(r'search-wiki/$', views.get_wiki_view),
   # getting resource specific feedback from the user
   url(r'quality-feedback/$', views.resource_quality_ratings),
   # getting general feedback from the user
   url(r'^feedback/$', views.feedback_forms),
   # download data
   # url(r'download_all_domain_data/(?P<domain_slug>.+)$', views.download_all_domain_data_view),
   # url(r'download_all_tech_data/(?P<tech_slug>.+)$', views.download_all_tech_data_view),
   # helper urls
   url(r'get_all_domains/$', views.get_all_domains_view),
   url(r'get_all_technologies/$', views.get_all_technologies_view),
   url(r'get_domains_and_slugs/$', views.get_domains_and_slugs_view),   
   ]

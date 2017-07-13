from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^job$', views.job, name="job"),
    url(r'^division$', views.division, name="division"),
    url(r'^standard$', views.standard, name="standard"),
    url(r'^patchStandard$', views.patchStandard, name="patchStandard"),
    url(r'^patchTolerance$', views.patchTolerance, name="patchTolerance"),
    url(r'^role$', views.role, name="role"),
    url(r'^bookmark$', views.bookmark, name="bookmark"),
    url(r'^link$', views.link, name="link"),
    url(r'^valuesFromBrand$', views.valuesFromBrand, name="valuesFromBrand"),
    url(r'^showJobs$', views.showJobs, name="showJobs"),
    url(r'^showBrands$', views.showBrands, name="showBrands"),
    url(r'^showDivisions$', views.showDivisions, name="showDivisions"),
    url(r'^showStandards$', views.showStandards, name="showStandards"),
    url(r'^showEvalutions$', views.showEvalutions, name="showEvalutions"),
    url(r'^showMemberEvaluations$', views.showMemberEvaluations, name="showMemberEvaluations"),
    url(r'^showMemberProperty$', views.showMemberProperty, name="showMemberProperty"),

]

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
    url(r'^upload$', views.upload, name="upload"),

    url(r'^valuesFromBrand$', views.valuesFromBrand, name="valuesFromBrand"),

    url(r'^showJobs$', views.showJobs, name="showJobs"),
    url(r'^showBrands$', views.showBrands, name="showBrands"),
    url(r'^showDivisions$', views.showDivisions, name="showDivisions"),
    url(r'^showStandards$', views.showStandards, name="showStandards"),
    url(r'^showEvalutions$', views.showEvalutions, name="showEvalutions"),
    url(r'^showMemberEvaluations$', views.showMemberEvaluations, name="showMemberEvaluations"),
    url(r'^showMemberProperty$', views.showMemberProperty, name="showMemberProperty"),
    url(r'^showUploads$', views.showUploads, name="showUploads"),

    url(r'^editJob/(?P<ID>\d+)$', views.editJob, name="editJob"),
    url(r'^editDivision/(?P<ID>\d+)$', views.editDivision, name="editDivision"),
    url(r'^editStandard/(?P<ID>\d+)$', views.editStandard, name="editStandard"),
    url(r'^editUpload/(?P<ID>\d+)$', views.editUpload, name="editUpload"),

    url(r'^deleteJob/(?P<ID>\d+)$', views.deleteJob, name="deleteJob"),
    url(r'^deleteBrand/(?P<ID>\d+)$', views.deleteBrand, name="deleteBrand"),
    url(r'^deleteDivision/(?P<ID>\d+)$', views.deleteDivision, name="deleteDivision"),
    url(r'^deleteStandard/(?P<ID>\d+)$', views.deleteStandard, name="deleteStandard"),
    url(r'^deleteUpload/(?P<ID>\d+)$', views.deleteUpload, name="deleteUpload"),


]

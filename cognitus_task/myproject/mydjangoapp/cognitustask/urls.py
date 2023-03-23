from django.urls import path
from cognitustask.views import DataList, DataDetail,Train,Predict
#from . import views
#from django.conf.urls import url

urlpatterns = [
  
 path('api/datas', DataList.as_view()),
 path('api/datas/<int:pk>', DataDetail.as_view()),
 path("train/",Train.as_view(),name='data_train'),
 path('predict/',Predict.as_view())

  #path("",views.data_form,name='data_insert'), # get and post req. for insert op
  #path("<int:id>/",views.data_form,name='data_update'), # get and post req. for update op
  #path('delete/<int:id>/',views.data_delete,name='data_delete'),
  #path("list/",views.data_list,name='data_list'), # get req. to retrieve and display all records"""
]
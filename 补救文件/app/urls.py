"""定义learning_logs的URL模式"""

from django.conf.urls import url

from . import views
app_name = 'learning_logs'

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示主题
    url(r'^topics/$', views.topics, name='topics'),

    # 特定主题的详细内容
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
from django.conf.urls import include, url
from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views
from polls.models import Question

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)  #register the users viewset
router.register(r'questions',QuestionViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'restdemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # /api-auth/  for session authentication page
    url(r'^api-token-auth/', views.obtain_auth_token),  ## token auth
]

import datetime

from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# Create your views here.
# from skillitupcore.MLToDBMapper import MLToDBMapper
from api import mlpred
from api.serializers import *
from skillitupcore.models import *


class DomainViewSet(ViewSet):
    permission_classes = [AllowAny]
    queryset = Domain.objects.all()

    def list(self, request):
        try:
            serializer = DomainSerializer(self.queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({"Error": "Domains not found"})

    def retrieve(self, request, pk=None):
        try:
            item = get_object_or_404(self.queryset, pk=pk)
            serializer = DomainSerializer(item)
            return Response(serializer.data)
        except:
            return Response({"Error": "Specified Domain not found"})


class SubDomainViewSet(ViewSet):
    queryset = SubDomain.objects.all()

    def list(self, request):
        try:
            serializer = SubDomainSerializer(self.queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({"Error": "SubDomains not found"})

    def retrieve(self, request, pk=None):
        try:
            item = get_object_or_404(self.queryset, pk=pk)
            serializer = SubDomainSerializer(item)
            return Response(serializer.data)
        except:
            return Response({"Error": "Specified SubDomain not found"})


class TopicViewSet(ViewSet):
    queryset = Topic.objects.all()

    def get_queryset(self):
        self.queryset = Topic.objects.all()

    def list(self, request):
        try:
            serializer = TopicSerializer(self.queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({"Error": "Topics not found"})

    def retrieve(self, request, pk=None):
        try:
            item = get_object_or_404(self.queryset, pk=pk)
            serializer = TopicSerializer(item)
            return Response(serializer.data)
        except:
            return Response({"Error": "Specified Topic not found"})


class ProfessionViewSet(ViewSet):
    queryset = Profession.objects.all()

    def get_queryset(self):
        self.queryset = Profession.objects.all()

    def list(self, request):
        try:
            self.get_queryset()
            serializer = ProfessionSerializer(self.queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({"Error": "Professions not found"})

    def retrieve(self, request, pk=None):
        try:
            item = get_object_or_404(self.queryset, pk=pk)
            serializer = ProfessionSerializer(item)
            return Response(serializer.data)
        except:
            return Response({"Error": "Specified Profession not found"})


class CourseViewSet(ViewSet):
    queryset = Course.objects.all()

    def get_queryset(self):
        self.queryset = Course.objects.all().order_by("-rating")

    def list(self, request):
        try:
            self.get_queryset()
            serializer = CourseSerializer(self.queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({"Error": "Courses not found"})

    def retrieve(self, request, pk=None):
        try:
            item = get_object_or_404(self.queryset, pk=pk)
            serializer = CourseSerializer(item)
            return Response(serializer.data)
        except:
            return Response({"Error": "Specified Course not found"})


class TrendingTechViewSet(ViewSet):
    queryset = TrendingTech.objects.all()

    def get_queryset(self):
        self.queryset = TrendingTech.objects.all().order_by("-popularity")

    def list(self, request):
        try:
            self.get_queryset()
            serializer = TrendingTechSerializer(self.queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({"Error": "Trending Technologies not found"})

    def retrieve(self, request, pk=None):
        try:
            item = get_object_or_404(self.queryset, pk=pk)
            serializer = TrendingTechSerializer(item)
            return Response(serializer.data)
        except:
            return Response({"Error": "Specified Technology not found"})


class TrendingToolViewSet(ViewSet):
    queryset = TrendingTool.objects.all().order_by("-popularity")

    def get_queryset(self):
        self.queryset = TrendingTool.objects.all().order_by("-popularity")

    def list(self, request):
        try:
            self.get_queryset()
            serializer = TrendingToolSerializer(self.queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({"Error": "Trending Tools not found"})

    def retrieve(self, request, pk=None):
        try:
            item = get_object_or_404(self.queryset, pk=pk)
            serializer = TrendingTechSerializer(item)
            return Response(serializer.data)
        except:
            return Response({"Error": "Specified Tool not found"})


class RecommendationTestViewSet(ViewSet):
    queryset = RecommendationTest.objects.all().order_by("date")

    def get_queryset(self):
        self.queryset = RecommendationTest.objects.all().order_by("date")

    def list(self, request):
        try:
            self.get_queryset()
            serializer = RecommendationTestSerializer(self.queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({"Error": "Records not found"})

    def retrieve(self, request, pk=None):
        try:
            item = get_object_or_404(self.queryset, pk=pk)
            serializer = RecommendationTestSerializer(item)
            return Response(serializer.data)
        except:
            return Response({"Error": "Record not found"})

    def create(self, request):

        try:
            serializer = RecommendationTestSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            pred = mlpred.model1predict(request.data)
            dbid = pred + 1
            profession = get_object_or_404(Profession.objects.all(), pk=dbid)
            serializer.validated_data["profession"] = profession
            serializer.save()
            pserializer = ProfessionSerializer(profession)
            self.get_queryset()
            data = {"suggested_job_id": dbid, "suggested_job": pserializer.data}
            return Response(data)
        except:
            return Response({"Error": "Data Integrity Error"})


class ExpertViewSet(ViewSet):
    queryset = Expert.objects.all()

    def get_queryset(self):
        self.queryset = Expert.objects.all()

    def list(self, request):
        try:
            self.get_queryset()
            serializer = ExpertSerializer(self.queryset, many=True)
            for e in serializer.data:
                e["username"] = User.objects.get(id=e["user"]).name
            return Response(serializer.data)
        except:
            return Response({"Error": "Experts not found"})

    def retrieve(self, request, pk=None):
        try:
            item = get_object_or_404(self.queryset, pk=pk)
            serializer = ExpertSerializer(item)
            data = serializer.data
            data["username"] = User.objects.get(id=serializer.data["user"]).name
            return Response(data)
        except:
            return Response({"Error": "Expert not found"})

    def create(self, request):

        try:
            serializer = ExpertSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            self.get_queryset()
            return Response(serializer.data)
        except:
            return Response({"Error": "Data Integrity Error"})


class LoginViewSet(ViewSet):

    def create(self, request):
        try:
            serializer = LoginSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            email = serializer.data["email"]
            password = serializer.data["password"]
            user = User.objects.get(email=email)
            if user.check_password(password):
                data = {"id": user.id, "email": user.email, "username": user.name}
                return Response(data)
            else:
                return Response({"Error": "Wrong Password"})
        except:
            return Response({"Error": "Data Integrity Error"})


class SignUpViewSet(ViewSet):

    def create(self, request):
        try:
            serializer = SignUpSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            email = serializer.data["email"]
            username = serializer.data["username"]
            password = serializer.data["password"]
            user = User.objects.create_user(email=email, name=username, date_of_birth=datetime.now(),
                                            occupation='S')
            user.set_password(password)
            user.save()
            data = {"id": user.id, "email": user.email, "username": user.name}
            return Response(data)
        except:
            return Response({"Error": "Data Integrity Error"})


class SearchExpertViewSet(ViewSet):

    def create(self, request):
        try:
            serializer = SearchExpertSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            expert = Expert.objects.filter(languages=serializer.data["language"], topic=serializer.data["topic"])
            serializer = ExpertSerializer(expert, many=True)
            for e in serializer.data:
                e["username"] = User.objects.get(id=e["user"]).name

            data = {"Suggested Professor Details": serializer.data}
            return Response(data)
        except:
            return Response({"Error": "Search Filters Error"})

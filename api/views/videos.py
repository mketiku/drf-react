from joplin.models.query import Q
from in1_chamber_models.models.universal.media import Media
from in1_chamber_models.models.universal.day import Day

from rest_framework import viewsets
from rest_framework import filters, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import (
    SessionAuthentication, TokenAuthentication)

from api.serializers import MediaSerializer
from api.filters import (
    CategoryFilterBackend,
    SessionFilterBackend,
    ChamberFilterBackend,
    PublicVideoFilterBackend)

from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from drf_react.utils.tools import create_jupiter_backend


class ListMedia(APIView):
    """
    View to list all Media in the system.
    """

    def get(self, request, format=None):
        """
        Return a list of all media.
        """
        queryset = Media.objects.filter(
            Q(mediatype__startswith='video')).results
        media = MediaSerializer(queryset, many=True)
        return Response(media.data)


class ListMediaGenericView(generics.ListCreateAPIView):
    model = Media
    serializer_class = MediaSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return Media.objects.filter(Q(mediatype__startswith='video'))

    def put(self, request, *args, **kwargs):
        if request.data.get("lpid", None):
            Media.objects.filter(lpid=request.data.get('lpid'))
        pass

        # def post(self, request, *args, **kwargs):
        #     pass


class VideoViewSet(viewsets.GenericViewSet):
    """
    A simple ViewSet for listing or retrieving videos.
    """
    lookup_value_regex = '[\w_\.]+'

    # queryset = Media.objects.of(settings.DEFAULT_SESSION_YEAR, backend=create_jupiter_backend()).filter(
    #     Q(mediatype__startswith='video'))
    serializer_class = MediaSerializer

    def list(self, request):
        # q = self.filter_queryset(self.get_queryset())
        # serializer = MediaSerializer(q, many=True)

        import json
        ## LOAD DATA IN
        with open("data.json", 'r') as f:
            data = json.load(f)
        return Response(data)

        # import json
        # data = serializer.data
        # file_name = "data.json"
        # # DUMP DATA OUT
        # with open(file_name, 'w') as f:
        #     json.dump(data, f)

        # return Response(serializer.data)

    def retrieve(self, request, pk=None):
        video = Media.objects.get(lpid=pk, backend=create_jupiter_backend())
        serializer = MediaSerializer(video)
        return Response(serializer.data)

    def create(self, request):
        pass

    def update(self, request):
        pass

    def get_queryset(self):
        with create_jupiter_backend():
            return Media.objects.filter(
                Q(mediatype__startswith='video'))

    def filter_queryset(self, queryset):
        filter_backends = ()
        if 'chamber' in self.request.query_params:
            filter_backends = (ChamberFilterBackend,)

        if 'category' in self.request.query_params:
            filter_backends += (CategoryFilterBackend,)

        if 'public' in self.request.query_params:
            filter_backends += (PublicVideoFilterBackend,)

        if 'session_year' in self.request.query_params:
            filter_backends += (SessionFilterBackend,)

        for backend in list(filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, view=self)

        return queryset

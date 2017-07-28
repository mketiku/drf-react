from rest_framework import filters
from joplin.models.query import Q


class SessionFilterBackend(filters.BaseFilterBackend):
    """
    Filter to handle session year in videos
    """
    def filter_queryset(self, request, queryset, view):
        # return queryset.filter(session_year=request.GET.get("session_year"))
        return queryset.filter(sessionid__contains=request.GET.get("session_year"))  #TODO
        # #not sure why this is not working with session_year

class CoerceBooleanFilterBackened(filters.BaseFilterBackend):

    def sanitize_boolean(self, field):
        if field is not None:
            lc_value = field.lower()
            if lc_value == "true":
                value = True
            elif lc_value == "false":
                value = False
        return value


class PublicVideoFilterBackend(CoerceBooleanFilterBackened, filters.BaseFilterBackend):
    """
    Filter that handles chamber of video
    """
    def filter_queryset(self, request, queryset, view):
        value = self.sanitize_boolean(request.GET.get("public"))
        return queryset.filter(Q(is_public=value))


class ChamberFilterBackend(filters.BaseFilterBackend):
    """
    Filter that handles chamber of video
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(chamber=request.GET.get("chamber"))


class CategoryFilterBackend(filters.BaseFilterBackend):
    """
    Video category filter
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(category=request.GET.get("category"))

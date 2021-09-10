from . import models
import rest_framework
from rest_framework_gis import serializers as geo_serializers
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model



class UserMeSerializer(geo_serializers.GeoFeatureModelSerializer):
    url = rest_framework.serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        geo_field = "last_location"
        fields = (
            "id", "username", "email", "is_superuser", "is_staff",
            "is_active", "date_joined", "last_login", "url")

    def get_url(self, obj):
        return self.context["request"].build_absolute_uri(reverse("rest:user-username", kwargs={"uid": obj.pk}))


class UserOtherSerializer(geo_serializers.GeoFeatureModelSerializer):
    url = rest_framework.serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        geo_field = "last_location"
        fields = ("id", "username", "email", "url")

    def get_url(self, obj):
        return self.context["request"].build_absolute_uri(reverse("rest:user-username", kwargs={"uid": obj.pk}))

from rest_framework.serializers import ModelSerializer

from userapp.models import Student


class StudentModelSerializer(ModelSerializer):
    class Meta:
        model = Student
        # fields 中填写的是反序列化与序列化器中所需字段的并集
        fields = ["id","name", "password", "age", "sex", "bir","phone"]

        extra_kwargs = {
            # 指定此字段只参与反序列化或只参与序列化
            # "id": {
            #     "read_only": True
            # },
            # "password": {
            #     "write_only": True
            # },

        }


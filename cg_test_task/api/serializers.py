from rest_framework import serializers

from employees.models import Employee, JobRelation


class JobRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRelation
        fields = ("id", "job_title", "supervisor")

    def to_representation(self, instance):
        self.fields["supervisor"] = JobRelationSerializer(read_only=True)
        return super(JobRelationSerializer, self).to_representation(instance)


class EmployeeSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(
        slug_field="job_title", queryset=JobRelation.objects.all()
    )
    chief = serializers.StringRelatedField(
        source="post.supervisor.job_title", read_only=True
    )

    class Meta:
        model = Employee
        fields = (
            "name",
            "post",
            "employment_date",
            "salary",
            "chief",
        )

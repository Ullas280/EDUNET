from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer


@api_view(['GET'])
def get_jobs(request):
    keyword = request.GET.get('keyword', '')
    if keyword:
        jobs = Job.objects.filter(title__icontains=keyword) | Job.objects.filter(location__icontains=keyword)
    else:
        jobs = Job.objects.all()

    serializer = JobSerializer(jobs.order_by('-createdAt'), many=True)
    return Response({'jobs': serializer.data, 'success': True}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    serializer = JobSerializer(job)
    return Response({'job': serializer.data, 'success': True}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_recruiter_jobs(request):
    user = request.user
    jobs = Job.objects.filter(posted_by=user).order_by('-createdAt')
    serializer = JobSerializer(jobs, many=True)
    return Response({'jobs': serializer.data, 'success': True}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_job(request):
    data = request.data
    job = Job.objects.create(
        title=data.get('title',''),
        description=data.get('description',''),
        location=data.get('location',''),
        position=data.get('position',''),
        jobType=data.get('jobType',''),
        salary=data.get('salary',''),
        experience=int(data.get('experience') or 0),
        posted_by=request.user
    )
    serializer = JobSerializer(job)
    return Response({'job': serializer.data, 'success': True, 'message': 'Job posted successfully'}, status=status.HTTP_201_CREATED)


# Application endpoints
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def apply_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    user = request.user
    # Prevent duplicate applications
    if Application.objects.filter(job=job, applicant=user).exists():
        return Response({'message': 'Already applied', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

    application = Application.objects.create(job=job, applicant=user)
    # return updated job
    serializer = JobSerializer(job)
    return Response({'message': 'Applied successfully', 'job': serializer.data, 'success': True}, status=status.HTTP_201_CREATED)

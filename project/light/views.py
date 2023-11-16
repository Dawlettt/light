from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Device


# Create your views here.
@api_view(['GET', 'POST'])
def device_list(request):
    if request.method == "GET":
        try:
            queryset = Device.objects.all()
            response_data = [
                {"id": i.id, "name": i.name, "lacotion": i.location, 'state': i.state, 'is_on_time': i.is_on_time,
                 "is_off_time": i.is_off_time} for i in queryset]
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)})
    elif request.method == "POST":
        try:
            name = request.data.get('name')
            location = request.data.get('location')
            state = request.data.get('state')
            is_on_time = request.data.get('is_on_time')
            is_off_time = request.data.get('is_off_time')
            created_data = Device.objects.create(name=name, location=location, state=state, is_on_time=is_on_time,
                                                 is_off_time=is_off_time)
            if not created_data:
                Exception("Error")
            return Response({"id": created_data.id, "name": created_data.name, "location": created_data.location,
                             'state': created_data.state, "is_on_time": created_data.is_on_time,
                             "is_off_time": created_data.is_off_time})
        except Exception as e:
            return Response({'message': str(e)})


@api_view(["GET", 'PUT', 'DELETE'])
def device_detail(request, id):
    if request.method == 'PUT':
        try:
            name = request.data.get('name')
            location = request.data.get('location')
            state = request.data.get('state')
            is_on_time = request.data.get('is_on_time')
            is_off_time = request.data.get('is_off_time')
            update_data = Device.objects.filter(id=id).update(name=name, location=location, state=state,
                                                              is_on_time=is_on_time, is_off_time=is_off_time)
            if update_data > 0:
                data = Device.objects.get(id=id)
                return Response(
                    {"name": data.name, "location": data.location, "state": data.state,
                     "is_on_time": data.is_on_time,
                     "is_off_time": data.is_off_time})
            else:
                return Response({"message": "No device updated"})

        except Device.DoesNotExist:
            return Response({"message": "Device not found"})
        except Exception as e:
            return Response({"message": str(e)})
    elif request.method == 'GET':
        try:
            get_data = Device.objects.get(id=id)
            name = get_data.name
            location = get_data.location
            state = get_data.state
            is_on_time = get_data.is_on_time
            is_off_time = get_data.is_off_time
            return Response(
                {"id": id, 'name': name, "location": location, "state": state, "is_on_time": is_on_time,
                 "is_off_time": is_off_time},
                status=status.HTTP_200_OK)
        except Device.DoesNotExist:
            return Response({"message": "Device not found"})
        except Exception as e:
            return Response({'message': str(e)})
    elif request.method == "DELETE":
        try:
            Device.objects.filter(id=int(id)).delete()
            return Response({"message": "deleted"})
        except Device.DoesNotExist:
            return Response({"message": "Alarm not found"})
        except Exception as e:
            return Response({"message": str(e)})

from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
#---Validators------------------------
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should be start with R')
    
name = serializers.CharField(validators=[start_with_r])
class Meta:
    model = Student
    fields = ['name', 'roll', 'city']
    

#---Field Level Validation-------------------------
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value 
    
#---Object level Validation------------------------------------
def validate(self, data):
    nm = data.get('name')
    ct = data.get('city')
    if nm.lower() == 'veer' and ct.lower() != 'ranchi':
        raise serializers.ValidationError('city must be Ranchi')
    return data


    



# class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    # class Meta:
    #     model = Student
    #     fields = ['name', 'roll', 'city']
        # read_only_fields = ['name', 'roll']
        # extra_kwargs = {'name':{'read_only':True}}

#---Validators------------------------

# def start_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError('Name should be start with R')
    
    

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100, validators=[start_with_r])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)
    
    
#     def create(self, validate_data):
#         return Student.objects.create(**validate_data)
    
    
#     def update(self, instance, validated_data):
#         print(instance.name)
#         instance.name = validated_data.get('name', instance.name)
#         print(instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
        
        
# #---Field Level Validation-------------------------

#     def validate_roll(self, value):
#         if value >= 200:
#             raise serializers.ValidationError('Seat Full')
#         return value 
    
# #---Object Level Validation-------------------------

#     def validate(self, data):
#         nm = data.get('name')
#         ct = data.get('city')
#         if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
#             raise serializers.ValidationError('city must be Ranchi')
#         return data
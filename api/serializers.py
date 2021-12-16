from rest_framework import serializers

from inv.models import Producto


#Transforma la data de Django en objeto Json o Xms para utilizarlo del lado del front-end
class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = '__all__'

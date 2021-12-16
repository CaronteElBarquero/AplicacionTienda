from django.db import models
from bases.models import ClaseModelo



######################################### MODEL CATEGORIA ################################

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion De La Categoria',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion) #Imprime la descripcion de la categoria
    

    #Metodo para que Django se refiera a este modelo en plural se refiera a "Categorias"
    class Meta:
        verbose_name_plural = "Categorias"

###########################################################################################




####################################### MODEL SUB-CATEGORIA ###############################

class SubCategoria(ClaseModelo):
    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion De La Categoria',
    
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion,self.descripcion) #Imprime la descripcion de la categoria y de la subcategoria
        
    class Meta:
        verbose_name_plural="Sub Categorias"
        unique_together = ('categoria','descripcion')    

###############################################################################################




########################################### MODEL MARCA #######################################

class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion De La Marca',
        unique=True
    )


    def __str__(self):
        return '{}'.format(self.descripcion)
    
    
    class Meta:
        verbose_name_plural = "Marca"

################################################################################################




############################################ UNIDAD DE MEDIDA ###################################


class UnidadMedida(ClaseModelo):

    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion De La Unidad De Medida',
        unique=True

    )


    def _str_(self):
        return '{}'.format(self.descripcion)


    class Meta:
        verbose_name_plural = "Unidades de Medida"


###################################################################################################




############################################### PRODUCTO ##########################################

class Producto(ClaseModelo):

    codigo = models.CharField(
        max_length=20,
        unique=True
    )

    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto,self).save()
    
    class Meta:
        verbose_name_plural = "Productos"
        unique_together = ('codigo','codigo_barra')


###################################################################################################


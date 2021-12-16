from django import forms
from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto




########################################### FORMS CATEGORIA ###########################################


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['descripcion','estado']
        labels = {'descripcion' : "Descripción De La Categoría",
                   "estado" : "Estado"}
        widget = {'descripcion' : forms.TextInput}
    

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class' : 'form-control'
            })

########################################################################################################




########################################### FORMS SUBCATEGORIA ###########################################


class SubCategoriaForm(forms.ModelForm):

    #Esta funcion nos sirve para ver si alguna categoria esta activa o inactiva y asi desactivarla para que no se haga una subcategoria
    categoria = forms.ModelChoiceField(
        queryset = Categoria.objects.filter(estado = True)
        .order_by('descripcion')
    )

    class Meta:
        model = SubCategoria
        fields = ['categoria','descripcion','estado']
        labels = {'descripcion' : "Sub Categoría",
                   "estado" : "Estado"}
        widget = {'descripcion' : forms.TextInput}
    

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class' : 'form-control'
            })
        self.fields['categoria'].empty_label = "Seleccione Categoría"


##########################################################################################################





########################################### FORMS Marca ###########################################


class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = ['descripcion','estado']
        labels = {'descripcion': "Descripción de la Marca",
                   "estado":"Estado"}
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


###################################################################################################






########################################### FORMS UNIDAD MEDIDA ###########################################



class UMForm(forms.ModelForm):
    
    class Meta:
        model=UnidadMedida
        fields = ['descripcion','estado']
        labels = {'descripcion': "Descripción de la Marca",
                  "estado":"Estado"}
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


###########################################################################################################





########################################### FORMS PRODUCTO ###########################################


class ProductoForm(forms.ModelForm):

    class Meta:

        model=Producto
        fields=['codigo','codigo_barra','descripcion','estado', \
                'precio','existencia','ultima_compra',
                'marca','subcategoria','unidad_medida']
        exclude = ['usuarioModi','fechaModi','usuarioCrea','fechaCrea'] #Excluimos estos campos del formulario
        widget={'descripcion': forms.TextInput()}


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['ultima_compra'].widget.attrs['readonly'] = True  #Se hace para que no puedan ser editados por el usuario
        self.fields['existencia'].widget.attrs['readonly'] = True



######################################################################################################
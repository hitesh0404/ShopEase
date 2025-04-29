from django.shortcuts import render, redirect,get_object_or_404
from .models import Product
def product_list(request):
    print(request.user.user_type)
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

from django.views import View
from .models import Category,Brand
from account.models import User,SupplierProfile
from .models import Brand
class ProductCreate(View):
    def get(self,request): 
        categories = Category.objects.all()
        
        brands =  Brand.objects.all()
        context = {
            'categories' : categories,
            'brands' : brands,
        }
        return render(request,'inventory/create_product.html',context )
    

    def post(self,request):
        print(request.POST)
        name = request.POST.get('name')
        price = request.POST.get('price')
        if request.FILES:
            image = request.FILES.get('image')
        else:
            image = "product_images/main/gopro_hero10.jpg"
        quantity = request.POST.get('quantity')
        suplier = SupplierProfile.objects.first()
        brand = request.POST.get('brand')
        product = Product(
                            name = name,
                            price=float(price),
                            quantity=int(quantity),
                            image=image,
                            suplier=suplier,
                            brand=Brand.objects.get(pk=int(brand))
                        )
        product.save()
        categories = Category.objects.all()
        for category in categories:  #  [smartphone watch  homeapp]
            cat = request.POST.get(category.name,None)
            if cat:
                product.category.add(category)
        product.save() 
        return redirect('product_list')

         


        

def product_detail(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request,'inventory/product_detail.html',{'product':product})

def product_delete(request,id):
    product = get_object_or_404(Product,id=id)
    if request.method == "GET":
        return render(request,'inventory/delete_confirmation.html',{'product':product})
    elif request.method == "POST":
        product.delete()
    return redirect('product_list')

 
from .forms import ProductUpdateForm

# class ProductUpdate(View):
#     def get(self,request,id):
#         print("here ")
#         product = get_object_or_404(Product,pk=id)
#         form = ProductUpdateForm(initial={
#             'name':product.name
#         })
#         context =   { 
#             'form':form,
#             'product':product
#         }
#         return render(request,'inventory/product_update.html',context)
    
#     def post(self,request,id):
#         product = get_object_or_404(Product,pk=id)
#         form = ProductUpdateForm(request.POST)
#         if form.is_valid():
#             product.name = form.cleaned_data['name']
#             product.save()
#             return redirect('product_list')
#         else:
#             context =   { 
#             'form':form,
#             'product':product
#             }
#             return render(request,'inventory/product_update.html',context)
        

from .forms import ProductUpdateModelForm
class ProductUpdate(View):
    def get(self,request,id):
        product = get_object_or_404(Product,id=id)
        form = ProductUpdateModelForm(instance=product) 
        context =   { 
            'form':form,
            'product':product
        }
        return render(request,'inventory/product_update.html',context)
    def post(self,request,id):
        product = get_object_or_404(Product,id=id)
        print(request.POST,request.FILES)
        form = ProductUpdateModelForm(request.POST,request.FILES,instance=product) 
        if form.is_valid():
            form.save()
            return redirect("product_list")
        context =   { 
            'form':form,
            'product':product
        }
        return render(request,'inventory/product_update.html',context)
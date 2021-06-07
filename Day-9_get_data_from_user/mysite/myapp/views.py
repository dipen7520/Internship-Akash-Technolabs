from django.shortcuts import render

# Create your views here.

def form(request):

    if request.method == 'POST':
        fn = request.POST.get("fn")
        ln = request.POST.get("ln")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        contact= request.POST.get("contact")
        address= request.POST.get("address")
        zipcode = request.POST.get("zipcode")
        college = request.POST.get("college")
        dept = request.POST.get("dept")

        context={
            'fn':fn,
            'ln':ln,
            'email':email,
            'gender':gender,
            'contact':contact,
            'address' :address,
            'zipcode':zipcode,
            'college':college,
            'dept':dept
        }
        return render(request,'data.html',context)

    return render(request,"form.html")

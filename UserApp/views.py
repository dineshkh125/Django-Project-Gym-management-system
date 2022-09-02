from django.shortcuts import render,redirect
from AdminApp.models import Category,Gym
from UserApp.models import UserInfo,Cart,Payment,Order_Master
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def homepage(request):
    cats=Category.objects.all()
    gyms = Gym.objects.all()
    return render(request,"master.html",{"cats":cats,"gyms":gyms})

def ShowGyms(request,cid):
    cats=Category.objects.all()
    cat=Category.objects.get(id=cid) 
    gyms = Gym.objects.filter(category=cat)
    return render(request,"master.html",{"cats":cats,"gyms":gyms})

def ViewDetails(request,id):
    gym = Gym.objects.get(id=id)
    return render(request,"ViewDetails.html",{"gym":gym })

def Login(request):
    cats = Category.objects.all()
    if(request.method == "GET"):
        return render(request,"Login.html",{"cats":cats})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            user = UserInfo.objects.get(username = uname,password=pwd)
        except:
            return redirect(Login)
        else:
            request.session["uname"]=uname
            return redirect(homepage)
        
def SignUp(request):
    cats = Category.objects.all()
    if(request.method == "GET"):
        return render(request,"SignUp.html",{"cats":cats})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        email = request.POST["email"]

        user = UserInfo(uname,pwd,email)
        user.save()
        return redirect(homepage)


def Logout(request): 
    request.session.clear() 
    return redirect(homepage)


def Contactus(request):
    cats = Category.objects.all()
    return render(request,"ContactUs.html",{"cats":cats})



def addToCart(request):
    if(request.method == "POST"):
        if("uname" in request.session):
            user = UserInfo.objects.get(username = request.session["uname"])
            gym = Gym.objects.get(id = request.POST["gym_id"])
            qty = request.POST["qty"]   
            #Before adding to cart we need to check for duplicate entry
            try:
                cart_item = Cart.objects.get(user = user,gym=gym)
            except:
                #Add item to cart
                cart_item = Cart()
                cart_item.user = user
                cart_item.gym = gym
                cart_item.qty = qty
                cart_item.save()
                return redirect(homepage)
            else:
                return HttpResponse("Item already in cart..")              
        else:
            return redirect(Login)
    else:
        return redirect(Login)

def ShowAllCartItems(request): 
    uname = request.session["uname"] 
    user = UserInfo.objects.get(username = uname) 
    if(request.method == "GET"):        
        items = Cart.objects.filter(user = user) 
        cats = Category.objects.all() 
        total = 0 
        for item  in items: 
            total += float(item.gym.price) * float(item.qty) 
        request.session["total"] = total 
        return render(request,"ShowAllCartItems.html",{"items":items,"cats":cats}) 
    else: 
        action = request.POST["action"] 
        gym_id = request.POST["gym_id"] 
        gym = Gym.objects.get(id=gym_id) 
        item = Cart.objects.get(user=user,gym=gym) 
         
        if(action=="update"): 
            qty = request.POST["qty"] 
            item.qty = qty 
            item.save() 
        else:             
            item.delete()             
        return redirect(ShowAllCartItems)

def MakePayment(request): 
    if(request.method == "GET"): 
        return render(request,"MakePayment.html",{}) 
    else: 
        card_no = request.POST["card_no"] 
        cvv = request.POST["cvv"] 
        expiry = request.POST["expiry"] 
 
        try: 
            buyer = Payment.objects.get(card_no=card_no,cvv=cvv,expiry=expiry)  
            owner = Payment.objects.get(card_no="123",cvv="123",expiry="22/2030") 
            total = request.session["total"] 
            buyer.balance -= total 
            owner.balance += total 
            buyer.save() 
            owner.save() 
           
            #Delete the cart items 
            items = Cart.objects.filter(user = request.session["uname"])
            service_details = []

            for item in items:
                service_details.append(item.gym.service_name )

            o1 = Order_Master()
            o1.username = request.session["uname"]
            o1.date_of_order = datetime.now()
            o1.amount = float(request.session["total"])
            o1.service_details = ",".join(service_details)
            o1.save()
            print(o1)

            for item in items:
                item.delete()
            return render(request,"Payment_Success.html",{})
        except:
            return HttpResponse("Invalid Card Details")
            
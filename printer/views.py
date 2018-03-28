from django.shortcuts import render,redirect
from .models import UserInfo
import datetime
import os
from print.codePrintSetting import ADPASSWORD,PRINTER_NAME,CODE_PATH
# Create your views here

def index(request):
    if request.method == "GET":
        try:
            status = request.GET['status']
        except:
            status = ""
        return render(request,'printer/index.html',{
            "status" : status, 
        })
    elif request.method == "POST":
        team = request.POST['team']
        password = request.POST['password']
        code = request.POST['code']
        try:
            users = UserInfo.objects.get(team=team)
            if users.password != password:
                print("--"+password+"--"+users.password+"--")
                raise UserInfo.DoesNotExist

        except UserInfo.DoesNotExist:
            return redirect('/print?status=wrong')
        else:
            printcode(users.team,users.seat,code)
            return redirect('/print?status=success')


def printcode(team,seat,code):
    now = datetime.datetime.now()
    tmark = now.strftime("%H%M%S")
    fpath = CODE_PATH+team+"-"+tmark+".print"
    f = open(fpath,"w")
    f.write("Seat: "+seat+"\t"+"Team: "+team+"\t"+now.strftime("%H:%M:%S")+"\n"+"--------------------------------------------\n"+code+"\n")
    f.write("------------------End------------------")
    f.close()
    os.system("cat "+fpath+" | paps --font=10 --top-margin=10  --bottom-margin=10 --lpi=10 |lp -d "+PRINTER_NAME)


def adminpage(request):
    if request.method == "GET":
        try:
            status=request.GET['status']
        except:
            status=""
        userlist = UserInfo.objects.all()
        return render(request,'printer/admin.html',{
            'userlist' : userlist,
            'status' : status,
        })
    if request.method == "POST":
        if request.POST['password'] == ADPASSWORD:
            rawdata = request.POST['info']
            for line in rawdata.split("\n")[:-1]:
                [name,seat,password] = line.split(" ")
                print(name,seat,password)
                newUser = UserInfo(
                    team = name,
                    seat = seat,
                    password = password[:-1]
                )
                newUser.save()
            userlist = UserInfo.objects.all()
            return redirect('/cool?status=success')
        else:
            return redirect('/cool?status=wrong')

def delAction(request):
    if request.method == "POST":
        if request.POST['password'] == ADPASSWORD:
            userlist = UserInfo.objects.all()
            for user in userlist:
                user.delete()
            return redirect('/cool')
        else:
            return redirect('/cool?status=wrong')

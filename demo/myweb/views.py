from django.shortcuts import render, HttpResponse, redirect
import requests
import json
import re
from myweb.models import UserInfo

# Create your views here.
def index(request):
    return HttpResponse("欢迎使用！！！")


def lt(request):
    url = "http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2023/10/news"
    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "text/plain;charset=UTF-8",
        "Host": "www.chinaunicom.com.cn",
        "Referer": "http://www.chinaunicom.com.cn/news/list202310.html",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    }
    res = requests.get(url=url, headers=header)
    res.encoding = "utf-8"
    list = getList(res)
    print((list))
    return render(request, "lt.html", {"list": list})


def user_list(request):
    name = 'YJW'
    list = ['YY', 'JJ', 'WW']
    my_dict = {"name": "YJW", "age": 25}
    t = [{"name": "周杰轮", "age": 22}, {"name": "王丽红", "age": 32}]
    return render(request, "user_list.html", {"name": name, "list": list, "dic": my_dict, "t": t})


def getList(res):
    try:
        list = json.loads(res.text)
    except Exception as err:
        f = re.findall('href="(.*?)"', res.text)
        res2 = requests.get(url=f[0])
        res2.encoding = "utf-8"
        list = json.loads(res2.text)
    return list


def some(request):
    print(request.GET)
    return HttpResponse("！!!")
    # return redirect(to="https://www.youtube.com/")


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, "login.html")

    print(request.POST)
    print(request.POST.get('user'))
    print(request.POST.get('pwd'))
    list = UserInfo.objects.all()
    for i in list:
        print(i.user,i.age,i.pwd)
    return render(request, "login.html",{"error_msg":"登录失败，账号或者密码错误！"})

def info(request):
    list = UserInfo.objects.all()
    return render(request,"info.html",{"list":list})

def add(request):
    if request.method=="GET":
        return render(request, "add.html")
    elif request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        age = request.POST.get('age')
        UserInfo.objects.create(user=user,pwd=pwd,age=age)
        return redirect("/info")

def deleteInfo(request):
    if request.method == "GET":
        id = request.GET.get('id')
        UserInfo.objects.filter(id=id).delete()
        return redirect("/info")
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from core.models import Usuario, Compras
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse
from django.contrib.auth.models import User
import requests


# Create your views here.


def logout_user(request):
    logout(request)
    return redirect('/')


def cadastro_usuario(request):
    return render(request, 'register.html')


def submit_cadastro_usuario(request):
    if request.POST:
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        password = request.POST.get('password')
        Usuario.objects.create(
            nome=nome,
            cpf=cpf,
            email=email,
            password=password
        )
        User.objects.create_user(
            username=email,
            email=email,
            password=password
        )
    return redirect('/')


def login_user(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/main/')
        else:
            messages.error(request, 'Usuário ou senha inválida.')

    return redirect('/')


@login_required(login_url='/login/')
def main(request):
    return render(request, 'main.html')


@login_required(login_url='/login/')
def cadastro_compra(request):
    return render(request, 'cadastro-compras.html')


@login_required(login_url='/login/')
def submit_cadastro_compra(request):
    if request.POST:
        codigo = request.POST.get('codigo')
        cpf_compra = request.POST.get('cpf_compra')
        valor = float(request.POST.get('valor'))
        data = request.POST.get('data')
        print(data)
        if cpf_compra == '15350946056':
            status = 'Aprovado'
        else:
            status = 'Em validação'

        if valor > 1500:
            percent_cashback = 20
            cashback = valor * 0.2
        elif valor > 1000:
            percent_cashback = 15
            cashback = valor * 0.15
        else:
            percent_cashback = 10
            cashback = valor * 0.1

        Compras.objects.create(
            codigo=codigo,
            cpf_compra=cpf_compra,
            valor=valor,
            data=data,
            status=status,
            percent_cashback=percent_cashback,
            cashback=cashback
        )
    return redirect('/main/')


@login_required(login_url='/login/')
def listar_compras(request):
    email = request.user
    usuario = Usuario.objects.filter(email=email)
    cpf_logado = [{'cpf': dados.cpf} for dados in usuario]
    cpf_usuario = cpf_logado[0]
    cpf = cpf_usuario['cpf']
    compra = Compras.objects.filter(cpf_compra=cpf)
    dados = {'compras': compra}
    print(dados)
    return render(request, 'lista-compras.html', dados)


@login_required(login_url='/login/')
def cashback(request):
    email = request.user
    cashback_api = Usuario.objects.filter(email=email)
    cpf_logado = [{'cpf': dados.cpf} for dados in cashback_api]
    cpf = cpf_logado[0]
    parametro = cpf['cpf']
    api_request = requests.get(
        f'https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf={parametro}'
    )
    dados = api_request.json()
    response = dados['body']
    return render(request, 'cashback.html', response)











from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tender.forms.project_form import ProjectForm
from tender.models.company_model import Company
from tender.models.item_model import Item
from tender.models.project_model import Project
from tender.models.registrant_model import Registrant
from tender.forms.company_form import CompanyForm
from tender.forms.registrant_form import RegistrantForm
from tender.serializers.company_serializer import CompanySerializer
from tender.serializers.item_serializer import ItemSerializer
from tender.serializers.project_serializer import ProjectSerializer
from tender.serializers.registrant_serializer import RegistrantSerializer

def dashboard(request):
    context = { 'is_admin': True }
    return render(request, "tender.html", context)

def all_companies(request):
    return render(request, "all_companies.html")

def one_company(request, id):
    context = { 'id': id }
    return render(request, "one_company.html", context)

def all_projects(request):
    return render(request, "all_projects.html")

def one_project(request, id):
    context = { 'id': id }
    return render(request, "one_project.html", context)

def join_tender(request, id):
    context = { 'id': id }
    return render(request, "join_tender.html", context)

@api_view(['GET','POST'])
def all_companies_json(request):
    def get():
        # Get all companies (Public)
        companies = Company.objects.all()
        companies_serialized = CompanySerializer(instance=companies, many=True)
        return Response(companies_serialized.data, status=status.HTTP_200_OK)
    
    def post():
        # Create a new company (User)
        if (request.user.is_authenticated):
            form = CompanyForm(request.POST)
            if (form.is_valid()):
                new_company = Company.objects.create(
                    user = request.user,
                    company_name = form.cleaned_data.get('company_name'),
                    pt_name = form.cleaned_data.get('pt_name'),
                    npwp = form.cleaned_data.get('npwp'),
                )
                new_company_serialized = CompanySerializer(instance=new_company)
                return Response(new_company_serialized.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if (request.method == 'GET'): return get()
    elif (request.method == 'POST'): return post()

@api_view(['GET'])
def my_companies_json(request):
    def get():
        if (request.user.is_authenticated):
            companies = Company.objects.filter(user=request.user)
            companies_serialized = CompanySerializer(instance=companies, many=True)
            return Response(companies_serialized.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if (request.method == 'GET'): return get()

@api_view(['GET','PUT'])
def one_company_json(request, id):
    def get():
        # Get company :id details (Public)
        company = Company.objects.get(id=id)
        company_serialized = CompanySerializer(instance=company)
        return Response(company_serialized.data, status=status.HTTP_200_OK)

    def put():
        # Edit company :id (Company)
        # TODO: Later
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'PUT'): return put()

@api_view(['GET','POST'])
def all_projects_json(request):
    def get():
        # Get all projects (Public)
        projects = Project.objects.all()
        projects_serialized = ProjectSerializer(instance=projects, many=True)
        return Response(projects_serialized.data, status=status.HTTP_200_OK)
    
    def post():
        # Create new project (Admin)
        if (request.user.is_authenticated):
            # TODO: Check admin
            form = ProjectForm(request.POST)
            print(form.is_valid())
            if (form.is_valid()):
                new_project = Project.objects.create(
                    title = form.cleaned_data.get('title'),
                    description = form.cleaned_data.get('description'),
                )
                new_project_serialized = ProjectSerializer(instance=new_project)
                return Response(new_project_serialized.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if (request.method == 'GET'): return get()
    elif (request.method == 'POST'): return post()

@api_view(['GET','PUT'])
def one_project_json(request, id):
    def get():
        # Get project :id details (Public)
        project = Project.objects.get(id=id)
        project_serialized = ProjectSerializer(instance=project)
        return Response(project_serialized.data, status=status.HTTP_200_OK)

    def put():
        # Edit project :id (Admin)
        # TODO: Later
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'PUT'): return put()

@api_view(['GET','POST'])
def all_registrants_json(request):
    # TODO: Later
    pass

@api_view(['GET','POST','PUT'])
def one_registrant_json(request, id):
    def get():
        # Get registrant :id details (Public)
        registrant = Registrant.objects.get(id=id)
        registrant_serialized = RegistrantSerializer(instance=registrant)
        return Response(registrant_serialized.data, status=status.HTTP_200_OK)

    def post():
        # Add new registration to project :id (Company) 
        if (request.user.is_authenticated):
            form = RegistrantForm(request.POST)
            if (form.is_valid()):
                company = form.cleaned_data.get('company')
                print(company.id)
                company = Company.objects.get(id=company.id)
                project = Project.objects.get(id=id)
                if (company != None):
                    new_registrant = Registrant.objects.create(
                        project = project,
                        company = company
                    )
                    new_registrant_serialized = RegistrantSerializer(instance=new_registrant)
                    return Response(new_registrant_serialized.data, status=status.HTTP_201_CREATED)
                    return Response(status=status.HTTP_201_CREATED)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put():
        # Edit registration :id (Company)
        # TODO: Later
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'PUT'): return put()
    elif (request.method == 'POST'): return post()

@api_view(['POST'])
def item_json(request):
    def post():
        registrant_id = request.body.get('registrant_id')
        quantity = request.body.get('quantity')
        price = request.body.get('price')

        registrant = Registrant.objects.get(id=registrant_id)
        registrant.offer_price += price * quantity
        registrant.save()

        new_item = Item.objects.create(
            registrant_id = registrant_id,
            name = request.body.get('name'),
            quantity = quantity,
            price = price,
            description = request.body.get('description'),
        )
        new_item_serialized = ItemSerializer(instance=new_item)
        return Response(new_item_serialized, status=status.HTTP_201_CREATED)

    if (request.method == 'POST'): return post()
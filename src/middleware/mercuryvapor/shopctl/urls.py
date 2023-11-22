from django.urls import path
from .views import *

urlpatterns = [
    path('createcustomer', create_customer),
    path('customers', get_customers),
    path('editcustomer/<int:custid>', edit_customer),
    path('deletecustomer/<int:custid>', delete_customer),
    path('createsource', create_source),
    path('sources', get_sources),
    path('editsource/<int:srcid>', edit_source),
    path('deletesource/<int:srcid>', delete_source),
    path('categories', get_categories),
    path('createcategory', create_category),
    path('editcategory/<int:catid>', edit_category),
    path('deletecategory/<int:catid>', delete_category),
    path('procbills', get_procbills),
    path('createprocbill/<int:srcid>', create_procbill),
]


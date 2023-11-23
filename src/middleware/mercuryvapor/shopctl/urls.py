from django.urls import path
from .views import *

urlpatterns = [
    # customer curd
    path('createcustomer', create_customer),
    path('customers', get_customers),
    path('editcustomer/<int:custid>', edit_customer),
    path('deletecustomer/<int:custid>', delete_customer),
    # source curd
    path('createsource', create_source),
    path('sources', get_sources),
    path('editsource/<int:srcid>', edit_source),
    path('deletesource/<int:srcid>', delete_source),
    # category curd
    path('categories', get_categories),
    path('createcategory', create_category),
    path('editcategory/<int:catid>', edit_category),
    path('deletecategory/<int:catid>', delete_category),
    # procbill curd
    path('procbills', get_procbills),
    path('createprocbill', create_procbill),
    path('procbills', get_procbills),
    path('editprocbill/<int:pbid>', edit_procbill),
    # purchase curd
    path('createpurchase', create_purchase),
    path('purchases', get_purchases),
    # batch curd
    path('createbatch', create_batch),
    path('batches', get_batches),
    path('editbatch/<int:bid>', edit_batch),
    # custbill curd
    path('createcustbill', create_custbill),
    path('custbills', get_custbills),
    path('custbillpaid/<int:cbid>', custbill_paid),
    # sale curd
    path('createsale', create_sale),
]


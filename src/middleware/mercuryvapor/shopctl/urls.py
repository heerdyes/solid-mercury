from django.urls import path
from .views import *

urlpatterns = [
    # templates
    path('ui/customers', custpage),
    path('ui/sources', srcpage),
    path('ui/categories', catpage),
    path('ui/procbills', procbillpage),
    path('ui/purchases', purchasepage),
    # customer curd
    path('api/createcustomer', create_customer),
    path('api/customers', get_customers),
    path('api/editcustomer/<int:custid>', edit_customer),
    path('api/deletecustomer/<int:custid>', delete_customer),
    # source curd
    path('api/createsource', create_source),
    path('api/sources', get_sources),
    path('api/editsource/<int:srcid>', edit_source),
    path('api/deletesource/<int:srcid>', delete_source),
    # category curd
    path('api/categories', get_categories),
    path('api/createcategory', create_category),
    path('api/editcategory/<int:catid>', edit_category),
    path('api/deletecategory/<int:catid>', delete_category),
    # procbill curd
    path('api/procbills', get_procbills),
    path('api/createprocbill', create_procbill),
    path('api/procbills', get_procbills),
    path('api/editprocbill/<int:pbid>', edit_procbill),
    # purchase curd
    path('api/createpurchase', create_purchase),
    path('api/purchases', get_purchases),
    # batch curd
    path('api/createbatch', create_batch),
    path('api/batches', get_batches),
    path('api/editbatch/<int:bid>', edit_batch),
    # custbill curd
    path('api/createcustbill', create_custbill),
    path('api/custbills', get_custbills),
    path('api/custbillpaid/<int:cbid>', custbill_paid),
    # sale curd
    path('api/createsale', create_sale),
    path('api/sales', get_sales),
]


from rest_framework.permissions import BasePermission, SAFE_METHODS, DjangoModelPermissions

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
    

class FullDjangoModelPermissions(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']


#this is for creating user defined permissions in the admin console 
class ViewCustomerHistoryPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.has_perm('store.view_history'))
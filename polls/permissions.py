from rest_framework.permissions import BasePermission

class StaffPermissionClass(BasePermission):
    def has_permission(self, request, view):
        if request.user.id ==2:
            return True
        return False    

class AdminPermissionClass(BasePermission):
    def has_permission(self, request, view):
        if request.user.id == 3:   
            return True
        return False         

class OwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.user.id:
            return True
        return False        
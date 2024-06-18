from django.http import HttpResponse
def homePage(request):
    return HttpResponse("<ol><a href='user/'><li>user list</li></a><a href='user/vendor/'><li>Vendors List</li></a><a href='admin/'><li>Admin pannel</li></a><a href='product/'><li>product List</li></a><a href='category/'><li>Category List</li></a><a href='cart/'><li>Cart List</li></a><a href='favorite/'><li>wish List</li></a></ol>")
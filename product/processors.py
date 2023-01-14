from .models import Category

def menu_links(request):
    cat = Category.objects.all()
    return dict(cat=cat)
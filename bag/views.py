from django.shortcuts import render


def view_bag(request):
    """ view for showing the bag contents page """
    return render(request, 'bag/bag.html')

from django.shortcuts import render

def home_page(request):

    if request.method == 'POST':
        order = request.POST.get('order')
        address = request.POST.get("address")

        print(order * 10)
        return render(request, 'waimai/home_page.html', {'address': address, 'order': order})

    return render(request, 'waimai/home_page.html')
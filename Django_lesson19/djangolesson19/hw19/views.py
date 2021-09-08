from django.shortcuts import render
from .forms import Aviaticketform


def aviaticket(request):
    form = Aviaticketform()
    if request.method == 'POST':
        form = Aviaticketform(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            from_him = data.get('from_him')
            where_him = data.get('where_him')
            what = int(data.get('what'))*100
            date = data.get('date')
            return render(request, 'ticket.html', {'name':name, 'from_him':from_him, 'where_him':where_him, 'what':what, 'date':date})
        else:
            return render(request, 'ticket.html', {'error': 'Data is not valid'})
    else:
        return render(request, 'ticket.html', {'form': form,})

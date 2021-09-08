from django.shortcuts import render
from .forms import WriteLineForm

def index(request):

    if request.method == 'POST':
        form = WriteLineForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            firstname = data.get('firstname')
            lastname = data.get('lastname')
            age = data.get('age')
            print(firstname)
            return render(request, 'index.html')
        else:
            data_dict = form.errors
            print(f'errors in {data_dict}')
            return render(request, 'index.html')
    else:
        form = WriteLineForm()

        return render(request, 'writeline_form.html', {'form': form})
# Create your views here.

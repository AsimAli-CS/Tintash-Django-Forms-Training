from django.shortcuts import render
from django.http import HttpResponseRedirect

def get_name(request):
    if request.method == 'POST':
        # Handle the form submission
        submitted_name = request.POST['your_name']
        # Store the submitted name in the session
        request.session['submitted_name'] = submitted_name
        # Redirect after POST
        return HttpResponseRedirect('/thanks/')
    
    # If the request method is GET, render the empty form
    return render(request, 'index.html', {'current_name': ''})

def thanks(request):
    # Retrieve the submitted name from the session
    submitted_name = request.session.get('submitted_name', '')
    return render(request, 'thanks.html', {'submitted_name': submitted_name})

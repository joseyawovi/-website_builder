from django.shortcuts import render,redirect
from .forms import BusinessDetailsForm
from .models import Template, BusinessDetails, UserWebsite

def homepage(request):
    return render(request, 'builder/homepage.html')


def business_details(request):
    if request.method == 'POST':
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            business = form.save()
            return redirect('template_selection')  # Redirect to template selection page
    else:
        form = BusinessDetailsForm()
    return render(request, 'builder/business_details.html', {'form': form})


def template_selection(request):
    templates = Template.objects.all()
    if request.method == 'POST':
        selected_template_id = request.POST.get('template')
        business_details = BusinessDetails.objects.latest('id')  # Get latest business details
        selected_template = Template.objects.get(id=selected_template_id)

        # Save user website with the selected template
        UserWebsite.objects.create(business_details=business_details, selected_template=selected_template)

        return redirect('website_preview')  # Redirect to preview page
    
    return render(request, 'builder/template_selection.html', {'templates': templates})

def website_preview(request):
    user_website = UserWebsite.objects.latest('created_at')  # Get the most recent website
    business_details = user_website.business_details
    selected_template = user_website.selected_template

    # Prepare context with business details to inject into the template
    context = {
        'business_name': business_details.name,
        'business_description': business_details.description,
        'template': selected_template.html_file,
        'static_url': '/static/'
    }

    return render(request, 'builder/website_preview.html', context)











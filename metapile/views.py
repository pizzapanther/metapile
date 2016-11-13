from django.template.response import TemplateResponse

def data_explorer (request):
  return TemplateResponse(request, 'data-explorer.html', {})
  
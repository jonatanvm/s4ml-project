import mimetypes

from django.http import JsonResponse, Http404, HttpResponse
from django.shortcuts import render, redirect

from investing.forms import MLModelForm
from investing.models import Price, Model, Run, Outcome, Prediction
from investing.tables import ModelTable, RunTable, PredictionTable


def calculate_profit(model_id=None):
    profit = 0
    outcomes = Outcome.objects.all() if not model_id else Outcome.objects.filter(prediction__model_id=model_id).all()
    for outcome in outcomes:
        price_before = Price.objects.filter(id=outcome.prediction.predictor - 1).first()
        if price_before:
            if outcome.value > price_before.bid and outcome.prediction.value > price_before.bid:
                profit += outcome.value - price_before.bid
            elif outcome.value < price_before.bid and outcome.prediction.value < price_before.bid:
                profit += price_before.bid - outcome.value
            else:
                profit -= abs(price_before.bid - outcome.value)

    return profit


def index(request):
    context = {
        'production_table': ModelTable(Model.objects.filter(type='P').all()),
        'test_table': ModelTable(Model.objects.filter(type='T').all()),
    }
    return render(request, 'index.html', context)


def runs(request, id):
    table = RunTable(Run.objects.filter(model_id=id).all())
    table.paginate(page=request.GET.get("page", 1), per_page=10)
    context = {
        'table': table,
    }
    return render(request, 'runs.html', context)


def predictions(request, id):
    table = PredictionTable(Prediction.objects.filter(model_id=id).all())
    table.paginate(page=request.GET.get("page", 1), per_page=10)
    context = {
        'table': table,
    }
    return render(request, 'runs.html', context)


def get_profit(request):
    return JsonResponse({'profit': calculate_profit()})


def get_latest_price_data(request):
    data = {'bid': [], 'ask': []}
    for dp in (Price.objects.values('bid', 'ask', 'date').all()[:30]):
        data['bid'].append({'y': dp['bid'], 't': dp['date']})
        data['ask'].append({'y': dp['ask'], 't': dp['date']})
    return JsonResponse({'data': data})


def upload_model(request):
    if request.method == 'POST':
        formset = MLModelForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect('index')
    else:
        formset = MLModelForm()
    return render(request, 'add_model.html', {'formset': formset})


def get_file(request, file_path):
    file_location = "uploads/" + file_path
    try:
        with open(file_location, 'r') as f:
            file_data = f.read()
            file_mime = mimetypes.guess_type(file_location)
            response = HttpResponse(file_data, content_type=file_mime[0])
            response['Content-Disposition'] = f'attachment; filename="{file_path}"'
            return response
    except IOError:
        raise Http404()


def study_log(request, study_log_id):
    file_location = f"uploads/study-logs/studylog{study_log_id}.md"
    try:
        with open(file_location, 'r') as f:
            file_data = f.read()
            return render(request, 'markdown.html', {'study_log': file_data})
    except IOError:
        raise Http404()


def readme(request):
    file_location = f"README.md"
    try:
        with open(file_location, 'r') as f:
            file_data = f.read()
            return render(request, 'markdown.html', {'study_log': file_data})
    except IOError:
        raise Http404()

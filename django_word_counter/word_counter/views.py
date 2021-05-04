from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def result(request):
    sentence = request.POST.get('sentence')

    words = sentence.split()

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    word_count_list = list(word_counts.items())

    word_count_list.sort(key=lambda t: -t[1])

    response = {
        'word_counts': word_count_list
    }

    return render(request, 'result.html', response)

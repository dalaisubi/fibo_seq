
from django.views.generic import ListView
from django.shortcuts import render
from .stats_middleware import StatsMiddleware


def FibonacciView(request):
	f0 = int(request.GET.get('f0', 0))
	f1 = int(request.GET.get('f1',0 ))
	n = int(request.GET.get('N', 0))
	i=2
	while i<n:
	    f0,f1 = f1,f0+f1
	    i += 1   
	
	context = {
		"result": f1
	}

	return render(request, "fibo_seq/index.html", context)
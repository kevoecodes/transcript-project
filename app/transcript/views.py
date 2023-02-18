import os

from django.http import HttpResponse
from django.shortcuts import render, redirect

from app.transcript.pdf import GeneratePDF


def downloadTranscript(request, pk):
    if request.method == "GET":
        GeneratePDF.generate(pk)
        try:
            with open(f'StudentTranscript_{pk}.pdf', 'rb') as file:
                # Set the content type as PDF
                response = HttpResponse(file.read(), content_type='application/pdf')
                # Set the content-disposition as attachment to prompt download
                response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(f'StudentTranscript_{pk}.pdf')
                return response
        except Exception as e:
            print(e)
            pass

    return redirect('/students')

from django.shortcuts import render

# Create your views here.
# htop_project/htop_app/views.py
import subprocess
import datetime
import os
import socket
from django.http import HttpResponse
from django.shortcuts import render

def htop(request):
    
    full_name = "Parth Chaturvedi"  
    
    # Get the system username
    username = os.getenv('USER', subprocess.getoutput('whoami'))
    
    # Get the server time in IST
    utc_time = datetime.datetime.utcnow()
    ist_time = utc_time + datetime.timedelta(hours=5, minutes=30)
    server_time = ist_time.strftime("%Y-%m-%d %H:%M:%S IST")
    
    # Get top output
    top_output = subprocess.getoutput('top -b -n 1')
    
    # Prepare the context for template rendering
    context = {
        'full_name': full_name,
        'username': username,
        'server_time': server_time,
        'top_output': top_output,
    }
    
    # Return plain text response
    response_text = f"""Name: {full_name}
Username: {username}
Server Time in IST: {server_time}

Top Output:
{top_output}
"""
    return HttpResponse(f"<pre>{response_text}</pre>", content_type="text/html")
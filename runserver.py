"""
This script runs the My_site application using a development server.
"""

from Room_App import app
import os


app.secret_key = os.urandom(24)
port = int(os.environ.get('PORT',8000))
app.run(debug=True, port=8000)

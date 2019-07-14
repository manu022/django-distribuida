# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn distribuida.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3

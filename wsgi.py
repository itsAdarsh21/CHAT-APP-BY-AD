from app import app, socketio

if __name__ == "_main_":  # Fixed the spacing
    socketio.run(app)  # Properly indented the line

#gunicorn and WSGI (web server gateway interface)


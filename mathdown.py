from bottle import route, run, static_file
import webview
import threading

@route('/')
def index():
    return static_file('mathdown.html', root='.')

@route('/<filepath:path>')
def resource(filepath):
    return static_file(filepath, root='.')

def start_server():
    run(host='localhost', port='8000')
    
if __name__ == '__main__':
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()

    webview.create_window('MathDown', 'http://localhost:8000', width=1024,
                           height=640, background_color='#212121')

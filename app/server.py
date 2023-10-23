import os
import cherrypy
from django.conf import settings
from config.wsgi import application
from cherrypy.process.plugins import Daemonizer


admin_static_path = os.path.join(os.path.dirname(settings.BASE_DIR), 'app/staticfiles/admin')
rest_framework_path = os.path.join(os.path.dirname(settings.BASE_DIR), 'app/staticfiles/rest_framework')

# Монтирование статических файлов Django
cherrypy.tree.mount(None, '/static/admin', { # Прямой путь к стилям
    '/': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': admin_static_path,
    }
})

cherrypy.tree.mount(None, '/static/rest_framework', {
    '/': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': rest_framework_path,
    }
})

cherrypy.tree.graft(application, '/')
cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8000,
                        'engine.autoreload.on': False,
                        })

if __name__ == '__main__':
    # daemonizer = Daemonizer(cherrypy.engine)
    # daemonizer.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()
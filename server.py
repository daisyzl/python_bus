#!/usr/bin/env python
#-*-coding:utf-8-*-   
#说明:
#!/usr/bin/env python
#-*-coding:utf-8-*-
#说明:
import tornado

from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.listen(7000)
    tornado.ioloop.IOLoop.current().start()
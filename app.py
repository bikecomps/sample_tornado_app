# app.py
# Starts HTTPServer with an application instance
import tornado.ioloop
import tornado.web
import os
class TextHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class SimpleHTMLHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h2>Now this is HTML!</h2><p>My paragraph</p>")

class AnotherHTMLHandler(tornado.web.RequestHandler):
    def get(self):
        # assume we magically got all our names in some list
        members = ["Daniel", "Carlton", "Will", "Carissa", "Mikenna", "Jonathan"]
        self.render("teamdisplay.html", title = "Go Bikes!", team = members)


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    settings = {
        "static_path" : os.path.join(dirname, "static"),
        "template_path" : os.path.join(dirname, "template")
    }

    application = tornado.web.Application([
        # define routes here
        # you can use regular expressions if you want BTW
        (r'/', TextHandler),
        (r'/text', TextHandler),
        (r'/embedhtml', SimpleHTMLHandler),
        (r'/importhtml', AnotherHTMLHandler)
    ], **settings)
    
    # make app listen on any port you want (as long as there's no collision)
    application.listen(8888)

    tornado.ioloop.IOLoop.instance().start()

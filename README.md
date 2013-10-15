This page contains instructions on the easiest way to setup tornado on your "local" computer:

* First, install tornado using `pip install tornado`. If you don't have `pip`, first install that. It's a tool that makes the management of Python packages seamless.

* Next, run app.py to start the server : `python app.py`.

* Open `app.py`. It contains rules to handle HTTP requests to the server. For 
example, a request to `http://localhost:8888/embedhtml` is routed to
`SimpleHTMLHandler`, which just writes back some HTML to the client.
`AnotherHTMLHandler` handles a `GET` request to `importhtml`. This 
RequestHandler renders the contents of `teamdisplay.html`, passing
`title` and `team` as arguments to be displayed/manipulated
by the HTML file. 

* That's it! [See Documentation](http://www.tornadoweb.org/en/stable/documentation.html).

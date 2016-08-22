import web

// Routes
urls = (
  '/hello', 'Index'
)

// Start App
app = web.application(urls, globals())

// Initial Render
render = web.template.render('templates/', base="layout")

class Index:
    def GET(self):
        # Old code not using template format
        '''
        form = web.input(name="Nobody", greet=None)
        form = web.input(greet="Sup")

        if form.greet:
            greeting = "%s, %s" % (form.greet, form.name)
            return render.index(greeting = greeting)
        else:
            return "Error: greet is required."
        '''

        # Render form template
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)

        # Handle Image Upload
        x = web.input(pic={})
        filedir = 'images/'
        if 'pic' in x:
            filepath=x.pic.filename.replace('\\','/')
            filename=filepath.split('/')[-1]
            fout = open(filedir + '/' + filename, 'w')
            fout.write(x.pic.file.read())
            fout.close()
        #raise web.seeother('/hello')

        return render.index(greeting = greeting)
if __name__ == "__main__":
    app.run()

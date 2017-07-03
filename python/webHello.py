import web
render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/new', 'thing'
)

class index:
    def GET(self):
    	name = 'Cash'
    	return render.index(name)

class thing:
	def GET(self):
		return render.thing()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
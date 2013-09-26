import web, json

urls = (
	'/', 'home',
)

#where templates live:
render = web.template.render('templates/')

class home:
	def GET(self): #show displaydata.html
		return render.displaydata()

	def POST(self):
		input = web.input()
		web.header('Content-Type', 'application/json')
		return json.dumps({
			'txt' : input.mod.lower(),
			'dat' : "%.3f" % float(input.num)
		})

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()

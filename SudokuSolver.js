var hapi = require('hapi');

var server = new hapi.Server('localhost', 8000);

server.views({
	engines: {
		jade: 'jade'
	},
	path: './templates'
});

server.route({ 
	method: 'GET', 
	path: '/', 
	handler: function (request, reply) {
	
		var context = {
	        title: 'Hapi'
	    };
	    
	    if (request.query.name) {
	        context.name = request.query.name;
	    };


	    reply.view('index').header('SudokuSolver', '0');
	}
});


server.start(function () {
    console.log("Running at http://localhost:8000/");
})

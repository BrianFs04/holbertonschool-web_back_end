const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
	describe('/ endpoint', () => {
		it('Status code and route result', (done) => {
			request('http://localhost:7865', 'GET', (err, res, body) => {
				if (err) throw err;
				expect(res.statusCode).to.equal(200);
				expect(body).to.equal('Welcome to the payment system');
				done();
			});
		});
	});
});

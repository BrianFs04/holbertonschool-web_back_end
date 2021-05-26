const request = require('request');
const { expect } = require('chai');

describe('Page', () => {
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
	describe('/cart/:id endpoint', () => {
		it('Status code and id type', (done) => {
			request(
				'http://localhost:7865/cart/12',
				'GET',
				(err, res, body) => {
					if (err) throw err;
					expect(res.statusCode).to.equal(200);
					expect(body).to.equal('Payment methods for cart 12');
					done();
				}
			);
		});
	});
	describe('/cart/:isNaN endpoint', () => {
		it('Status code and id type', (done) => {
			request('http://localhost:7865/cart/x', 'GET', (err, res) => {
				if (err) throw err;
				expect(res.statusCode).to.equal(404);
				done();
			});
		});
	});
});

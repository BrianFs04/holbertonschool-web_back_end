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
	describe('/available_payments endpoint', () => {
		it('Status code and route result', (done) => {
			request(
				'http://localhost:7865/available_payments',
				'GET',
				(err, res, body) => {
					if (err) throw err;
					expect(res.statusCode).to.equal(200);
					expect(body).to.equal(
						'{"payment_methods":{"credit_cards":true,"paypal":false}}'
					);
					done();
				}
			);
		});
	});
	describe('/login endpoint', () => {
		it('Status code and route result', (done) => {
			const options = {
				url: 'http://localhost:7865/login',
				method: 'POST',
				json: {
					userName: 'Betty',
				},
			};
			request(options, (err, res, body) => {
				if (err) throw err;
				expect(res.statusCode).to.equal(200);
				expect(body).to.equal('Welcome Betty');
				done();
			});
		});
	});
});

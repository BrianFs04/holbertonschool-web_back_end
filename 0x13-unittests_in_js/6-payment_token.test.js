const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromApi', () => {
	it('Async function', (done) => {
		getPaymentTokenFromAPI(true).then(() => {
			expect(getPaymentTokenFromAPI.calledWith(true)).to.be.true;
		});
		done();
	});
});

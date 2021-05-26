const { expect } = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
	let consoleSpy;
	let functionSpy;

	beforeEach(() => {
		consoleSpy = sinon.spy(console, 'log');
		functionSpy = sinon.spy(Utils, 'calculateNumber');
	});

	afterEach(() => {
		consoleSpy.restore();
		functionSpy.restore();
	});

	it('Validate Utils func and result message', () => {
		sendPaymentRequestToApi(100, 20);
		expect(functionSpy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
		expect(consoleSpy.calledWith('The total is: 120')).to.be.true;
	});
});

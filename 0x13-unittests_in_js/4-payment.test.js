const { expect } = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', () => {
	let consoleSpy;
	let functionStub;

	beforeEach(() => {
		consoleSpy = sinon.spy(console, 'log');
		functionStub = sinon.stub(Utils, 'calculateNumber');
		functionStub.returns(10);
	});

	afterEach(() => {
		functionStub.restore();
		consoleSpy.restore();
	});

	it('Validate Utils func and result message', () => {
		sendPaymentRequestToApi(100, 20);
		expect(functionStub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
		expect(consoleSpy.calledWith('The total is: 10')).to.be.true;
	});
});

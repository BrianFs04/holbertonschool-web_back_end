const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber type === SUM', () => {
	it('Addition', () => {
		expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
	});
});

describe('calculateNumber type === SUBTRACT', () => {
	it('Subtraction', () => {
		expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
	});
});

describe('calculateNumber type === DIVIDE', () => {
	it('Divide', () => {
		expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
		expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
		expect(calculateNumber('DIVIDE', 0, 2)).to.equal(0);
	});
});

const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber type === SUM', () => {
	it('Addition', () => {
		assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
	});
});

describe('calculateNumber type === SUBTRACT', () => {
	it('Subtraction', () => {
		assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
	});
});

describe('calculateNumber type === DIVIDE', () => {
	it('Divide', () => {
		assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
		assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
		assert.strictEqual(calculateNumber('DIVIDE', 0, 2), 0);
	});
});

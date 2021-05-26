const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
	it('...', () => {
		assert.strictEqual(calculateNumber(1, 3), 4);
		assert.strictEqual(calculateNumber(1, 3.7), 5);
		assert.strictEqual(calculateNumber(1.2, 3.7), 5);
		assert.strictEqual(calculateNumber(1.5, 3.7), 6);
		assert.strictEqual(calculateNumber(-1.5, 3.5), 3);
		assert.strictEqual(calculateNumber(1.5, -3.4), -1);
		assert.strictEqual(calculateNumber(-1.2, -3.7), -5);
	});
});

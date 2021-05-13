import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  set amount(newAmount) {
    if (typeof newAmount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    this._amount = newAmount;
  }

  get amount() {
    return this._amount;
  }

  set currency(newCurrency) {
    if (!(newCurrency instanceof Currency)) {
      throw new TypeError('Currency must be a Currency');
    }
    this._amount = newCurrency;
  }

  get currency() {
    return this._currency;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency._name} (${this._currency._code})`;
  }

  static convertPrice(amount, convertionRate) {
    return amount * convertionRate;
  }
}

const createInt8TypedArray = (length, position, value) => {
  if (position > length) throw new RangeError('Position outside range');
  const buffer = new ArrayBuffer(length);
  const dataview = new DataView(buffer);
  dataview.setUint8(position, value);
  return dataview;
};

export default createInt8TypedArray;

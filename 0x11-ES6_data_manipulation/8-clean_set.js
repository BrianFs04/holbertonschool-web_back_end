const cleanSet = (set, startString) => {
  let res = '';
  if (startString || startString.length) {
    set.forEach((i) => {
      if (i.startsWith(startString)) res += `${i.slice(startString.length)}-`;
    });
    return res.slice(0, res.length - 1);
  }
  return res;
};

export default cleanSet;

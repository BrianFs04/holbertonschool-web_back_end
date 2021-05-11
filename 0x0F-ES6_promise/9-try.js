export default function guardrail(mathFunction) {
  const queue = [];
  let res;
  try {
    res = mathFunction();
  } catch (e) {
    res = e.toString();
  }
  queue.push(res);
  queue.push('Guardrail was processed');

  return queue;
}

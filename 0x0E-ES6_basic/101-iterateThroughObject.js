/* eslint-disable */
export default function iterateThroughObject(reportWithIterator) {
    const res = [];
    for (const i of reportWithIterator) {
        res.push(i);
    }
    return res.join(" | ");
}

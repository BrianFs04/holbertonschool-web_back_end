/* eslint-disable */
export default function createIteratorObject(report) {
    const res = [];
    for (const [keys, values] of Object.entries(report.allEmployees)) {
        for (const value of values) {
            res.push(value);
        }
    }
    return res;
}

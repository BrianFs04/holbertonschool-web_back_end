import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

before(() => {
	queue.testMode.enter();
});

afterEach(() => {
	queue.testMode.clear();
});

after(() => {
	queue.testMode.exit();
});

it('display a error message if jobs is not an array', () => {
	expect(() => createPushNotificationsJobs(undefined, queue)).to.throw(
		Error,
		'Jobs is not an array'
	);
});

it('create two new jobs to the queue', () => {
	const list = [
		{
			phoneNumber: '4153518780',
			message: 'This is the code 1234 to verify your account',
		},
		{
			phoneNumber: '4153518780',
			message: 'This is the code 1234 to verify your account',
		},
	];
	createPushNotificationsJobs(list, queue);
	expect(queue.testMode.jobs.length).to.equal(2);
});

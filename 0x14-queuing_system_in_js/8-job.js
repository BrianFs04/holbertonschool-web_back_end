const createPushNotificationsJobs = (jobs, queue) => {
	if (!Array.isArray(jobs)) throw Error('Jobs is not an array');
	for (const eachJob of jobs) {
		const job = queue.create('push_notification_code_3', eachJob);
		job.save();
		job.on('enqueue', () => {
			console.log(`Notification job created: ${job.id}`);
		})
			.on('complete', () => {
				console.log(`Notification job ${job.id} completed`);
			})
			.on('failed', (errorMessage) => {
				console.log(
					`Notification job ${job.id} failed: ${errorMessage}`
				);
			})
			.on('progress', (progress) => {
				console.log(`Notification job ${job.id} ${progress}% complete`);
			});
	}
};

export default createPushNotificationsJobs;

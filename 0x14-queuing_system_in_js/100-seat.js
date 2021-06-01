import kue from 'kue';
import redis from 'redis';
import express from 'express';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

const reserveSeat = (number) => {
	client.set('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
	const reservedSeats = await getAsync('available_seats');
	return reservedSeats;
};

let reservationEnabled = true;

const queue = kue.createQueue();

const app = express();

app.get('/available_seats', async (req, res) => {
	const numberOfAvailableSeats = await getCurrentAvailableSeats();
	res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', async (req, res) => {
	if (!reservationEnabled)
		return res.json({ status: 'Reservations are blocked' });
	const numberOfAvailableSeats = await getCurrentAvailableSeats();
	const job = queue
		.create('reserve_seat', { numberOfAvailableSeats })
		.save((err) => {
			if (err) res.json({ status: 'Reservation failed' });
			res.json({ status: 'Reservation in process' });
		})
		.on('complete', () => {
			console.log(`Seat reservation job ${job.id} completed`);
		})
		.on('failed', (errorMessage) => {
			console.log(
				`Seat reservation job ${job.id} failed: ${errorMessage}`
			);
		});
});

app.get('/process', async (req, res) => {
	queue.process('reserve_seat', async (job, done) => {
		console.log(job.data.numberOfAvailableSeats);
		if (job.data.numberOfAvailableSeats <= 0)
			done(Error('Not enough seats available'));
		const decreaseSeatsNumber = +job.data.numberOfAvailableSeats - 1;
		await reserveSeat(decreaseSeatsNumber);
		if (decreaseSeatsNumber === 0) reservationEnabled = false;
		done();
	});
	res.json({ status: 'Queue processing' });
});

app.listen(1245, () => {
	console.log('ready');
	reserveSeat(50);
	reservationEnabled = true;
});

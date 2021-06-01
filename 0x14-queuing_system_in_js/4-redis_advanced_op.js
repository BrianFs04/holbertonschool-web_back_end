import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
	console.log('Redis client connected to the server');
});

client.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`);
});

const dict = {
	Portland: 50,
	Seattle: 80,
	'New York': 20,
	Bogota: 20,
	Cali: 40,
	Paris: 2,
};

for (const [key, val] of Object.entries(dict)) {
	client.hset('HolbertonSchools', key, val, redis.print);
}

client.hgetall('HolbertonSchools', (error, obj) => console.log(obj));

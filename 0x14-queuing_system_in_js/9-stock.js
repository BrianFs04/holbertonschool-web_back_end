import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
	{
		itemId: 1,
		itemName: 'Suitcase 250',
		price: 50,
		initialAvailableQuantity: 4,
	},
	{
		itemId: 2,
		itemName: 'Suitcase 450',
		price: 100,
		initialAvailableQuantity: 10,
	},
	{
		itemId: 3,
		itemName: 'Suitcase 650',
		price: 350,
		initialAvailableQuantity: 2,
	},
	{
		itemId: 4,
		itemName: 'Suitcase 1050',
		price: 550,
		initialAvailableQuantity: 5,
	},
];

const getItemById = (id) =>
	listProducts.filter((items) => items.itemId === id)[0];

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

const reserveStockByd = (itemId, stock) => {
	client.set(itemId, stock);
};

const getCurrentReservedStockById = async (itemId) => {
	const reservedStock = await getAsync(itemId);
	return reservedStock;
};

const app = express();

app.get('/list_products', (req, res) => {
	res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
	const id = +req.params.itemId;

	const item = getItemById(id);
	const stock = await getCurrentReservedStockById(id);

	if (item) {
		item.reservedStock = +stock || 0;
		res.json(item);
		return;
	}
	res.status(404).json({ status: 'Product not found' });
});

app.get('/reserve_product/:itemId', async (req, res) => {
	const id = +req.params.itemId;

	const item = getItemById(id);

	if (!item) {
		res.status(404).json({ staus: 'Product not found' });
		return;
	}
	const stock = await getCurrentReservedStockById(id);
	if (item.initialAvailableQuantity - stock < 1) {
		res.status(403).json({ status: 'Not enough stock available', id });
		return;
	}

	reserveStockByd(id, +stock + 1);
	res.json({ status: 'Reservation confirmed', id });
});

app.listen(1245);

const util = require('util');
const express = require('express');
const redis = require('redis');

const listProducts = [
  {
    Id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    Id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    Id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    Id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  }
];
function getItemById(id) {
  const product = listProducts.filter((product) => product.Id === id);
  return product.length > 0 ? product[0] : product;
}
const app = express();
app.listen(1245);
app.get('/list_products', (req, res) => {
  res.send(listProducts);
});
const client = redis.createClient();
function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}
client.get = util.promisify(client.get);
async function getCurrentReservedStockById(itemId) {
  return client.get(`item.${itemId}`)
    .then((value) => {
      return value;
    })
    .catch((err) => {
      console.log(err);
    })
}
app.get('/list_products/:itemId', async (req, res) => {
  const id = req.params.itemId;
  const item = getItemById(parseInt(id));
  if (item.length === 0) {
    res.send({"status":"Product not found"});
  } else {
    item.currentQuantity = await getCurrentReservedStockById(id); 
    res.send(item);
  }
});
app.get('/reserve_product/:itemId', (req, res) => {
  const item = getItemById(parseInt(req.params.itemId));
  if (item instanceof Array) {
    res.send({"status":"Product not found"});
  } else {
    const stock = item.stock;
    if (stock === 0) {
      res.send({"status":"Not enough stock available","itemId": parseInt(req.params.itemId)});
    } else {
      reserveStockById(req.params.itemId, 1);
      res.send({"status":"Reservation confirmed","itemId": parseInt(req.params.itemId)});
    }
  }
});

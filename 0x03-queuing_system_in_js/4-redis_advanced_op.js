const redis = require('redis');
const client = require('./0-redis_client');

client.hset('HolbertonSchools', 'Portland', 50, () => redis.print('Reply: 1'));
client.hset('HolbertonSchools', 'Seattle', 80, () => redis.print('Reply: 1'));
client.hset('HolbertonSchools', 'New York', 20, () => redis.print('Reply: 1'));
client.hset('HolbertonSchools', 'Bogota', 20, () => redis.print('Reply: 1'));
client.hset('HolbertonSchools', 'Paris', 2, () => redis.print('Reply: 1'));
client.hgetall('HolbertonSchools', (err, value) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.stringify(value, null, 2));
  }
});

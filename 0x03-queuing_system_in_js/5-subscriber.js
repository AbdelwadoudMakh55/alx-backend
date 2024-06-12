const redis = require('redis');

function connectToRedis() {
  const client = redis.createClient();
  client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
  client.on('connect', () => console.log('Redis client connected to the server'));
  return client;
}
const client = connectToRedis();
client.subscribe('holberton school channel', (message) => {
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  } else if (message !== null) {
    console.log(message);
  }
});

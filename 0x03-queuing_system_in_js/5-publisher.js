const redis = require('redis');

function connectToRedis() {
  const client = redis.createClient();
  client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
  client.on('connect', () => console.log('Redis client connected to the server'));
  return client;
}
const client = connectToRedis();
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
  }, time);
  client.publish('holberton school channel', message);
}
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
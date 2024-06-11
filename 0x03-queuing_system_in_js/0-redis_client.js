const { createClient } = require('redis');
function connectToRedis() {
  const client = createClient();
  client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
  client.on('connect', () => console.log('Redis client connected to the server'));
  return client;
}
const client = connectToRedis();
module.exports = client;

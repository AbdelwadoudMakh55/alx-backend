const redis = require('redis');

function connectToRedis() {
  const client = redis.createClient();
  client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
  client.on('connect', () => console.log('Redis client connected to the server'));
  return client;
}
const client = connectToRedis();
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, value) => {
    if (err) {
      throw err;
    } else {
      redis.print('Value set correctly');
    }
  });

}
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, value) => {
    console.log(value);
  });
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

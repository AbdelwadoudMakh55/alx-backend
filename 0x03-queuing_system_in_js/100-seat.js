const redis = require('redis');
const express = require('express');
const kue = require('kue');
const util = require('util');

const client = redis.createClient();
function reserveSeat(number) {
  client.set('available_seats', number);
}
client.get = util.promisify(client.get);
async function getCurrentAvailableSeats() {
  return client.get('available_seats')
    .then((value) => {
      return value;
    })
    .catch((err) => {
      return err;
    })
};
reserveSeat(50);
let reservationEnabled = true;
const queue = kue.createQueue();
const app = express();
app.listen(1245);
app.get('/available_seats', async (req, res) => {
  res.send({"numberOfAvailableSeats": await getCurrentAvailableSeats()});
});
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.send({"status": "Reservation are blocked"});
  } else {
    const job = queue.create('reserve_seat', {reserve: 1});
    job.save((err) => {
      if (!err) {
        res.send({"status": "Reservation in process"});
      } else {
        res.send({"status": "Reservation failed"});
      }
    });
    job.on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    });
    job.on('failed', (err) => {
      console.log(`Seat reservation job ${job.id} failed: ${err}`);
    });
  }
});
app.get('/process', async (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    const seats = await getCurrentAvailableSeats();
    reserveSeat(seats - 1);
    const newSeats = await getCurrentAvailableSeats();
    if (newSeats === 0) {
      reservationEnabled = false;
    }
    if (newSeats >= 0) {
      job.complete();
      done();
    } else {
      job.failed();
      done(new Error('Not enough seats available'));
    }
  });
  res.send({"status": "Queue processing"});
});

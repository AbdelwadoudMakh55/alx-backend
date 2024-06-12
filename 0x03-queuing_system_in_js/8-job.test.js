const createPushNotificationsJobs = require('./8-job');
const kue = require('kue');
const expect = require('chai').expect;

const queue = kue.createQueue();
before(() => {
  queue.testMode.enter();
});
after(() => {
    queue.testMode.clear();
    queue.testMode.exit()
});
describe('createPushNotificationsJobs', () => {
  it('display a error message if jobs is not an array', () => {
    const list = 123;
    try {
      createPushNotificationsJobs(list, queue);
    } catch (err) {
      expect(err.toString()).to.equal('Error: Jobs is not an array');
    }
  });
  it('create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '7889622',
        message: 'Hello'
      },
      {
        phoneNumber: '7922332',
        message: 'Hola'
      }
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
  });
});

const kue = require('kue');

const blacklisted_nums = ['4153518780', '4153518781'];
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklisted_nums.includes(phoneNumber)) {
    job.failed();
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    done();
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}
const queue = kue.createQueue();
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
})

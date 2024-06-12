const kue = require('kue');

const queue = kue.createQueue();
const data = {
  phoneNumber: '0656789222',
  message: 'Welcome'
}
const push_notification_code = queue.create('push_notification_code', data)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${push_notification_code.id}`);
    }
  })
push_notification_code.on('complete', () => {
  console.log('Notification job completed');
});
push_notification_code.on('failed', () => {
  console.log('Notification job failed');
});

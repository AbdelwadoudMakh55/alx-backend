function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  jobs.forEach((job) => {
    const job_ = queue.create('push_notification_code_3')
      .save((err) => {
        if (!err) {
            console.log(`Notification job created: ${job_.id}`);
        }
      })
    job_.on('complete', () => {
      console.log(`Notification job ${job_.id} completed`);
    })
    job_.on('failed', (err) => {
      console.log(`Notification job ${job_.id} failed: ${err}`);
    })
    job_.on('progress', (progress) => {
      console.log(`Notification job ${job_.id} ${progress}% complete`);
    })
  })
}
module.exports = createPushNotificationsJobs;

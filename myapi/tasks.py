"""
from celery import shared_task
@shared_task
def check_for_orders():      
    orders = User_store.objects.all()
    now = datetime.datetime.utcnow().replace(tzinfo=utc,second=00, microsecond=00)
    week_old = now - datetime.timedelta(week=1)
    for order in orders:
        if order.manu_date.date() == week_old.date():
            send_mail('Manufacturing Reminder',
                '{} is due {}'.format(order.id, order.manu_date),
                'edwin.jnm123@gmail.com',
                ['gummy@gmail.com.com'])
            return None
"""

from __future__ import absolute_import

from celery.decorators import task
from django.contrib.auth import get_user_model

@task()
def user_send_activation_email(user_id):
    user = get_user_model().objects.get(pk=user_id)
    user.send_activation_email()


from celery.schedules import crontab

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'tasks.add',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16),
    },
}
app.conf.timezone = 'UTC'

@task(name="send_notification", bind=True, default_retry_delay=300, max_retries=5)
def send_notification(self, subject, message):
    from django.core.mail import send_mail as sm

    # Fetch all users except superuser
    users = User.objects.exclude(is_superuser=True).all()
    user_emails = [user.email for user in users]

    # try sending email
    try:
        res = sm(
            subject=subject,
            html_message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=user_emails,
            fail_silently=False,
            message=None)
        print(f'Email send to {len(user_emails)} users')
    except Exception:

        # retry when fail
        send_notification.retry()
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .tasks import send_notifications


from .models import PostCategory


@receiver(m2m_changed, sender=PostCategory)
def post_created(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        instance.title = 'Уведомление'
        subscribers_emails = []

        for cat in categories:
            subscribers = cat.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]

        for s in subscribers_emails:
            send_notifications.delay(instance.preview(), instance.pk, instance.title, (s,))

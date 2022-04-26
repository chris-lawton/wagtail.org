import requests
from django.conf import settings
from wagtail.core.signals import page_published, page_unpublished

from .models import AreWeHeadlessYetHomePage, AreWeHeadlessYetTopicPage


def register_signal_handlers():
    if not getattr(settings, "VERCEL_DEPLOY_HOOK_URL", None):
        return

    from .thread_pool import run_in_thread_pool

    @run_in_thread_pool
    def deploy(sender, **kwargs):
        """Triggers a build on Vercel."""

        response = requests.post(
            settings.VERCEL_DEPLOY_HOOK_URL,
            timeout=settings.VERCEL_DEPLOY_REQUEST_TIMEOUT,
        )
        response.raise_for_status()

    page_published.connect(deploy, sender=AreWeHeadlessYetHomePage)
    page_published.connect(deploy, sender=AreWeHeadlessYetTopicPage)

    page_unpublished.connect(deploy, sender=AreWeHeadlessYetHomePage)
    page_unpublished.connect(deploy, sender=AreWeHeadlessYetTopicPage)

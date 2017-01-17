# coding: utf-8
"""
Plugin for Sentry which allows sending notification via Telegram messenger.

DISCLAIMER: Tested only with Sentry 8.9.0
"""
from __future__ import absolute_import
from sentry.plugins import register
from .plugin import TelegramNotificationsPlugin


__version__ = '0.0.2'

register(TelegramNotificationsPlugin)
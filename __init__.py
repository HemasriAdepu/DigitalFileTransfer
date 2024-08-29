# file_transfer/__init__.py
default_app_config = 'members.apps.MembersConfig'

def setup_signals():
    from . import signals

default_app_config = 'file_transfer.apps.FileTransferConfig'

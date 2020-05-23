===================================
  EMQ X extension Python SDK
===================================

+----------------+------------------------------------------------------+
|Project site    | https://github.com/emqx-extension-python-sdk         |
+----------------+------------------------------------------------------+
|Issues          | https://github.com/emqx/extension-python-sdk/issues/ |
+----------------+------------------------------------------------------+
|Documentation   | todo.....                                            |
+----------------+------------------------------------------------------+
|Author          | emqx(taodk@emqx.io)                                    |
+----------------+------------------------------------------------------+
|Latest Version  | 0.1                                                  |
+----------------+------------------------------------------------------+
|Python versions | 3.6 or above                                         |
+----------------+------------------------------------------------------+
|Keywords        | emqx                                                 |
+----------------+------------------------------------------------------+

Using Python to handle the hooks in `EMQ X <https://emqx.io/>`__ to
realize client authentication, ACL check and message.

Install
=======

::

   pip3 install emqx-extension-hook

Download
========

`Download EMQ X v4.1 + <https://emqx.io/downloads>`__

Configuration
=============

Use emqx-extension-hook plugins:

::

   ## etc/plugins/emqx_extension_hook.conf

   ## Search path for scripts/library
   exhook.drivers.python3.path = /emqx-ext/examples/

   ## Initial module name
   ##
   exhook.drivers.python3.init_module = client

example:

.. code:: python

   ## /emqx-ext/examples/client.py

   from emqx-extension-hook.hooks import EmqxHookSdk, hooks_handler
   from emqx-extension-hook.types import EMQX_CLIENTINFO_PARSE_T, EMQX_MESSAGE_PARSE_T


   class CustomHook(EmqxHookSdk):

       @hooks_handler(topics='testtopic/#', qos=1)
       def on_client_connect(self,
                             conninfo: EMQX_CLIENTINFO_PARSE_T = None,
                             props: dict = None,
                             state: list = None):
           print(f'[Python SDK] [on_client_connect] {conninfo.clientid} connecte')

       @hooks_handler()
       def on_client_connected(self,
                               clientinfo: EMQX_CLIENTINFO_PARSE_T,
                               state: list = None):
           print(
               f'[Python SDK] [on_client_connected] {clientinfo.clientid} connected')

       @hooks_handler()
       def on_client_check_acl(self, clientinfo: EMQX_CLIENTINFO_PARSE_T,
                               pubsub: str,
                               topic: str,
                               result: bool,
                               state: tuple) -> bool:
           print(
               f'[Python SDK] [on_client_check_acl] {clientinfo.username} check ACL: {pubsub} {topic}')
           if clientinfo.username == '':
               return False
           return True

       @hooks_handler()
       def on_client_authenticate(self, clientinfo: EMQX_CLIENTINFO_PARSE_T, authresult, state) -> bool:
           print(
               f'[Python SDK] [on_client_authenticate] {clientinfo.clientid} authenticate')
           if clientinfo.clientid != '':
               return True
           return False


   emqx_hook = CustomHook(hook_module='client.emqx_hook')


   def init():
       return emqx_hook.on_start()


   def deinit():
       return

Load plugin
============

::

   ./bin/emqx_ctl plugins load emqx_extension_hook




Develop
=======

Installation
~~~~~~~~~~~~

You can install emqx-extension-python-sdk either via the Python Package Index (PyPI) or from source.

To install using `setup`:

.. sourcecode:: console

    $ python setup.py develop

To install using `pip`:

.. sourcecode:: console

    $ pip install -U emqx_sdk


Run example
~~~~~~~~~~~~
.. sourcecode:: console

    $


FAQ
============

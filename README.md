# EMQ X extension Python SDK

Using Python to handle the hooks in [EMQ X](https://emqx.io/) to
record connection and disconnection information, realize client authentication, ACL check and message storage.

## Install

EMQ X extension requires Python 3.6 or later :

```bash
pip3 install emqx-extension-sdk
```

The emqx-extension-sdk is open source, welcome to [commit](https://github.com/emqx/emqx-extension-python-sdk) to help us improve the function.


## Download

You can use the open source version for most functions, but **only EMQ X Enterprise edition** supports message storage.

[Download EMQ X MQTT Broker v4.1 +](https://emqx.io/downloads)

EMQ X Enterprise v4.1 is coming.


## Configuration

Use emqx-extension-hook plugins:

```bash
## Setup the supported drivers
##
## Value: python2 | python3 | java
exhook.drivers = python3

## Search path for scripts/library
exhook.drivers.python3.path = data/extension/hooks.py

## Call timeout
##
## Value: Duration
##exhook.drivers.python3.call_timeout = 5s

## Initial module name
## Your filename or module name
exhook.drivers.python3.init_module = hooks
```

example:

```python
## data/extension/hooks.py

from emqx_extension.hooks import EmqxHookSdk, hooks_handler
from emqx_extension.types import EMQX_CLIENTINFO_PARSE_T, EMQX_MESSAGE_PARSE_T


class CustomHook(EmqxHookSdk):

    @hooks_handler()
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
    def on_client_authenticate(self, clientinfo: EMQX_CLIENTINFO_PARSE_T, authresult,
                               state) -> bool:
        print(
            f'[Python SDK] [on_client_authenticate] {clientinfo.clientid} authenticate')
        if clientinfo.clientid != '':
            return True
        return False
    
    # on_message_* only EMQ X Enterprise
    @hooks_handler()
    def on_message_publish(self, message: EMQX_MESSAGE_PARSE_T, state):
        print(
            f'[Python SDK] [on_message_publish] {message.topic} {message.payload}')


emqx_hook = CustomHook(hook_module=f'{__name__}.emqx_hook')


def init():
    return emqx_hook.start()


def deinit():
    return
```

## Benchmark

Coming soon.

## Load plugin

```bash
./bin/emqx_ctl plugins load emqx_extension_hook
```

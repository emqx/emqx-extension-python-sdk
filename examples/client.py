from emqx_sdk.hooks import EmqxHookSdk
from emqx_sdk.types import EMQX_CLIENTINFO_T


class CustomHook(EmqxHookSdk):

    def on_client_connect(self,
                          conninfo: EMQX_CLIENTINFO_T = None,
                          props: dict = None,
                          state: list = None):
        for con in conninfo:
            print(con[0].decode(), str(con[1]))


emqx_hook = CustomHook(hook_module='client.emqx_hook')


def init():
    return emqx_hook.on_start()


def deinit():
    return

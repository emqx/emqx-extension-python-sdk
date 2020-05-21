from .hooks import EmqxHookSdk
from .types import EMQX_CLIENTINFO_T


class CustomHook(EmqxHookSdk):

    def on_client_connect(self,
                          conninfo: EMQX_CLIENTINFO_T,
                          props: dict,
                          state: list):
        print(conninfo)


def init():
    d = CustomHook()
    return d.on_start()


def deinit():
    return

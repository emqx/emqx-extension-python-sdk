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

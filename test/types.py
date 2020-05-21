from typing import List, NamedTuple, Dict


EMQX_TOPICS = List[str]


class EMQX_CLIENTINFO_T(NamedTuple):
    node: str
    clientid: str
    username: str
    password: str
    peerhost: str
    sockport: int
    protocol: str
    mountpoint: str
    is_superuser: bool
    anonymous: bool


class EMQX_MESSAGE(NamedTuple):
    node: str
    id: str
    qos: int
    from_: str  # todo
    topic: str
    payload: str
    timestamp: int


EMQX_PROPS_T = Dict[str, int]


class EMQX_OPTS(NamedTuple):
    is_new: bool
    nl: int
    qos: int
    rap: int
    rh: int

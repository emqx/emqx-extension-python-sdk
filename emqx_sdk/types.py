from typing import List, NamedTuple, Dict, Tuple, Any


EMQX_TOPICS = List[str]

EMQX_CLIENTINFO_T = List[Tuple[bytes, Any]]


class EMQX_CLIENTINFO_PARSE_T(NamedTuple):
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



EMQX_MESSAGE_T = List[Tuple[bytes, Any]]


class EMQX_MESSAGE_PARSE_T(NamedTuple):
    node: str
    id: str
    qos: int
    from_: str  # todo
    topic: str
    payload: str
    timestamp: int


EMQX_PROPS_T = Dict[str, int]

EMQX_OPTS_T = List[Tuple[bytes, Any]]


class EMQX_OPTS_PARSE_T(NamedTuple):
    is_new: bool
    nl: int
    qos: int
    rap: int
    rh: int

from typing import List, NamedTuple, Dict, Tuple, Any
from abc import ABC


EMQX_TOPICS = List[str]

EMQX_CLIENTINFO_T = List[Tuple[bytes, Any]]


class EMQXBase(ABC):
    def to_dict(self) -> dict:
        return self.__dict__


class EMQX_CLIENTINFO_PARSE_T(EMQXBase):
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

    def to_dict(self) -> dict:
        return {
            'node': self.node,
            'clientid': self.clientid,
            'username': self.username,
            'password': self.password,
            'peerhost': self.peerhost,
            'sockport': self.sockport,
            'protocol': self.protocol,
            'mountpoint': self.mountpoint,
            'is_superuser': self.is_superuser,
            'anonymous': self.anonymous
        }



EMQX_MESSAGE_T = List[Tuple[bytes, Any]]


class EMQX_MESSAGE_PARSE_T(EMQXBase):
    node: str
    id: str
    qos: int
    from_clientid: str  # todo
    topic: str
    payload: str
    timestamp: int

    def to_dict(self) -> dict:
        return {
            'node': self.node,
            'id': self.id,
            'qos': self.qos,
            'from_clientid': self.from_clientid,
            'topic': self.topic,
            'payload': self.payload,
            'timestamp': self.timestamp
        }


EMQX_PROPS_T = Dict[str, int]

EMQX_OPTS_T = List[Tuple[bytes, Any]]


class EMQX_OPTS_PARSE_T(EMQXBase):
    is_new: bool
    nl: int
    qos: int
    rap: int
    rh: int

    def to_dict(self) -> dict:
        return {
            'is_new': self.is_new,
            'nl': self.nl,
            'qos': self.qos,
            'rap': self.rap,
            'rh': self.rh
        }

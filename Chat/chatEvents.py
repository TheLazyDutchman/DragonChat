from dataclasses import dataclass

@dataclass
class event:
    group: str

@dataclass
class messageEvent(event):
    username: str
    msg: str
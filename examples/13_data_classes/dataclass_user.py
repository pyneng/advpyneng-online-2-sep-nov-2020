from datetime import datetime
from dataclasses import dataclass, field
from typing import List


def login(user):
    user.sessions.append(str(datetime.now()))


@dataclass
class Session:
    start: str
    end: str


@dataclass
class Permission:
    name: str
    level: int


@dataclass
class User:
    username: str
    permissions: Permission
    sessions: List[str] = field(default_factory=list)


if __name__ == "__main__":
    admin = Permission("admin", 100)
    user = Permission("user", 10)

    u1 = User("user1", admin)
    u2 = User("user2", user)
    u3 = User("user3", admin)

    login(u1)
    login(u2)
    login(u3)
    login(u1)
    login(u2)
    login(u2)
    login(u3)
    print(u1)
    print(u2)
    print(u3)

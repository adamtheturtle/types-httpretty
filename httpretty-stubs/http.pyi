from typing import Literal

STATUSES: dict[int, str]

class HttpBaseClass:
    GET: Literal["GET"]
    PUT: Literal["PUT"]
    POST: Literal["POST"]
    DELETE: Literal["DELETE"]
    HEAD: Literal["HEAD"]
    PATCH: Literal["PATCH"]
    OPTIONS: Literal["OPTIONS"]
    CONNECT: Literal["CONNECT"]
    METHODS: tuple[
        Literal[
            "GET",
            "PUT",
            "POST",
            "DELETE",
            "HEAD",
            "PATCH",
            "OPTIONS",
            "CONNECT",
        ],
        ...,
    ]
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: object, /) -> bool: ...
    def __hash__(self) -> int: ...

def parse_requestline(s: str | bytes) -> tuple[str, str, str]: ...
def last_requestline(sent_data: str | bytes) -> tuple[str, str, str]: ...

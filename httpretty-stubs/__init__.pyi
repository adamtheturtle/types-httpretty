from typing import Literal

from .core import (
    EmptyRequestHeaders as EmptyRequestHeaders,
)
from .core import (
    Entry as Entry,
)
from .core import (
    HTTPrettyRequest as HTTPrettyRequest,
)
from .core import (
    HTTPrettyRequestEmpty as HTTPrettyRequestEmpty,
)
from .core import (
    URIInfo as URIInfo,
)
from .core import (
    URIMatcher as URIMatcher,
)
from .core import (
    get_default_thread_timeout as get_default_thread_timeout,
)
from .core import (
    httprettified as httprettified,
)
from .core import (
    httprettized as httprettized,
)
from .core import (
    httpretty as httpretty,
)
from .core import (
    set_default_thread_timeout as set_default_thread_timeout,
)
from .errors import (
    HTTPrettyError as HTTPrettyError,
)
from .errors import (
    UnmockedError as UnmockedError,
)

__version__: str
HTTPretty = httpretty
activate = httprettified
enabled = httprettized
enable = httpretty.enable
register_uri = httpretty.register_uri
disable = httpretty.disable
is_enabled = httpretty.is_enabled
reset = httpretty.reset
Response = httpretty.Response
GET: Literal["GET"]
PUT: Literal["PUT"]
POST: Literal["POST"]
DELETE: Literal["DELETE"]
HEAD: Literal["HEAD"]
PATCH: Literal["PATCH"]
OPTIONS: Literal["OPTIONS"]
CONNECT: Literal["CONNECT"]

def last_request() -> HTTPrettyRequest | HTTPrettyRequestEmpty: ...
def latest_requests() -> list[HTTPrettyRequest]: ...
def has_request() -> bool: ...

from dataclasses import dataclass
from typing import TypedDict, Self

from .api import ApiItem, ApiRequestV2


class TypedTeleportToken(TypedDict):
    """Teleport token type definition."""

    creation_timestamp: int
    expiration_timestamp: int
    invitation_url: str
    token_id: str
    

@dataclass
class TeleportTokenListRequest(ApiRequestV2):
    """Request object for teleport token list."""

    @classmethod
    def create(cls) -> Self:
        """Create teleport token list request."""
        return cls(method="post", path="/teleport/invitation-history")


@dataclass
class TeleportTokenCreateRequest(ApiRequestV2):
    """Request object for teleport token create."""

    @classmethod
    def create(cls) -> Self:
        """Create teleport token create request."""
        return cls(method="post", path="/teleport/token")


@dataclass
class TeleportTokenDeleteRequest(ApiRequestV2):
    """Request object for teleport token delete."""

    @classmethod
    def create(cls, token_id: str) -> Self:
        """Create teleport token delete request."""
        return cls(method="delete", path=f"/teleport/token/{token_id}")


class TeleportToken(ApiItem):
    """Represents a teleport token."""

    raw: TypedTeleportToken

    @property
    def token_id(self) -> str:
        """ID of teleport token."""
        return self.raw["token_id"]

    @property
    def invitation_url(self) -> str:
        """Invitation URL of teleport token."""
        return self.raw["invitation_url"]
    
    @property
    def creation_timestamp(self) -> int:
        """Creation timestamp of teleport token."""
        return self.raw["creation_timestamp"]

    @property
    def expiration_timestamp(self) -> int:
        """Expiration timestamp of teleport token."""
        return self.raw["expiration_timestamp"]

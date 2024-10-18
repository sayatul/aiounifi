from ..models.api import TypedApiResponse
from ..models.teleport import (
    TeleportToken,
    TeleportTokenCreateRequest,
    TeleportTokenDeleteRequest,
    TeleportTokenListRequest
)
from .api_handlers import APIHandler


class Teleport(APIHandler[TeleportToken]):
    """Represents Teleport."""

    obj_id_key = "token_id"
    item_cls = TeleportToken
    api_request = TeleportTokenListRequest.create()

    async def create(self) -> TypedApiResponse:
        """Create teleport token on controller."""
        return await self.controller.request(
            TeleportTokenCreateRequest.create()
        )

    async def delete(self, token_id: str) -> TypedApiResponse:
        """Delete teleport token on controller."""
        return await self.controller.request(
            TeleportTokenDeleteRequest.create(token_id=token_id)
        )
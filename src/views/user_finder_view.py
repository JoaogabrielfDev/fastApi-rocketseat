from src.controllers.interfaces.user_finder import UserFinderInterface
from .http_types.http_request import HttpResquest
from .http_types.http_response import HttpResponse


class UserFinderView:
    def __init__(self, controller: UserFinderInterface) -> None:
        self.__controler = controller
        
    async def handle_find_user_by_name(self, http_request: HttpResponse) -> HttpResponse:
        user_data = http_request.path_params["user_name"]
        response = await self.__controler.find_user_by_name(user_data)
        return HttpResponse(body=response, status_code=200)
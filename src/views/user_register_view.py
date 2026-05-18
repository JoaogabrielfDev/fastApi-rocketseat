from src.controllers.interfaces.user_register import UserRegisterInterface
from .http_types.http_request import HttpResquest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler


class UserRegisterView:
    def __init__(self, controller: UserRegisterInterface) -> None:
        self.__controler = controller
        
    async def handle_register_user(self, http_request: HttpResquest) -> HttpResponse:
        try:
            user_data = http_request.body
            response = await self.__controler.register_user(user_data)
            return HttpResponse(body=response, status_code=201)
        
        except Exception as exception:
            error_handler(exception)
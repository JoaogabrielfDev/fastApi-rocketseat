from abc import ABC, abstractmethod

class UserRegisterInterface:
    
    @abstractmethod
    async def register_user(self, user_data: dict) -> dict: pass

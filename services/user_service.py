from models.user import User

class UserService:
    users = []

    @staticmethod
    def add_user(user: User):
        UserService.users.append(user)
        return user
    
    @staticmethod
    def get_user(user_id: int):
        for user in UserService.users:
            if user.id == user_id:
                return user
        return None
    
    @staticmethod
    def get_userall():
        users = UserService.users
        return users
        
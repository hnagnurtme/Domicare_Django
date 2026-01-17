from typing import Optional
from models.user import User

# find user by email
def find_by_email(email: str) -> Optional[User]:
    try:
        return User.objects.select_related().prefetch_related('roles').get(email=email)
    except User.DoesNotExist:
        return None

# exists by email
def exists_by_email(email: str) -> bool:
    return User.objects.filter(email=email).exists()

# find user by id
def find_by_id(user_id: int) -> Optional[User]:
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None

# save user
def save(user: User) -> User:
    user.save()
    return user

class UserRepository:
    def find_by_email(self, email: str) -> Optional[User]:
        return find_by_email(email)

    def exists_by_email(self, email: str) -> bool:
        return exists_by_email(email)

    def find_by_id(self, user_id: int) -> Optional[User]:
        return find_by_id(user_id)

    def save(self, user: User) -> User:
        return save(user)

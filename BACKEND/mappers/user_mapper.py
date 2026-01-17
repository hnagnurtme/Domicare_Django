from dtos.role_dto import RoleDTO
from dtos.user_dto import UserDTO
from models.user import User


class UserMapper:
    @staticmethod
    def to_dto(user: User) -> UserDTO:
        if user is None:
            return None

        roles_dto = None
        if user.roles.exists():
            roles_dto = {
                RoleDTO(
                    id=role.id,
                    name=role.name,
                    description=role.description,
                )
                for role in user.roles.all()
            }
        return UserDTO(
            id=user.id,
            name=user.full_name,
            password=user.password,
            phone=user.phone,
            address=user.address,
            avatar=user.avatar,
            email=user.email,
            gender=user.gender,
            dateOfBirth=user.date_of_birth,
            isEmailConfirmed=user.is_email_confirmed,
            emailConfirmationToken=user.email_confirmation_token,
            googleId=user.google_id,
            roles=roles_dto,
            updateAt=user.update_at,
            updateBy=user.update_by,
            createAt=user.create_at,
            createBy=user.create_by,
            isActive=user.is_active,
        )

    @staticmethod
    def to_entity(user_dto: UserDTO) -> User:
        return User(
            id=user_dto.id,
            full_name=user_dto.name,
            password=user_dto.password,
            phone=user_dto.phone,
            address=user_dto.address,
            avatar=user_dto.avatar,
            email=user_dto.email,
            gender=user_dto.gender,
            date_of_birth=user_dto.date_of_birth,
            is_email_confirmed=user_dto.is_email_confirmed,
            email_confirmation_token=user_dto.email_confirmation_token,
            google_id=user_dto.google_id,
            update_at=user_dto.update_at,
            update_by=user_dto.update_by,
            create_at=user_dto.create_at,
            create_by=user_dto.create_by,
            is_active=user_dto.is_active,
        )
# from accounts.DB.users_option import UserRole
from app.services.reg_service import AuthService
from accounts.DB.repositories.user_rep import UserRepository

user_repo = UserRepository()
auth_service = AuthService(user_repo)

# тестовый админ, не обращаем внимание, с django superuser он никак не связан
# auth_service.create_user("admin@test.com", "Admin", "Admin_12345", UserRole.ADMIN)
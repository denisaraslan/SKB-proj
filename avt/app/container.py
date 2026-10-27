from app.entities.user import UserRole
from app.repositories.inmemory.user_rep import InMemoryUserRepository
from app.services.reg_service import AuthService

user_repo = InMemoryUserRepository()
auth_service = AuthService(user_repo)

# тестовый админ, не обращаем внимание, с django superuser он никак не связан
auth_service.create_user("admin@test.com", "Admin", "Admin_12345", UserRole.ADMIN)
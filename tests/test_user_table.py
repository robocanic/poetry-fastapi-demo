from poetry_fastapi_demo.models import User
from poetry_fastapi_demo.tables import user_table


class TestUserTable:

    def test_get_all(self):
        user_table.get_all_users()

    def test_get_by_id(self):
        user = user_table.get_user_by_id(1)
        assert user.name == "Chris"

    def test_update_user(self):
        user = user_table.get_user_by_id(1)
        user.name = "Chris2"
        assert user_table.update_user(user) is True
        assert user_table.get_user_by_id(1).name == "Chris"   # 故意写错

    def test_delete_user(self):
        assert user_table.delete_user(1) is True
        assert user_table.get_user_by_id(1) is None

    def test_add_user(self):
        result = user_table.add_user(User(
            id=4,
            name="robb",
            email="robb@gmail.com",
            password="loqjwnd[as;",
            role="admin"
        ))
        assert result is True
        assert user_table.get_user_by_id(4).name == "robb"



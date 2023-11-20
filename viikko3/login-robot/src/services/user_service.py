from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user
    
    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # Validate username using a regular expression
        if not re.match("^[a-z]{3,}$", username):
            raise UserInputError("Invalid username format")

        # Add additional password validation logic if needed
        if len(password) < 8 or not any(char.isalpha() for char in password):
            raise UserInputError("Invalid password")

        # Add any other validation checks you need

        # If no validation errors, return True or perform additional actions
        return True
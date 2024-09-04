import os


class GeneralConfig:
    JWT_SECRET_KEY = "Example"
    JWT_REFRESH_SECRET_KEY = "Test"
    JWT_TIME_EXPIRE = 720
    JWT_ALGORITHM = "HS256"


gc = GeneralConfig()

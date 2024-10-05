import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pokemon.db'  # Usando SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False

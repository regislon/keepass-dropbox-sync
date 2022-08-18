"""
Dynaconf Settings
"""
from dynaconf import Dynaconf, Validator

settings = Dynaconf(
    envvar_prefix=False,
    settings_files=[
        "settings.toml",
        "secrets.toml",
    ],
    validators=[
        Validator("host", default=False),
        Validator("apiversion", default="False"),
        Validator("apikey", default=False),
    ],
)

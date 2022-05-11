from dataclasses import dataclass


@dataclass
class CacheConfig:
    host: str
    port: str
    password: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    misc: Miscellaneous
    cache_config: CacheConfig

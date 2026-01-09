from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("fasterapi")
except PackageNotFoundError:
    # Si le package n'est pas installé (ex: test en local)
    __version__ = "unknown"

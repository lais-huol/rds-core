"""
Documentar.
"""

import dynaconf

settings = dynaconf.Dynaconf(
    envvar_prefix="DYNACONF",
)

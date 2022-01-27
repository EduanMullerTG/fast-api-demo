import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "src"))

from fast_api_demo import (  # noqa: E402, F401
    create_app,
)

app = create_app()

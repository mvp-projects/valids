# valids

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Build Status](https://github.com/mvp-projects/valids/workflows/test/badge.svg?branch=main&event=push)](https://github.com/mvp-projects/valids/actions?query=workflow%3Atest)
[![Coverage badge](https://raw.githubusercontent.com/mvp-projects/valids/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/mvp-projects/valids/blob/python-coverage-comment-action-data/htmlcov/index.html)

-----

**Table of Contents**

```python
from valids import valid
from valids.exceptions import ValueValidationError
from valids.typing import Int16

try:
    valid(
        dtype=Int16,
        v=12_123,
    ).equal(
        other=12_123,
    ).multiple_of(
        of=3,
    ).less_than(
        other=100_000,
    ).greater_than(
        other=10_000,
    )
except ValueValidationError as e:
    print(f"Value didn't pass validation. {e}")
```
# Flipt Python SDK

[![pypi](https://img.shields.io/pypi/v/flipt.svg)](https://pypi.org/project/flipt)
![beta](https://img.shields.io/badge/status-beta-yellow)

## Documentation

API documentation is available at <https://www.flipt.io/docs/reference/overview>.

## Status

This SDK is in `beta`, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning your installation of this package wherever necessary.

## Install

```
pip install flipt=={version}
```

## Usage

```python
from flipt import flagCreateRequest
from flipt.client import FliptApi

fliptApi = FliptApi()

fcr = flagCreateRequest(key="new-flag", name="NewFlag", enabled=True)
flag = fliptApi.flags.create("default", request=fcr)

# Print out the flag details.
print(flag)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest [opening an issue](https://github.com/flipt-io/flipt-python/issues) first to discuss with us!

On the other hand, contributions to the README are always very welcome!

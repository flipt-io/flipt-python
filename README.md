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

# customize to point to your instance of Flipt
FLIPT_API="http://localhost:8080"
fliptApi = FliptApi(base_url=FLIPT_API)

fcr = flagCreateRequest(key="new-flag", name="NewFlag", enabled=True)
flag = fliptApi.flags.create("default", request=fcr)

# Print out the flag details.
print(flag)
```

### Evaluation

In [v1.24.0](https://github.com/flipt-io/flipt/releases/tag/v1.24.0) of Flipt server, we added a new set of Evaluation API endpoints to allow evaluating of both boolean and multivariate flags. This SDK supports both sets of evaluation APIs (old and new) as of [v0.2.7](https://github.com/flipt-io/flipt-python/releases/tag/0.2.7).

The previous API endpoints at `/api/v1/evaluate` have been deprecated and may be removed in a future release. We recommend using the new Evaluation API at `/evaluate/v1/` for all new projects.

For more information on the new Evaluation API, please see the [API documentation](https://www.flipt.io/docs/reference/overview#v1-24-0) or blog post on [Flipt v1.24.0](https://www.flipt.io/blog/boolean-flags-and-rollouts).

```python
fliptApi = FliptApi()

er = evaluationRequest(namespace_key="defaut", flag_key="new-flag", entity_id="user-123", context={"platform": "ios"})
resp = fliptApi.evaluation.variant(er)

# Print out the evaluation response.
print(resp)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest [opening an issue](https://github.com/flipt-io/flipt-python/issues) first to discuss with us!

On the other hand, contributions to the README are always very welcome!

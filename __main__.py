"""A Python Pulumi program"""

import pulumi
import pulumi_kong as kong

consumer = kong.Consumer("my-consumer", username="my-username-1", custom_id="123")
service = kong.Service(
    "mockbin",
    name="mockbin",
    host="mockbin.org",
    protocol="http",
)
route = kong.Route(
    "mockbin-route",
    name="mocking",
    service_id=service.id,
    paths=["/mockbin"],
    protocols=[
        "http",
        "https",
    ],
    methods=[
        "GET",
        "POST",
    ],
)

jwt_plugin = kong.Plugin(
    "jwtPlugin",
    name="key-auth",
    service_id=service.id,
)

consumer_key_auth = kong.ConsumerKeyAuth(
    "consumerKeyAuth",
    consumer_id=consumer.id,
    key="secret",
    tags=[
        "myTag",
        "anotherTag",
    ],
)

rate_limit = kong.Plugin(
    "rateLimit",
    name="rate-limiting",
    service_id=service.id,
    enabled=True,
    config_json="""	{
    		"second": 1,
    		"hour" : 1000,
            "policy": "local"
    	}
    """,
)

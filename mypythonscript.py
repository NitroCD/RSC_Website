import rscapi
from rscapi.models.member import Member
from rscapi.rest import ApiException
from pprint import pprint

import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
loop = asyncio.new_event_loop()

# Defining the host is optional and defaults to https://staging-api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://staging-api.rscna.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Api-Key
# configuration.api_key['Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
configuration.api_key_prefix['Api-Key'] = 'Bearer'

async def init():
    # Enter a context with an instance of the API client
    async with rscapi.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = rscapi.MembersApi(api_client)
        id = 56 # int | A unique integer value identifying this user.

        try:
            api_response = await api_instance.members_read(id)
            print("The response of MembersApi->members_read:\n")
            return api_response
        except Exception as e:
            print("Exception when calling MembersApi->members_read: %s\n" % e)

testStr = asyncio.run(init())

def test_method():
    return testStr
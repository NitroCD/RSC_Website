import rscapi
from rscapi.models.member import Member
from rscapi.models.members_list200_response import MembersList200Response
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

# Configure API key authorization: Api-Key
# configuration.api_key['Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
configuration.api_key_prefix['Api-Key'] = 'Bearer'

async def getMembersList():
    # Enter a context with an instance of the API client
    async with rscapi.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = rscapi.MembersApi(api_client)
        # rsc_name = 'Nitro' # str | rsc_name (optional)
        # discord_username = 'cdno' # str | discord_username (optional)
        discord_id = 305826641337384970 # int | Discord ID of member to search for (optional)
        # limit = 56 # int | Number of results to return per page. (optional)
        # offset = 56 # int | The initial index from which to return the results. (optional)

        try:
            api_response = await api_instance.members_list(discord_id=discord_id)
            return api_response.results[0]
        except Exception as e:
            print("Exception when calling MembersApi->members_read: %s\n" % e)

testStr = asyncio.run(getMembersList())

def test_method():
    return testStr
# SimPlurAPI
### A SimplyPlural API wrapper library for [Python](https://www.python.org/).

## Installation
Python 3.12 or newer is required.

## Usage and examples

### Environment variables
These can be set in the `.env` file.

There are separate keys for production and development modes to allow for easy mode switches.
Both sets can be present at the same time without issues.

#### Production mode
These keys will be used when running in production mode.
These should target the public production servers.

| Setting | Default | Description |
| --------| ------- | ----------- |
| `api_url_http` | `https://api.apparyllis.com/v#/` | • The base URL for SimplyPlural API HTTP requests in production mode. <br/>• `#` is a wildcard for the API version and will be replaced at runtime. <br/>• **Unless you are running your own fork of Simply Plural, you shouldn't change this.** |
| `api_url_socket` | `wss://api.apparyllis.com/v#/socket` | • The base URL for SimplyPlural API socket requests in production mode. <br/>• `#` is a wildcard for the API version and will be replaced at runtime. <br/>• **Unless you are running your own fork of Simply Plural, you shouldn't change this.** |
| `api_version` | `1` | • The target SimplyPlural API version in production mode. <br/>• **Unless you are running your own fork of Simply Plural, you shouldn't change this.** |
| `auth_token` | | • Your SimplyPlural account authorization token. <br/>• Full permissions are necessary to use some features. |
| `user_id` | | • Your SimplyPlural user ID. <br/>• You can find it in account info near the bottom. |

#### Development mode
These keys will be used when running in development mode.
These should target the pretesting servers.

| Setting | Default | Description |
| --------| ------- | ----------- |
| `dev_api_url_http` | `https://api.apparyllis.com/v#/` | • The base URL for SimplyPlural API HTTP requests in development mode. <br/>• `#` is a wildcard for the API version and will be replaced at runtime. <br/>• **Unless you are running your own fork of Simply Plural, you shouldn't change this.** |
| `dev_api_url_socket` | `wss://api.apparyllis.com/v#/socket` | • The base URL for SimplyPlural API socket requests in development mode. <br/>• `#` is a wildcard for the API version and will be replaced at runtime. <br/>• **Unless you are running your own fork of Simply Plural, you shouldn't change this.** |
| `dev_api_version` | `1` | • The target SimplyPlural API version in development mode. <br/>• **Unless you are running your own fork of Simply Plural, you shouldn't change this.** |
| `dev_auth_token` | | • Your SimplyPlural development account authorization token. <br/>• Full permissions are necessary to use some features. <br/>• You will need to make an account on the pretesting servers. |
| `dev_user_id` | | • Your SimplyPlural development user ID. <br/>• You can find it in account info near the bottom. <br/>• You will need to make an account on the pretesting servers. |

## Links
- [SimplyPlural for Web](https://app.apparyllis.com)
- [SimplyPlural Discord](https://discord.com/invite/F7r4jZgENB)
- [SimplyPlural documentation](https://docs.apparyllis.com/docs/intro)

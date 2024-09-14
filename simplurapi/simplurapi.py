__all__ = ['SimPlurAPI']
__version__ = '0.1.0'
__author__ = 'SparkliTwizzl'


import json
import logging
import os
import requests
from dotenv import load_dotenv
from typing import Final


_moduleName:str = 'SimPlurAPI'


class _APIkeywords:
    _SUBTYPE_ANALYTICS:Final[str] = 'analytics'
    _SUBTYPE_AUTOMATED:Final[str] = 'automated'
    _TYPE_TIMERS:Final[str] = 'timers'
    _TYPE_USER:Final[str] = 'user'


class SimPlurAPI:
    class Config:
        _useDevelopmentMode:bool = True
        _useSocketConnection:bool = False


        def __init__( self, outer_instance ):
            self.outer = outer_instance


        def is_in_development_mode( self ):
            return self._useDevelopmentMode

        def is_in_production_mode( self ):
            return not self._useDevelopmentMode

        def is_using_http_connection( self ):
            return not self._useSocketConnection

        def is_using_socket_connection( self ):
            return self._useSocketConnection

        def set_to_development_mode( self ):
            self.outer._logger.info( 'Set %s to development mode.' % _moduleName )
            self._useDevelopmentMode = True
            if self.outer._devUserId is None or self.outer._devUserId == '':
                raise ValueError( 'Dev user ID cannot be blank.' )
            if self.outer._devAuthToken is None or self.outer._devAuthToken == '':
                raise ValueError( 'Dev auth token cannot be blank.' )

        def set_to_production_mode( self ):
            self.outer._logger.info( 'Set %s to production mode.' % _moduleName )
            self._useDevelopmentMode = False
            if self.outer._userId is None or self.outer._userId == '':
                raise ValueError( 'User ID cannot be blank.' )
            if self.outer._authToken is None or self.outer._authToken == '':
                raise ValueError( 'Auth token cannot be blank.' )

        def set_connection_to_http( self ):
            self.outer._logger.info( 'Set %s connection mode to HTTP.' % _moduleName )
            self._useSocketConnection = False

        def set_connection_to_socket( self ):
            self.outer._logger.info( 'Set %s connection mode to WebSocket.' % _moduleName )
            self._useSocketConnection = True


    config:Config

    _API_URL_HTTP_DEFAULT:Final[str] = "https://api.apparyllis.com/v#/"
    _API_URL_SOCKET_DEFAULT:Final[str] = "wss://api.apparyllis.com/v#/socket"
    _API_VERSION_DEFAULT:Final[int] = 1
    _DEV_API_URL_HTTP_DEFAULT:Final[str] = "https://devapi.apparyllis.com/v#/"
    _DEV_API_URL_SOCKET_DEFAULT:Final[str] = "wss://devapi.apparyllis.com/v#/socket"
    _DEV_API_VERSION_DEFAULT:Final[int] = 1

    _apiUrlHttp:str
    _apiUrlSocket:str
    _apiVersion:int
    _authToken:str
    _devApiUrlHttp:str
    _devApiUrlSocket:str
    _devApiVersion:int
    _devAuthToken:str
    _devUserId:str
    _isSocketConnectionAlive:bool = False
    _logger:logging
    _requests:requests
    _userId:str


    def __init__( self, requestProvider = requests ):
        self._logger = logging.getLogger( __name__ )
        self._load_env_values()
        self._requests = requestProvider
        self.config = SimPlurAPI.Config( self )


    # public non-API methods
    def api_url_http( self ):
        if self.config.is_in_development_mode():
            return self._devApiUrlHttp.replace( '#', self._devApiVersion )
        return self._apiUrlHttp.replace( '#', self._apiVersion )

    def api_url_socket( self ):
        if self.config.is_in_development_mode():
            return self._devApiUrlSocket.replace( '#', self._devApiVersion )
        return self._apiUrlSocket.replace( '#', self._apiVersion )

    def auth_token( self ):
        if self.config.is_in_development_mode():
            return self._devAuthToken
        return self._authToken

    def close_socket_connection( self ):
        if not self.config.is_using_socket_connection:
            raise ConnectionError( 'WebSocket connection is not enabled.' )
        if not self._isSocketConnectionAlive:
            raise ConnectionResetError( 'WebSocket connection is not open.' )
        #TODO
        raise NotImplemented

    def open_socket_connection( self ):
        if not self.config.is_using_socket_connection:
            raise ConnectionError( 'WebSocket connection is not enabled.' )
        if self._isSocketConnectionAlive:
            raise ConnectionRefusedError( 'WebSocket connection is already open.' )
        #TODO
        raise NotImplemented

    def user_id( self ):
        if self.config.is_in_development_mode():
            return self._devUserId
        return self._userId


    # public API methods
    def get_analytics( self ):
        response = self._send_http_get_request(
            type=_APIkeywords._TYPE_USER,
            subtype=_APIkeywords._SUBTYPE_ANALYTICS )
        return response


    def get_automated_timer( self, timerId:str ):
        #TODO
        raise NotImplemented

    def get_all_automated_timers_for_system( self, systemId:str ):
        response = self._send_http_get_request(
            type=_APIkeywords._TYPE_TIMERS,
            subtype=_APIkeywords._SUBTYPE_AUTOMATED,
            arg=systemId )
        return response

    def get_all_automated_timers_for_self( self ):
        return self.get_all_automated_timers_for_system( self.user_id() )

    def add_automated_timer( self, timerId:str, name:str, message:str, type:int, delayInHours:int ):
        #TODO
        raise NotImplemented

    def update_automated_timer( self, timerId:str, name:str, message:str, type:int, delayInHours:int ):
        #TODO
        raise NotImplemented

    def delete_automated_timer( self, timerId:str ):
        #TODO
        raise NotImplemented


    def get_board_message( self, messageId:str ):
        #TODO
        raise NotImplemented

    def get_all_board_messages_for_member( self, memberId:str ):
        #TODO
        raise NotImplemented

    def get_all_unread_board_messages( self ):
        #TODO
        raise NotImplemented

    def add_board_message( self, id, title:str, message:str, writtenBy:str, writtenFor:str, writtenAt:int, read:bool, supportMarkdown:bool ):
        #TODO
        raise NotImplemented

    def update_board_message( self, id, read:bool ):
        #TODO
        raise NotImplemented

    def delete_board_message( self, id ):
        #TODO
        raise NotImplemented


    def get_chat_message( self, id ):
        #TODO
        raise NotImplemented

    def get_all_chat_messages_for_channel( self, channelId:str ):
        #TODO
        raise NotImplemented

    def add_chat_message( self, id, message:str, channelId:str, writerId:str, writtenAt:int, replyToId:str ):
        #TODO
        raise NotImplemented

    def update_chat_message( self, id, message:str, updatedAt:int ):
        #TODO
        raise NotImplemented

    def delete_chat_message( self, id ):
        #TODO
        raise NotImplemented


    def get_chat_category( self, id ):
        #TODO
        raise NotImplemented

    def get_all_chat_categories( self, systemId:str ):
        #TODO
        raise NotImplemented

    def add_chat_category( self, id, name:str, description:str, channelIds:list ):
        #TODO
        raise NotImplemented

    def update_chat_category( self, id, name:str, description:str, channelIds:list ):
        #TODO
        raise NotImplemented

    def delete_chat_category( self, id ):
        #TODO
        raise NotImplemented


    def get_chat_channel( self, id ):
        #TODO
        raise NotImplemented

    def get_all_chat_channels( self, systemId:str ):
        #TODO
        raise NotImplemented

    def add_chat_channel( self, id, name:str, description:str ):
        #TODO
        raise NotImplemented

    def update_chat_channel( self, id, name:str, description:str ):
        #TODO
        raise NotImplemented

    def delete_chat_channel( self, id ):
        #TODO
        raise NotImplemented


    def get_comment( self, systemId:str, commentId:str ):
        #TODO
        raise NotImplemented

    def get_all_comments( self, commentId:str, type:str ):
        #TODO
        raise NotImplemented

    def add_comment( self, commentId:str, time:int, text:str, supportMarkdown:bool, parentDocId:str, collectionId:str ):
        #TODO
        raise NotImplemented

    def update_comment( self, commentId:str, text:str, supportMarkdown:bool ):
        #TODO
        raise NotImplemented

    def delete_comment( self, commentId:str ):
        #TODO
        raise NotImplemented


    def get_custom_front( self, frontId:str, systemId:str ):
        #TODO
        raise NotImplemented

    def get_all_custom_fronts( self, systemId:str ):
        #TODO
        raise NotImplemented

    def add_custom_front( self, frontId:str, name:str, description:str, avatarURL:str, color:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool ):
        #TODO
        raise NotImplemented

    def update_custom_front( self, frontId:str, name:str, description:str, avatarURL:str, color:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool ):
        #TODO
        raise NotImplemented

    def delete_custom_front( self, frontId:str ):
        #TODO
        raise NotImplemented


    def get_all_friends( self ):
        #TODO
        raise NotImplemented

    def get_all_recieved_friend_requests( self ):
        #TODO
        raise NotImplemented

    def get_all_sent_friend_requests( self ):
        #TODO
        raise NotImplemented

    def get_current_fronters_for_friend( self, userId:str ):
        #TODO
        raise NotImplemented

    def get_current_fronters_for_all_friends( self ):
        #TODO
        raise NotImplemented

    def get_friend_settings_for_user( self, userId:str, friendId:str ):
        #TODO
        raise NotImplemented

    def add_friend( self, user:str ):
        #TODO
        raise NotImplemented

    def respond_to_friend_request( self, user:str ):
        #TODO
        raise NotImplemented

    def update_settings_for_friend( self, user:str ):
        #TODO
        raise NotImplemented

    def delete_friend_request( self, user:str ):
        #TODO
        raise NotImplemented

    def remove_friend( self, user:str ):
        #TODO
        raise NotImplemented


    def get_all_current_fronters( self ):
        #TODO
        raise NotImplemented

    def get_front_history_entry( self, systemId:str, entryId:str ):
        #TODO
        raise NotImplemented

    def get_front_history_entries_for_timespan( self, systemId:str, startTime:int, endTime:int ):
        #TODO
        raise NotImplemented

    def get_front_history_entries_for_member( self, memberId:str, startTime:int, endTime:int ):
        #TODO
        raise NotImplemented

    def add_front_history_entry( self, entryId:str, customStatus:str, custom:bool, live:bool, startTime:int, endTime:int, fronterId:str ):
        #TODO
        raise NotImplemented

    def update_front_history_entry( self, entryId:str, customStatus:str, custom:bool, live:bool, startTime:int, endTime:int, fronterId:str ):
        #TODO
        raise NotImplemented

    def delete_front_history_entry( self, entryId:str ):
        #TODO
        raise NotImplemented



    def get_group( self, systemId:str, groupId:str ):
        #TODO
        raise NotImplemented

    def get_all_groups( self, systemId:str ):
        #TODO
        raise NotImplemented

    def add_group( self, groupId:str, name:str, description:str, color:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool, emoji:str, parentId:str, members:list ):
        #TODO
        raise NotImplemented

    def update_group( self, groupId:str, name:str, description:str, color:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool, emoji:str, parentId:str, members:list ):
        #TODO
        raise NotImplemented

    def delete_group( self, groupId:str ):
        #TODO
        raise NotImplemented


    def get_member( self, systemId:str, memberId: str ):
        #TODO
        raise NotImplemented

    def get_all_members( self, systemId:str ):
        #TODO
        raise NotImplemented

    def add_member( self, memberId:str, name:str, description:str, color:str, pronouns:str, pluralkitId:str, avatarURL:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool, preventFrontNotifs:bool, info ):
        #TODO
        raise NotImplemented

    def update_member( self, memberId:str, name:str, description:str, color:str, pronouns:str, pluralkitId:str, avatarURL:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool, preventFrontNotifs:bool, info ):
        #TODO
        raise NotImplemented

    def delete_member( self, memberId:str ):
        #TODO
        raise NotImplemented


    def get_note( self, systemId:str, noteId:str ):
        #TODO
        raise NotImplemented

    def get_all_notes( self, systemId:str ):
        #TODO
        raise NotImplemented

    def add_note( self, noteId:str, title:str, text:str, color:str, memberId:str, timestamp:int, supportDescMarkdown:bool ):
        #TODO
        raise NotImplemented

    def update_note( self, noteId:str, title:str, text:str, color:str, memberId:str, timestamp:int, supportDescMarkdown:bool ):
        #TODO
        raise NotImplemented

    def delete_note( self, noteId:str ):
        #TODO
        raise NotImplemented


    def get_poll( self, systemId:str, pollId:str ):
        #TODO
        raise NotImplemented

    def get_all_polls( self, systemId:str ):
        #TODO
        raise NotImplemented

    def add_poll( self, pollId:str, title:str, desc:str, allowAbstain:bool, allowVeto:bool, custom:bool, endTime:int, supportDescMarkdown:bool, options, votes ):
        #TODO
        raise NotImplemented

    def update_poll( self, pollId:str, title:str, desc:str, allowAbstain:bool, allowVeto:bool, custom:bool, endTime:int, supportDescMarkdown:bool, options, votes ):
        #TODO
        raise NotImplemented

    def delete_poll( self, pollId:str ):
        #TODO
        raise NotImplemented


    def sync_member_from_pluralkit( self, memberId:str ):
        #TODO
        raise NotImplemented

    def sync_member_to_pluralkit( self, memberId:str ):
        #TODO
        raise NotImplemented

    def sync_all_members_from_pluralkit( self ):
        #TODO
        raise NotImplemented

    def sync_all_members_to_pluralkit( self ):
        #TODO
        raise NotImplemented


    def get_repeated_timer( self, systemId:str, timerId:str ):
        #TODO
        raise NotImplemented

    def get_all_repeated_timers( self, systemId:str ):
        #TODO
        raise NotImplemented

    def add_repeated_timer( self, timerId:str, title:str, text:str, dayInterval:int, time, startTime ):
        #TODO
        raise NotImplemented

    def update_repeated_timer( self, timerId:str, title:str, text:str, dayInterval:int, time, startTime ):
        #TODO
        raise NotImplemented

    def delete_repeated_timer( self, timerId:str ):
        #TODO
        raise NotImplemented


    def get_user_id_for_auth_token( self ):
        #TODO
        raise NotImplemented

    def get_user( self, userId:str ):
        #TODO
        raise NotImplemented

    def get_all_reports( self ):
        #TODO
        raise NotImplemented

    def generate_report( self ):
        #TODO
        raise NotImplemented

    def update_user( self, userId:str ):
        #TODO
        raise NotImplemented

    def set_username( self, userId:str, username:str ):
        #TODO
        raise NotImplemented

    def delete_report( self, reportId:str ):
        #TODO
        raise NotImplemented


    # private methods
    def _load_env_values( self ):
        try:
            load_dotenv()
        except Exception:
            raise FileNotFoundError( '.env file was not found.' )

        self._apiUrlHttp = os.getenv( 'api_url_http', self._API_URL_HTTP_DEFAULT )
        self._apiUrlSocket = os.getenv( 'api_url_socket', self._API_URL_SOCKET_DEFAULT )
        self._apiVersion = os.getenv( 'api_version', self._API_VERSION_DEFAULT )
        self._authToken = os.getenv( 'auth_token' )
        self._userId = os.getenv( 'user_id' )

        self._devApiUrlHttp = os.getenv( 'dev_api_url_http', self._DEV_API_URL_HTTP_DEFAULT )
        self._devApiUrlSocket = os.getenv( 'dev_api_url_socket', self._DEV_API_URL_SOCKET_DEFAULT )
        self._devApiVersion = os.getenv( 'dev_api_version', self._DEV_API_VERSION_DEFAULT )
        self._devAuthToken = os.getenv( 'dev_auth_token' )
        self._devUserId = os.getenv( 'dev_user_id' )

    def _log_response( self, response:requests.Response ):
        request = response.request
        method = request.method
        url = request.url
        url = url.replace( self.auth_token(), '_AUTH_TOKEN_' )
        url = url.replace( self.user_id(), '_USER_ID_' )
        statusCode = response.status_code
        reason = response.reason
        elapsed = response.elapsed.total_seconds()
        self._logger.info( '%s %s returned %d (%s) in %f seconds' % ( method, url, statusCode, reason, elapsed ) )

    def _request_headers_http( self ):
        authToken = self._devAuthToken if self.config.is_in_development_mode else self._authToken
        return {
            'Content-Type': 'application/json',
            'Authorization': authToken
        }

    def _request_url_http( self, type:str, subtype:str='', arg:str='' ):
        base = self.api_url_http()
        url = os.path.join( base, type, subtype, arg ).replace( '\\', '/' )
        if url.endswith( '/' ): # request URLs cannot have a trailing slash
            url = url[ slice( -1 ) ]
        return url

    def _send_http_get_request( self, type:str, subtype:str = '', arg:str = '', params:dict = {}, body:dict = {} ):
        return self._send_http_request( 'GET', type, subtype, arg, params, body )

    def _send_http_patch_request( self, type:str, subtype:str = '', arg:str = '', params:dict = {}, body:dict = {} ):
        return self._send_http_request( 'PATCH', type, subtype, arg, params, body )

    def _send_http_post_request( self, type:str, subtype:str = '', arg:str = '', params:dict = {}, body:dict = {} ):
        return self._send_http_request( 'POST', type, subtype, arg, params, body )

    def _send_http_delete_request( self, type:str, subtype:str = '', arg:str = '', params:dict = {}, body:dict = {} ):
        return self._send_http_request( 'DEL', type, subtype, arg, params, body )

    def _send_http_request( self, method:str, type:str, subtype:str, arg:str, params:dict, body:dict ):
        url = self._request_url_http( type, subtype, arg )
        headers = self._request_headers_http()
        response = self._requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json.dumps( body ) if body != {} else body )
        self._log_response( response )
        return response

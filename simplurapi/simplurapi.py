__all__ = ['SimPlurAPI']
__version__ = '0.1.0'


import os
from dotenv import load_dotenv


class SimPlurAPI:
    _apiUrlHttp:str
    _apiUrlHttpDefault:str = "https://api.apparyllis.com/v#/"
    _apiUrlSocket:str
    _apiUrlSocketDefault:str = "wss://api.apparyllis.com/v#/socket"
    _apiVersion:int
    _apiVersionDefault:int = 1
    _authToken:str
    _userId:str

    _devApiUrlHttp:str
    _devApiUrlHttpDefault:str = "https://devapi.apparyllis.com/v#/"
    _devApiUrlSocket:str
    _devApiUrlSocketDefault:str = "wss://devapi.apparyllis.com/v#/socket"
    _devApiVersion:int
    _devApiVersionDefault:int = 1
    _devAuthToken:str
    _devUserId:str

    _isSocketConnectionAlive:bool = False
    _useDevelopmentMode:bool = True
    _useSocketConnection:bool = False


    def __init__( self ):
        self._load_env_values()
        raise NotImplemented


    def use_development_mode( self ):
        self._useDevelopmentMode = True
        raise NotImplemented

    def use_production_mode( self ):
        self._useDevelopmentMode = False
        raise NotImplemented

    def use_http_connection( self ):
        self._useSocketConnection = False
        raise NotImplemented

    def use_socket_connection( self ):
        self._useSocketConnection = True
        raise NotImplemented

    def open_socket_connection( self ):
        if not self._useSocketConnection:
            raise ConnectionError( 'Socket connection is not enabled.' )
        if self._isSocketConnectionAlive:
            raise ConnectionRefusedError( 'Socket connection is already open.' )
        raise NotImplemented

    def close_socket_connection( self ):
        if not self._useSocketConnection:
            raise ConnectionError( 'Socket connection is not enabled.' )
        if not self._isSocketConnectionAlive:
            raise ConnectionResetError( 'Socket connection is not open.' )
        raise NotImplemented


    def get_analytics( self ):
        raise NotImplemented


    def get_automated_timer( self, timerId:str ):
        raise NotImplemented

    def get_all_automated_timers( self, systemId:str ):
        raise NotImplemented

    def add_automated_timer( self, timerId:str, name:str, message:str, type:int, delayInHours:int ):
        raise NotImplemented

    def update_automated_timer( self, timerId:str, name:str, message:str, type:int, delayInHours:int ):
        raise NotImplemented

    def delete_automated_timer( self, timerId:str ):
        raise NotImplemented


    def get_board_message( self, messageId:str ):
        raise NotImplemented

    def get_all_board_messages_for_member( self, memberId:str ):
        raise NotImplemented

    def get_all_unread_board_messages( self ):
        raise NotImplemented

    def add_board_message( self, id, title:str, message:str, writtenBy:str, writtenFor:str, writtenAt:int, read:bool, supportMarkdown:bool ):
        raise NotImplemented

    def update_board_message( self, id, read:bool ):
        raise NotImplemented

    def delete_board_message( self, id ):
        raise NotImplemented


    def get_chat_message( self, id ):
        raise NotImplemented

    def get_all_chat_messages_for_channel( self, channelId:str ):
        raise NotImplemented

    def add_chat_message( self, id, message:str, channelId:str, writerId:str, writtenAt:int, replyToId:str ):
        raise NotImplemented

    def update_chat_message( self, id, message:str, updatedAt:int ):
        raise NotImplemented

    def delete_chat_message( self, id ):
        raise NotImplemented


    def get_chat_category( self, id ):
        raise NotImplemented

    def get_all_chat_categories( self, systemId:str ):
        raise NotImplemented

    def add_chat_category( self, id, name:str, description:str, channelIds:list ):
        raise NotImplemented

    def update_chat_category( self, id, name:str, description:str, channelIds:list ):
        raise NotImplemented

    def delete_chat_category( self, id ):
        raise NotImplemented


    def get_chat_channel( self, id ):
        raise NotImplemented

    def get_all_chat_channels( self, systemId:str ):
        raise NotImplemented

    def add_chat_channel( self, id, name:str, description:str ):
        raise NotImplemented

    def update_chat_channel( self, id, name:str, description:str ):
        raise NotImplemented

    def delete_chat_channel( self, id ):
        raise NotImplemented


    def get_comment( self, systemId:str, commentId:str ):
        raise NotImplemented

    def get_all_comments( self, commentId:str, type:str ):
        raise NotImplemented

    def add_comment( self, commentId:str, time:int, text:str, supportMarkdown:bool, parentDocId:str, collectionId:str ):
        raise NotImplemented

    def update_comment( self, commentId:str, text:str, supportMarkdown:bool ):
        raise NotImplemented

    def delete_comment( self, commentId:str ):
        raise NotImplemented


    def get_custom_front( self, frontId:str, systemId:str ):
        raise NotImplemented

    def get_all_custom_fronts( self, systemId:str ):
        raise NotImplemented

    def add_custom_front( self, frontId:str, name:str, description:str, avatarURL:str, color:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool ):
        raise NotImplemented

    def update_custom_front( self, frontId:str, name:str, description:str, avatarURL:str, color:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool ):
        raise NotImplemented

    def delete_custom_front( self, frontId:str ):
        raise NotImplemented


    def get_all_friends( self ):
        raise NotImplemented

    def get_all_recieved_friend_requests( self ):
        raise NotImplemented

    def get_all_sent_friend_requests( self ):
        raise NotImplemented

    def get_current_fronters_for_friend( self, userId:str ):
        raise NotImplemented

    def get_current_fronters_for_all_friends( self ):
        raise NotImplemented

    def get_friend_settings_for_user( self, userId:str, friendId:str ):
        raise NotImplemented

    def add_friend( self, user:str ):
        raise NotImplemented

    def respond_to_friend_request( self, user:str ):
        raise NotImplemented

    def update_settings_for_friend( self, user:str ):
        raise NotImplemented

    def delete_friend_request( self, user:str ):
        raise NotImplemented

    def remove_friend( self, user:str ):
        raise NotImplemented


    def get_all_current_fronters( self ):
        raise NotImplemented

    def get_front_history_entry( self, systemId:str, entryId:str ):
        raise NotImplemented

    def get_front_history_entries_for_timespan( self, systemId:str, startTime:int, endTime:int ):
        raise NotImplemented

    def get_front_history_entries_for_member( self, memberId:str, startTime:int, endTime:int ):
        raise NotImplemented

    def add_front_history_entry( self, entryId:str, customStatus:str, custom:bool, live:bool, startTime:int, endTime:int, fronterId:str ):
        raise NotImplemented

    def update_front_history_entry( self, entryId:str, customStatus:str, custom:bool, live:bool, startTime:int, endTime:int, fronterId:str ):
        raise NotImplemented

    def delete_front_history_entry( self, entryId:str ):
        raise NotImplemented



    def get_group( self, systemId:str, groupId:str ):
        raise NotImplemented

    def get_all_groups( self, systemId:str ):
        raise NotImplemented

    def add_group( self, groupId:str, name:str, description:str, color:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool, emoji:str, parentId:str, members:list ):
        raise NotImplemented

    def update_group( self, groupId:str, name:str, description:str, color:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool, emoji:str, parentId:str, members:list ):
        raise NotImplemented

    def delete_group( self, groupId:str ):
        raise NotImplemented


    def get_member( self, systemId:str, memberId: str ):
        raise NotImplemented

    def get_all_members( self, systemId:str ):
        raise NotImplemented

    def add_member( self, memberId:str, name:str, description:str, color:str, pronouns:str, pluralkitId:str, avatarURL:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool, preventFrontNotifs:bool, info ):
        raise NotImplemented

    def update_member( self, memberId:str, name:str, description:str, color:str, pronouns:str, pluralkitId:str, avatarURL:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool, preventFrontNotifs:bool, info ):
        raise NotImplemented

    def delete_member( self, memberId:str ):
        raise NotImplemented


    def get_note( self, systemId:str, noteId:str ):
        raise NotImplemented

    def get_all_notes( self, systemId:str ):
        raise NotImplemented

    def add_note( self, noteId:str, title:str, text:str, color:str, memberId:str, timestamp:int, supportDescMarkdown:bool ):
        raise NotImplemented

    def update_note( self, noteId:str, title:str, text:str, color:str, memberId:str, timestamp:int, supportDescMarkdown:bool ):
        raise NotImplemented

    def delete_note( self, noteId:str ):
        raise NotImplemented


    def get_poll( self, systemId:str, pollId:str ):
        raise NotImplemented

    def get_all_polls( self, systemId:str ):
        raise NotImplemented

    def add_poll( self, pollId:str, title:str, desc:str, allowAbstain:bool, allowVeto:bool, custom:bool, endTime:int, supportDescMarkdown:bool, options, votes ):
        raise NotImplemented

    def update_poll( self, pollId:str, title:str, desc:str, allowAbstain:bool, allowVeto:bool, custom:bool, endTime:int, supportDescMarkdown:bool, options, votes ):
        raise NotImplemented

    def delete_poll( self, pollId:str ):
        raise NotImplemented


    def sync_member_from_pluralkit( self, memberId:str ):
        raise NotImplemented

    def sync_member_to_pluralkit( self, memberId:str ):
        raise NotImplemented

    def sync_all_members_from_pluralkit( self ):
        raise NotImplemented

    def sync_all_members_to_pluralkit( self ):
        raise NotImplemented


    def get_repeated_timer( self, systemId:str, timerId:str ):
        raise NotImplemented

    def get_all_repeated_timers( self, systemId:str ):
        raise NotImplemented

    def add_repeated_timer( self, timerId:str, title:str, text:str, dayInterval:int, time, startTime ):
        raise NotImplemented

    def update_repeated_timer( self, timerId:str, title:str, text:str, dayInterval:int, time, startTime ):
        raise NotImplemented

    def delete_repeated_timer( self, timerId:str ):
        raise NotImplemented


    def get_user_id_for_auth_token( self ):
        raise NotImplemented

    def get_user( self, userId:str ):
        raise NotImplemented

    def get_all_reports( self ):
        raise NotImplemented

    def generate_report( self ):
        raise NotImplemented

    def update_user( self, userId:str ):
        raise NotImplemented

    def set_username( self, userId:str, username:str ):
        raise NotImplemented

    def delete_report( self, reportId:str ):
        raise NotImplemented


    def _load_env_values( self ):
        try:
            load_dotenv()
        except Exception:
            raise NotImplemented
        self._apiUrlHttp = os.getenv( 'api_url_http', self._apiUrlHttpDefault )
        self._apiUrlSocket = os.getenv( 'api_url_socket', self._apiUrlSocketDefault )
        self._apiVersion = os.getenv( 'api_version', self._apiVersionDefault )
        self._authToken = os.getenv( 'auth_token' )
        self._userId = os.getenv( 'user_id' )
        self._devApiUrlHttp = os.getenv( 'dev_api_url_http', self._devApiUrlHttpDefault )
        self._devApiUrlSocket = os.getenv( 'dev_api_url_socket', self._devApiUrlSocketDefault )
        self._devApiVersion = os.getenv( 'dev_api_version', self._devApiVersionDefault )
        self._devAuthToken = os.getenv( 'dev_auth_token' )
        self._devUserId = os.getenv( 'dev_user_id' )

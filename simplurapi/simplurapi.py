__all__ = ['SimPlurAPI']


class SimPlurAPI:
    _APIbaseURL:str
    _APIversion:int
    _authToken:str
    _devAuthToken:str
    _devUserID:str
    _isSocketConnectionAlive:bool = False
    _useDevelopmentMode:bool = True
    _useSocketConnection:bool = False
    _userID:str


    def __init__( self ):
        raise NotImplemented


    def use_development_mode( self ):
        raise NotImplemented

    def use_production_mode( self ):
        raise NotImplemented

    def use_http_connection( self ):
        raise NotImplemented

    def use_socket_connection( self ):
        raise NotImplemented

    def open_socket_connection( self ):
        raise NotImplemented

    def close_socket_connection( self ):
        raise NotImplemented


    def get_analytics( self ):
        raise NotImplemented


    def get_automated_timer( self, timerID:str ):
        raise NotImplemented

    def get_all_automated_timers( self, systemID:str ):
        raise NotImplemented

    def add_automated_timer( self, timerID:str, name:str, message:str, type:int, delayInHours:int ):
        raise NotImplemented

    def update_automated_timer( self, timerID:str, name:str, message:str, type:int, delayInHours:int ):
        raise NotImplemented

    def delete_automated_timer( self, docID:str ):
        raise NotImplemented


    def get_board_message( self, messageID:str ):
        raise NotImplemented

    def get_all_board_messages_for_member( self, memberID:str ):
        raise NotImplemented

    def get_all_unread_board_messages( self ):
        raise NotImplemented

    def add_board_message( self, ID, title:str, message:str, writtenBy:str, writtenFor:str, writtenAt:int, read:bool, supportMarkdown:bool ):
        raise NotImplemented

    def update_board_message( self, ID, read:bool ):
        raise NotImplemented

    def delete_board_message( self, ID ):
        raise NotImplemented


    def get_chat_message( self, ID ):
        raise NotImplemented

    def get_all_chat_messages_for_channel( self, channelID:str ):
        raise NotImplemented

    def add_chat_message( self, ID, message:str, channelID:str, writerID:str, writtenAt:int, replyToID:str ):
        raise NotImplemented

    def update_chat_message( self, ID, message:str, updatedAt:int ):
        raise NotImplemented

    def delete_chat_message( self, ID ):
        raise NotImplemented


    def get_chat_category( self, ID ):
        raise NotImplemented

    def get_all_chat_categories( self, systemID:str ):
        raise NotImplemented

    def add_chat_category( self, ID, name:str, description:str, channelIDs:list ):
        raise NotImplemented

    def update_chat_category( self, ID, name:str, description:str, channelIDs:list ):
        raise NotImplemented

    def delete_chat_category( self, ID ):
        raise NotImplemented


    def get_chat_channel( self, ID ):
        raise NotImplemented

    def get_all_chat_channels( self, systemID:str ):
        raise NotImplemented

    def add_chat_channel( self, ID, name:str, description:str ):
        raise NotImplemented

    def update_chat_channel( self, ID, name:str, description:str ):
        raise NotImplemented

    def delete_chat_channel( self, ID ):
        raise NotImplemented


    def get_comment( self, systemID:str, commentID:str ):
        raise NotImplemented

    def get_all_comments( self, commentID:str, type:str ):
        raise NotImplemented

    def add_comment( self, commentID:str, time:int, text:str, supportMarkdown:bool, parentDocID:str, collectionID:str ):
        raise NotImplemented

    def update_comment( self, commentID:str, text:str, supportMarkdown:bool ):
        raise NotImplemented

    def delete_comment( self, commentID:str ):
        raise NotImplemented


    def get_custom_front( self, frontID:str, systemID:str ):
        raise NotImplemented

    def get_all_custom_fronts( self, systemID:str ):
        raise NotImplemented

    def add_custom_front( self, frontID:str, name:str, description:str, avatarURL:str, color:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool ):
        raise NotImplemented

    def update_custom_front( self, frontID:str, name:str, description:str, avatarURL:str, color:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool ):
        raise NotImplemented

    def delete_custom_front( self, frontID:str ):
        raise NotImplemented


    def get_all_friends( self ):
        raise NotImplemented

    def get_all_recieved_friend_requests( self ):
        raise NotImplemented

    def get_all_sent_friend_requests( self ):
        raise NotImplemented

    def get_current_fronters_for_friend( self, userID:str ):
        raise NotImplemented

    def get_current_fronters_for_all_friends( self ):
        raise NotImplemented

    def get_friend_settings_for_user( self, userID:str, friendID:str ):
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

    def get_front_history_entry( self, systemID:str, entryID:str ):
        raise NotImplemented

    def get_front_history_entries_for_timespan( self, systemID:str, startTime:int, endTime:int ):
        raise NotImplemented

    def get_front_history_entries_for_member( self, memberID:str, startTime:int, endTime:int ):
        raise NotImplemented

    def add_front_history_entry( self, entryID:str, customStatus:str, custom:bool, live:bool, startTime:int, endTime:int, fronterID:str ):
        raise NotImplemented

    def update_front_history_entry( self, entryID:str, customStatus:str, custom:bool, live:bool, startTime:int, endTime:int, fronterID:str ):
        raise NotImplemented

    def delete_front_history_entry( self, entryID:str ):
        raise NotImplemented



    def get_group( self, systemID:str, groupID:str ):
        raise NotImplemented

    def get_all_groups( self, systemID:str ):
        raise NotImplemented

    def add_group( self, groupID:str, name:str, description:str, color:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool, emoji:str, parentID:str, members:list ):
        raise NotImplemented

    def update_group( self, groupID:str, name:str, description:str, color:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool, emoji:str, parentID:str, members:list ):
        raise NotImplemented

    def delete_group( self, groupID:str ):
        raise NotImplemented


    def get_member( self, systemID:str, memberID: str ):
        raise NotImplemented

    def get_all_members( self, systemID:str ):
        raise NotImplemented

    def add_member( self, memberID:str, name:str, description:str, color:str, pronouns:str, pluralkitID:str, avatarURL:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool, preventFrontNotifs:bool, info ):
        raise NotImplemented

    def update_member( self, memberID:str, name:str, description:str, color:str, pronouns:str, pluralkitID:str, avatarURL:str, private:bool, preventTrusted:bool, supportDescMarkdown:bool, preventFrontNotifs:bool, info ):
        raise NotImplemented

    def delete_member( self, memberID:str ):
        raise NotImplemented


    def get_note( self, systemID:str, noteID:str ):
        raise NotImplemented

    def get_all_notes( self, systemID:str ):
        raise NotImplemented

    def add_note( self, noteID:str, title:str, text:str, color:str, memberID:str, timestamp:int, supportDescMarkdown:bool ):
        raise NotImplemented

    def update_note( self, noteID:str, title:str, text:str, color:str, memberID:str, timestamp:int, supportDescMarkdown:bool ):
        raise NotImplemented

    def delete_note( self, noteID:str ):
        raise NotImplemented


    def get_poll( self, systemID:str, pollID:str ):
        raise NotImplemented

    def get_all_polls( self, systemID:str ):
        raise NotImplemented

    def add_poll( self, pollID:str, title:str, desc:str, allowAbstain:bool, allowVeto:bool, custom:bool, endTime:int, supportDescMarkdown:bool, options, votes ):
        raise NotImplemented

    def update_poll( self, pollID:str, title:str, desc:str, allowAbstain:bool, allowVeto:bool, custom:bool, endTime:int, supportDescMarkdown:bool, options, votes ):
        raise NotImplemented

    def delete_poll( self, pollID:str ):
        raise NotImplemented


    def sync_member_from_pluralkit( self, memberID:str ):
        raise NotImplemented

    def sync_member_to_pluralkit( self, memberID:str ):
        raise NotImplemented

    def sync_all_members_from_pluralkit( self ):
        raise NotImplemented

    def sync_all_members_to_pluralkit( self ):
        raise NotImplemented


    def get_repeated_timer( self, systemID:str, timerID:str ):
        raise NotImplemented

    def get_all_repeated_timers( self, systemID:str ):
        raise NotImplemented

    def add_repeated_timer( self, timerID:str, title:str, text:str, dayInterval:int, time, startTime ):
        raise NotImplemented

    def update_repeated_timer( self, timerID:str, title:str, text:str, dayInterval:int, time, startTime ):
        raise NotImplemented

    def delete_repeated_timer( self, timerID:str ):
        raise NotImplemented


    def get_user_id_for_auth_token( self ):
        raise NotImplemented

    def get_user( self, userID:str ):
        raise NotImplemented

    def get_all_reports( self ):
        raise NotImplemented

    def generate_report( self ):
        raise NotImplemented

    def update_user( self, userID:str ):
        raise NotImplemented

    def set_username( self, userID:str, username:str ):
        raise NotImplemented

    def delete_report( self, reportID:str ):
        raise NotImplemented

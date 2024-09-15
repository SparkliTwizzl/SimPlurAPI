from datetime import datetime, timezone


def unix_epoch_timestamp( year=1970, month=1, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=timezone.utc ):
    dt = datetime( year, month, day, hour, minute, second, microsecond, tzinfo )
    return int( dt.timestamp() * 1000 )

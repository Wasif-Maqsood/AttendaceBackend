import jwt, datetime

def  create_access_tokken(id):
    return jwt.encode({
        'user_id' :id,
        'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=50),
        'iat': datetime.datetime.utcnow()
    }, 'access_secret', algorithm='HS256')

def  create_refresh_tokken(id):
    return jwt.encode({
        'user_id' :id,
        'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=5),
        'iat': datetime.datetime.utcnow()
    }, 'refresh_secret', algorithm='HS256')
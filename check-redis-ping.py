#!/bin/python
import redis
import argparse
import sys

# Show the Help Menu
parser = argparse.ArgumentParser()
parser.add_argument("-H", "--hostname", help="The hostname of Redis endpoint")
parser.add_argument("-P", "--password", help="The pass to access the Redis endpoint")
parser.add_argument("-p", "--port", help="The Redis port")
parser.add_argument("--ssl", help="Yes/No")
args_redis = parser.parse_args()

# The function to know if the Redis connection
# has the SSL connection

def redis_connection(myHostname=None, myPassword=None, myPort=6380, mySSL="No"):
    if mySSL == "yes".lower():
        r = redis.StrictRedis(host=myHostname, port=myPort,password=myPassword,ssl=True)
        result = r.ping()
        if result == True:
            print("Ping returned : Redis OK - {}".format(myHostname))
            sys.exit(0)
        elif result == False:
            print("Ping returned : Redis CRITICAL - {}".format(myHostname))
            sys.exit(2)
        else:
            print("There is a issue with Redis AUTH.")
            sys.exit(1)
    else:
        if mySSL == "no".lower():
            r = redis.StrictRedis(host=myHostname, port=myPort,password=myPassword,ssl=False)
            result = r.ping()
            if result == True:
                print("Ping returned : Redis OK - {}".format(myHostname))
                sys.exit(0)
            elif result == False:
                print("Ping returned : Redis CRITICAL - {}".format(myHostname))
                sys.exit(2)
            else:
                print("There is a issue with Redis AUTH.")
                sys.exit(1)  

# Using Try/Except to catch the Response Error

try:
     redis_connection(args_redis.hostname, args_redis.password, args_redis.port, args_redis.ssl)
except redis.exceptions.ResponseError as err:
    print(err)
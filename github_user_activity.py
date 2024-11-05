"""
Github user activity CLI

Beginner project from Roadmap.sh

A simple project to fetch the recent activity of a GitHub user and display in terminal
"""
import sys, requests

def main():
    
    #if length of sys.argv is 0, say its too short...
    if len(sys.argv) < 2 :
        print('no arguments provided, please add a github username as an argument')
    elif len(sys.argv) > 2 :
        print('too many arguments, please add 1 github username as an argument')
    else :
        username = sys.argv[1]
        print('username: ', username)

    #set the access token
    access_token = 'YOUR_API_TOKEN'

    #set the api endpoint
    url = 'https://api.github.com/users/<username>/events'
    #edit this to add username....

    #send the requests.get()

    #deal with the returned status code....

    #read the returned json data and print....

if __name__ == "__main__" :
    main()
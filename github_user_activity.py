"""
Github user activity CLI

Beginner project from Roadmap.sh

A simple project to fetch the recent activity of a GitHub user and display in terminal
"""
import sys
import requests

def main():
    """main function, taking the github username as the argument and printing the user activity"""

    #if length of sys.argv is 0, say its too short...
    if len(sys.argv) < 2 :
        print('no arguments provided, please add a github username as an argument')
    elif len(sys.argv) > 2 :
        print('too many arguments, please add 1 github username as an argument')
    else :
        username = sys.argv[1]
        print('username: ', username)

    #set the access token
    #access_token = 'YOUR_API_TOKEN'

    #set the api endpoint
    url = f'https://api.github.com/users/{username}/events'
    #edit this to add username....
    #print('this is the url: https://api.github.com/users/',username,'/events')

    #send the GET request
    response = requests.get(url, timeout = 10)

    print(response)

    #check the response status code
    if response.status_code == 200:
        #parse the JSON response
        events = response.json()

        #print each event type and created at time
        for index, event in enumerate(events):
            if index > 4:
                break
            print(f"Event: {event['type']}")

    else :
        print(f'Error: {response.status_code}')

    #deal with the returned status code....

    #read the returned json data and print....

if __name__ == "__main__" :
    main()

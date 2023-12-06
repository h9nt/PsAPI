from requests import Session
from colorama import init
from os import system

request = Session()
init(autoreset=True)
system('cls')

# - Color Change & Name Remove don't work anymore i think lmao.


class PsAPI(object):
    @staticmethod
    def RemoveAvatar(token: str) -> str: # Tested and Working.
        try:
            url = "https://us-prof.np.community.playstation.net/userProfile/v1/users/me/avatar"
            
            payload = {"avatarId": "0"}
            
            headers = {
                "Content-Type"  : "application/json",
                "Origin"        : "https://id.sonyentertainmentnetwork.com",
                "User-Agent"    : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                "Authorization" : "Bearer {}".format(token.replace("Bearer", ""))
            }
            
            response = request.request("PUT", url, json=payload, headers=headers)
            if response.status_code != 204 or response.text != "":
                return False
            else:
                return True
        except Exception as e:
            print(str(e))
    
    @staticmethod
    def changeProfileColor(token: str, color) -> dict: # Buggy and don't work anymore i think.
        try:
            url = "https://profile.api.playstation.com/v1/users/me/profile/backgroundImage"
            
            payload = {
                "backgroundImage"   : {"color": "{}".format(hex(color).replace(" ", ""))},
                "availability"      : {}
            }
            
            headers = {
                "Content-Type"  : "application/json",
                "User-Agent"    : "PlayStation/19.10.0(Android)",
                "Authorization" : "Bearer {}".format(token.replace("Bearer", ""))
            }

            response = request.request("GET", url, json=payload, headers=headers)
            if response.status_code != 204 or response.text != "":
                return False
            else:
                return True
        except Exception as e:
            print(str(e))
    
    @staticmethod
    def removeFirstName(token: str) -> dict: # Buggy & Don't work anymore [Possibly]
        try:
            url = "https://accounts.api.playstation.com/api/v1/accounts/me/communication"
            
            payload = {
                "communicationName": {
                    "first": "",
                    "last": ""
                },
                "communicationNamePhonetic": {
                    "first": "",
                    "last": ""
                },
                "communicationPreferences": {
                    "availableNotifications": [
                        {
                            "code": "sonyCommunications",
                            "optedIn": False
                        },
                        {
                            "code": "partnerCommunications",
                            "optedIn": False
                        }
                    ],
                    "realName": {
                        "name": {
                            "first": "",
                            "middle": "",
                            "last": ""
                        }
                    }
                }
            }
        
            headers = {
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                "Origin": "https://id.sonyentertainmentnetwork.com",
                "Authorization": "Bearer {}".format(token.replace("Bearer", ""))
            }

            response = request.request("PUT", url, json=payload, headers=headers)
            if response.status_code != 204 or response.text != "":
                return False
            else:
                return True
        except Exception as e:
            print(str(e))

# made with <3 by @Fhivo.
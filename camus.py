###############################################################################
#                                   <Camus>                                   #
#                                                                             #
#                                                 Book & Movie Data Parser    #
#                                             Designed by Chianti Scarlett    #
###############################################################################


from modules.core import set_API_CLIENT, set_API_SECRET
from modules.parser import NaverAPI

# Initialize API with global keys
set_API_CLIENT(NAVER_API_CLIENT_KEY)
set_API_SECRET(NAVER_API_SECRET)


def main():
    API = NaverAPI()
    data = API.load_movie({'query': '타이타닉'})
    print(data)


if __name__ == "__main__":
    main()

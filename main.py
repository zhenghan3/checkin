
from message_send import MessageSend
from config import message_tokens, youdao_cookie,ali_refresh_token,ty_pwd,ty_user
import youdao , aliyunpan, tianyiyunpan

def run():
    content =''
    title = ""
    if youdao_cookie != None:
        content = youdao.signin(youdao_cookie) +'\n\n'
        title = "【有道】"
    if ali_refresh_token != None :
        access_token, _ = aliyunpan.get_access_token(ali_refresh_token)
        content += aliyunpan.sign_in(access_token) + '\n\n'
        title += "【阿里】"
    if ty_user != None and ty_pwd != None:
        content += tianyiyunpan.main(ty_user, ty_pwd)
        title += "【天翼】"

    send = MessageSend()
    send.send_all(message_tokens,title+'每日签到',content)
if __name__ == "__main__":
    run()


    



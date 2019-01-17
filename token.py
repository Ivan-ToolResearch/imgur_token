#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 12:53:30 2018

@author: cheating
"""

from imgurpython import ImgurClient


# 讓你輸入字串
def get_input(string):
    return input(string)


def authenticate():
    # Get client ID and secret from config.py
    client_id = '你的ID'
    client_secret = '你的secret'
    client = ImgurClient(client_id, client_secret)

    # 進行請求，取得URL，要利用瀏覽去登入該網址，才能取得等等的pin碼
    authorization_url = client.get_auth_url('pin')

    print("Go to the following URL: {0}".format(authorization_url))

    # 要求輸入網頁中的pin碼
    pin = get_input("Enter pin code: ")

    # 獲取TOKEN
    credentials = client.authorize(pin, 'pin')
    client.set_user_auth(credentials['access_token'], credentials['refresh_token'])

    print("Authentication successful! Here are the details:")
    print("   Access token:  {0}".format(credentials['access_token']))
    print("   Refresh token: {0}".format(credentials['refresh_token']))

    return client



if __name__ == "__main__":
    authenticate()

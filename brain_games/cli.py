#!/usr/bin/env/ python3
import prompt


def welcome_user():
    username = prompt.string('May I have your name?' )
    print(f'Hello, {username}! ')

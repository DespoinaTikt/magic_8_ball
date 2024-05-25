import random

def ballreply(replyNum):
    if replyNum == 1:
        return 'It is certain'
    elif replyNum == 2:
        return 'It is decidedly so'
    elif replyNum == 3:
        return 'Yes - definitely'
    elif replyNum == 4 :
        return 'Ask again later'
    elif replyNum == 5 :
        return 'Outlook not so good'
    elif replyNum == 6:
        return 'My reply is no'
    elif replyNum == 7:
        return 'Do not count on it'
    elif replyNum == 8:
        return 'Very doubtful'
    elif replyNum == 9:
        return 'Signs point to yes'
    elif replyNum == 10:
        return 'Most likely'
    elif replyNum == 11:
        return 'As I see it yes'
    elif replyNum == 12:
        return 'Outlook good'
    elif replyNum == 13:
        return 'Yes'
    elif replyNum == 14:
        return 'Concentrate and ask again later'
    elif replyNum == 15:
        return 'Cannot predict now'
    elif replyNum == 16:
        return 'Better not tell you now'
    elif replyNum == 17:
        return 'Reply hazy, try again'
    elif replyNum == 18:
        return 'My sources say no'
    elif replyNum == 19:
        return 'You may rely on it'
    elif replyNum == 20:
        return 'Without a doubt'

print('Think of a yes/no question and press enter to see the result')

input()

print(ballreply(random.randint(1,20)))
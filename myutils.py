def sendMsg(soc, msg):
    '''
    soc is the socket object called to send the message: soc.send(msg)
    username is the username of the user sending the msg
    msg is the msh to be send (w/out the \n at the end)
    '''
    print 'You: {}'.format(msg)
    soc.send(msg+"\n")

def askName():
    '''
    asks for username to be used when establishing connection with other peer
    '''
    username = raw_input("Please enter your username: ")
    print 'Welcome {}!'.format(username)
    return username

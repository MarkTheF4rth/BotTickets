from Decorators.func import func

@func()
def ticket_view(self, ticket_type, server):
    """Print a formatted message to discord indicating tickets 
        of this type, and the kind of support it has received"""

    tickets = ticket_type.tickets

    header = ['**__A list of '+ticket_type.plural+'__**:']
    msg_break = '**Continued...**' # printed at the end of every message that does not end the list
    output = []
    lengths = [] # used to format the space used for the username field

    keylist = list(tickets.keys())
    keylist.sort() # sort tickets by index

    for index in keylist:
        values = tickets[index]
        user = server.get_member(values[0][0])
        if user:
            user = user.name
        else:
            user = str(user) # if a player has left the server, their information will be unobtainable
        lengths.append(len(user))
        output.append([user, index, values[1], len(values[0])])

    if output:
        max_length = max(lengths)
        final_message = []
        if ticket_type.votes:
            final_message = (header+['**`{0:<{length}}` *index:* `{1:<5}` (votes: `{3}`) {4}: ** {2}'
                    .format(*x, ticket_type.adjective, length=max_length) for x in output])
        else:
            final_message = (header+['**`{0:<{length}}` *index:* `{1:<5}` {3}: ** {2}'
                    .format(*x[0:-1], ticket_type.adjective, length=max_length) for x in output])

        return '\n'.join(final_message)


    else:
        return '**There are no tickets of this type at the moment**'


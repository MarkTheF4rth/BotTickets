from collections import OrderedDict
from func import func
import pickle

@func()
def buffer_compare(self, message):
    if message.author in self.buffer:
        if message.content == self.buffer[message.author]:
            return False
    self.buffer[message.author] = message.content
    return True

@func()
def ticket_edit(self, ticket_dict, content, message, index=-1, request=False):
    if not self.buffer_compare(message):
        return

    if not index+1:
        index = self.index
        self.index += 1

    ticket_dict[index] = (message.author.id, ' '.join(content))
    if request:
        self.votes[index] = [message.author.id]

    self.message_printer('Your ticket has been saved under index: '+str(index), message.channel)
    pickle.dump(self.index, open(self.data_dir+"index.p", "wb"))

@func()
def ticket_view(self, ticket_dict, ticket_type, ticket_adj, message, ctx, votes=False):
    header = ['**__A list of '+ticket_type+'__**:']
    msg_break = '**Continued...**'
    output = []
    lengths = []

    channel = message.author
    if len(ctx.message_content) == 1 and ctx.message_content[0] == 'pub':
        channel = message.channel

    keylist = list(ticket_dict.keys())
    keylist.sort()

    for index in keylist:
        values = ticket_dict[index]
        user = message.server.get_member(values[0])
        if user:
            user = user.name
        else:
            user = "unkown"
        lengths.append(len(user))
        output.append([user, index, values[1]])

    if output:
        max_length = max(lengths)
        final_message = []
        if votes:
            final_message = header+['**`{0:<{length}}` *index:* `{1:<5}` votes: `{4}` {3}: ** {2}'.format(*x, ticket_adj, len(self.votes[x[1]]), length=max_length) for x in output]
        else:
            final_message = header+['**`{0:<{length}}` *index:* `{1:<5}` {3}: ** {2}'.format(*x, ticket_adj, length=max_length) for x in output]

        self.message_printer('\n'.join(final_message), channel, msg_break=msg_break)

    else:
        self.message_printer('**There are no tickets of this type at the moment**', channel)

@func()
def ticket_del(self, ticket_dict, content, message, request=False):
    output = ['**__Damage Report:__**']

    for index in content:
        if not index.isdigit():
            output.append('Index **'+index+'** could not be deleted as it is not a number')

        elif int(index) not in ticket_dict.keys():
            output.append('Index **'+index+'** could not be deleted as it does not exist')

        else:
            if ticket_dict[int(index)][0] == message.author.id or 'UT Team' in [x.name for x in message.author.roles]:
                del(ticket_dict[int(index)])
                if request:
                    del(self.votes[int(index)])
                output.append('Index **'+index+'** has been deleted')
            else:
                output.append('Index **'+index+'** could not be deleted as it does not belong to you')

    self.message_printer('\n'.join(output), message.channel)

@func()
def ticket_clear(self, ticket_dict, message, ctx, request=False):
    header = '**__Damage Report:__**\n'
    output = []

    if ctx.message_content[0].lower() == 'all':
        if set(['admin', 'UT Team']) & set(ctx.accepted_roles) or message.author.id == '230038455982358528':
            ticket_dict = {}
            if request:
                self.votes = {}
            output.append('Everything has been deleted')

    else:
        replace_dict = {}
        for index, ticket in ticket_dict.items():
            if ticket[0] == message.author.id:
                if request:
                    del(self.votes[index])
                output.append('Index '+str(index)+' has been deleted')
            else:
                replace_dict.update({index:ticket})
        ticket_dict = replace_dict

    if output:
        self.message_printer(header+'\n'.join(output), message.channel)
    else:
        self.message_printer('**You have not made any tickets to delete**', message.channel)

    return ticket_dict

@func()
def validate_edit(self, content, message, ticket_dict):
    if len(content) <= 2 or not content[0].isdigit():
        return 'format'

    index = int(content[0])

    if index and not index in ticket_dict:
        self.message_printer('That ticket index does not exist', message.channel)
        return 'invalid'

    elif index and not ticket_dict[index][0] == message.author.id:
        self.message_printer('That ticket does not belong to you', message.channel)
        return 'invalid'

    return 'valid'

@func()
def vote_validate(self, content, message):
    output = {'baddigit':[], 'notpresent':[], 'alreadyvoted':[], 'notvoted':[]}
    for index in content:
        if not index.isdigit():
            output['baddigit'].append(index)
            continue

        index = int(index)
        if index not in self.requests:
            output['notpresent'].append(index)
            continue

        if message.author.id in self.votes[index]:
            output['alreadyvoted'].append(index)
            continue

        output['notvoted'].append(index)

    return output

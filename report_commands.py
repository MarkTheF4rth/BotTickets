from command import command
import pickle
import os

@command(description='reports bugs')
def report(self, message, ctx):
    self.ticket_edit(self.reports, ctx.message_content, message)
    pickle.dump(self.reports, open(self.data_dir+"reports.p", "wb"))

@command(description='requests features')
def request(self, message, ctx):
    self.ticket_edit(self.requests, ctx.message_content, message, request=True)
    pickle.dump(self.requests, open(self.data_dir+"requests.p", "wb"))
    pickle.dump(self.votes, open(self.data_dir+"votes.p", "wb"))

@command(description='view reported bugs')
def viewreports(self, message, ctx):
    self.ticket_view(self.reports, 'reports', 'reported', message, ctx)

@command(description='view requested features')
def viewrequests(self, message, ctx):
    self.ticket_view(self.requests, 'requests', 'requested', message, ctx, votes=True)



@command(aliases=['delreport'], description='deletes one ore multiple reports')
def delreport(self, message, ctx):
    self.ticket_del(self.reports, ctx.message_content, message)
    pickle.dump(self.reports, open(self.data_dir+"reports.p", "wb"))

@command(aliases=['delrequest'], description='deletes one ore multiple requests')
def delrequest(self, message, ctx):
    self.ticket_del(self.requests, ctx.message_content, message)
    pickle.dump(self.requests, open(self.data_dir+"requests.p", "wb"))



@command(description='deletes all reports you\'ve made')
def clearreports(self, message, ctx):
    self.reports = self.ticket_clear(self.reports, message, ctx)
    pickle.dump(self.reports, open(self.data_dir+"reports.p", "wb"))

@command(description='deletes all requests you\'ve made')
def clearrequests(self, message, ctx):
    self.requests = self.ticket_clear(self.requests, message, ctx)
    pickle.dump(self.requests, open(self.data_dir+"requests.p", "wb"))



@command(description='edits existing report')
def editreport(self, message, ctx):
    content = ctx.message_content

    out = self.validate_edit(content, message, self.reports)
    if out == 'valid':
        self.ticket_edit(self.reports, content, message, int(content[0]))
    elif out == 'format':
        self.message_printer('Please format your message as: `!editreport <index> <report>`, where index is a number', message.channel)

    pickle.dump(self.reports, open(self.data_dir+"reports.p", "wb"))

@command(description='edits existing request')
def editrequest(self, message, ctx):
    content = ctx.message_content

    out = self.validate_edit(content, message, self.requests)
    if out == 'valid':
        self.ticket_edit(self.requests, content, message, int(content[0]), request=True)
    elif out == 'format':
        self.message_printer('Please format your message as: `!editrequest <index> <request>`, where index is a number', message.channel)

    pickle.dump(self.requests, open(self.data_dir+"requests.p", "wb"))
    pickle.dump(self.votes, open(self.data_dir+"votes.p", "wb"))

@command(description='vote on one or multiple  current request')
def vote(self, message, ctx):
    final_output = ['**__Damage Report:__**']

    output = self.vote_validate(ctx.message_content, message)
    
    for index in output['notvoted']:
        self.votes[index].append(message.author.id)
        final_output.append('You have successfully voted for index `{}`'.format(index))

    for index in output['baddigit']:
        final_output.append('`{}` could not be voted for as its not numerical'.format(index))

    for index in output['notpresent']:
        final_output.append('ticket number `{}` does not exist'.format(index))

    for index in output['alreadyvoted']:
        final_output.append('you have already voted for ticket number `{}`'.format(index))

    self.message_printer('\n'.join(final_output), message.channel)
    pickle.dump(self.votes, open(self.data_dir+"votes.p", "wb"))


@command(description='remove your vote from one or multiple request')
def unvote(self, message, ctx):
    final_output = ['**__Damage Report:__**']
    
    output = self.vote_validate(ctx.message_content, message)

    for index in output['alreadyvoted']:
        self.votes[index].remove(message.author.id)
        final_output.append('You have successfully unvoted for index `{}`'.format(index))

    for index in output['baddigit']:
        final_output.append('`{}` could not be unvoted for as its not numerical'.format(index))

    for index in output['notpresent']:
        final_output.append('ticket number `{}` does not exist'.format(index))

    for index in output['notvoted']:
        final_output.append('you have not voted for ticket number `{}`'.format(index))

    self.message_printer('\n'.join(final_output), message.channel)
    pickle.dump(self.votes, open(self.data_dir+"votes.p", "wb"))

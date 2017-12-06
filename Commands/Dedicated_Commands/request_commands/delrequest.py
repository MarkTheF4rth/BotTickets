from Decorators.command import command

@command(usage=[('index', '...')], description='deletes a given report index')
def delrequest(self, message, ctx):
    """Dedicated command to delete report tickets"""

    output = self.ticket_del(self.tickets['request'], ctx.message_content, ctx.accepted_roles, message.author.id)

    self.message_printer(output, message.channel)

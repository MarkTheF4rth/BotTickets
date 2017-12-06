from Decorators.command import command

@command(usage=[('index', '...')], category='Tickets Commands', description='deletes a given report index')
def delreport(self, message, ctx):
    """Dedicated command to delete report tickets"""

    output = self.ticket_del(self.tickets['report'], ctx.message_content, ctx.accepted_roles, message.author.id)

    self.message_printer(output, message.channel)

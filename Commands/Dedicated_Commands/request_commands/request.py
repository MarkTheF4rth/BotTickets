from Decorators.command import command

@command(description='requests features')
def request(self, message, ctx):
    """Dedicated command for request ticket type"""

    output = self.ticket_edit(self.tickets['request'], message.author.id, ctx.message_content)

    self.message_printer(output, message.channel)

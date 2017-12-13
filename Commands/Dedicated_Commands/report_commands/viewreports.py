from Decorators.command import command

@command(description='view reported bugs')
def viewreports(self, message, ctx):
    """Dedicated command to print a list of report tickets"""
    channel = message.author

    if len(ctx.message_content) > 0 and ctx.message_content[0].lower() == 'pub':
        channel = message.channel

    output = self.ticket_view(self.tickets['report'], message.server)
    self.message_printer(output, channel)

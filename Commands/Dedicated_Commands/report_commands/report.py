from Decorators.command import command

@command(description='reports bugs')
def report(self, message, ctx):
    """Dedicated command for report ticket type"""

    output = self.ticket_edit(self.tickets['report'], message.author.id, ctx.message_content)

    self.message_printer(output, message.channel)

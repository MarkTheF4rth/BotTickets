from Decorators.command import command

@command(usage=[('index', '...')], description="removes your vote from a ticket")
def unvote(self, message, ctx):
    """Removes a user's vote from a given index if applicable"""
    self.message_printer(self.ticket_unvote(ctx.message_content, message.author.id, message.server), message.channel)

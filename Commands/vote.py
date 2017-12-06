from Decorators.command import command

@command(usage=[('index', '...')], description="allows you to place a vote on a ticket")
def vote(self, message, ctx):
    """Allows a user to vote on a given index"""
    self.message_printer(self.ticket_vote(ctx.message_content, message.author.id), message.channel)

from Decorators.command import command

@command(aliases=['ctt'], usage=[('ticket name', ''), ('votes', ''), ('plural', '?'), 
        ('adjective', '?'), ('variable author')], description='Creates a ticket type',
        category='TicketDefault')
def createtickets(self, message, ctx):
    '''Creates a ticket type based on given information'''
    
    pass 

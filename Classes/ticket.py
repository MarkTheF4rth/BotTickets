
class Ticket:
    """An object which carries all relevent information about tickets"""

    def __init__(self, name, adjective, plural, votes, var_auth, dedicated, tickets={}):
        self.name = name
        self.votes = votes # can this ticket be voted on

        self.adjective = adjective # used in printed messages
        self.plural = plural

        self.variable_author = var_auth # passes ownership of ticket over to first voter if applicable
        self.dedicated_commands = dedicated # there are commands dedicated towards this ticket type
        self.tickets = tickets

    def add_ticket(self, index, ticket, user):
        """Creates a ticket"""
        self.tickets[index] = ([user], ticket)

    def remove_ticket(self, index):
        """Removes a ticket index, assuming the user has permission to do so, 
            and that the ticket index exists"""
        del(self.tickets[index])

    def clear_tickets(self):
        """Clears all current tickets"""
        self.tickets = {}

    def add_vote(self, index, user_id):
        """Adds a vote to a given ticket index, assuming that the 
            index is correct and voting is available"""
        self.tickets[index][0].append(user_id)

    def remove_vote(self, index, user_id):
        """Removes a vote from the given ticket index, 
            assuming the user is eligible to do so"""
        self.tickets[index][0].remove(user_id)

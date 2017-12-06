from Decorators.func import func

@func()
def clear_reverse_ticket_ref(self, ticket_type):
    """Removes all instances of a given ticket type from the reverse 
        ticket reference dictionary"""

    new_backref = {}

    for index, tickets in self.reverse_ticket_ref.items():
        if tickets != ticket_type:
            new_backref[index] = tickets

    self.save_file("backref", self.reverse_ticket_ref)
    self.reverse_ticket_ref = new_backref

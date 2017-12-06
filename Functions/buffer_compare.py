from Decorators.func import func

@func()
def buffer_compare(self, user_id, content):
    """prevents duplicate inputs by comparing latest valid request from a 
        given user to a previous valid request from the same user

        this prevents spam and an occasional bug where discord
        sends a message twice for some reason"""

    if user_id in self.buffer:
        if content == self.buffer[user_id]:
            return False
    self.buffer[user_id] = content # updates buffer
    return True


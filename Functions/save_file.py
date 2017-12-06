from Decorators.func import func
import pickle

@func()
def save_file(self, data_name, data_set, ticket=False):
    """uses pickle to save the given data to a file"""

    if ticket: # ticket files are saved in Data/TicketBot/Tickets 
        file_path = self.ticket_data_dir+'Tickets/'

    else: # everything else is saved in Data/TicketBot
        file_path = self.ticket_data_dir

    full_file_path = file_path+data_name+self.ticket_file_suffix
    print(full_file_path, 'has been updated')
    pickle.dump(data_set, open(full_file_path, "wb"))

from Decorators.func import func
import pickle, os
from Classes.ticket import Ticket

@func()
def sync_ticket_data(self):
    """Reads cached ticket data from file, then creates a ticket object using 
        the combined information of ticket configs and ticket data"""

    self.tickets = {}

    if not os.path.isdir(self.data_dir+'/Ticket_Bot'):
        print('Ticket data dir not found, initialising...')
        self.ticket_data_init()

    else:
        self.index = pickle.load(open(self.data_dir+'Ticket_Bot/index'+self.ticket_file_suffix, 'rb'))
        self.reverse_ticket_ref = pickle.load(open(self.data_dir+'Ticket_Bot/backref'+self.ticket_file_suffix, 'rb'))

    
    pwd = self.ticket_data_dir+'Tickets/'

    for ticket_name, ticket_parameters in self.ticket_types.items():
        ordered_ticket_parameters = [ticket_name,
                ticket_parameters['adjective'],
                ticket_parameters['plural'],
                ticket_parameters['votes'],
                ticket_parameters['variable author'],
                ticket_parameters['dedicated commands']]

                
        file_path = pwd+ticket_name+self.ticket_file_suffix

        if os.path.isfile(file_path):
            print('"{}" cache file found, syncing...'.format(ticket_name))
            with open(file_path, 'rb') as ticket_file:
                ticket = pickle.load(ticket_file)
                self.tickets[ticket_name] = Ticket(*ordered_ticket_parameters, ticket)

        else: 
            print('"{}" cache file not found, instancing...'.format(ticket_name))
            self.tickets[ticket_name] = Ticket(*ordered_ticket_parameters)


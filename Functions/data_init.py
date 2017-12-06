from Decorators.func import func
import os, pickle

@func()
def ticket_data_init(self):
    os.makedirs(self.ticket_data_dir)
    os.makedirs(self.ticket_data_dir+'/Tickets')

    self.index = 0
    self.reverse_ticket_ref = {} # allows ticket index's to be traced to their source

    pickle.dump(self.index, open(self.data_dir+'Ticket_Bot/index'+self.ticket_file_suffix, 'wb'))
    pickle.dump(self.index, open(self.data_dir+'Ticket_Bot/backref'+self.ticket_file_suffix, 'wb'))

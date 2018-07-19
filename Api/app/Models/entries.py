class Entry():
    """
    This class will store diary entries
    and also have methods that will manipulate
    those entries.
    """
# This list stores all entries
    Entries = []
# This method fetches entry by its id
    def get_by_id(self,entryId):
        self.entry = next(filter(lambda x: x['id'] == entryId, self.Entries), None)
        return self.entry
# Appends an entry to the list
    def save(self,entry):
        self.Entries.append(entry)
# deletes an entry
    def delete_entry(self,entry):
        self.Entries.remove(entry)
# updates an entry if it exists with new data
    def update_entry(self,new_entry,id_):
        self.entry = next(filter(lambda x: x['id'] == id_, self.Entries), None)
        self.entry.update(new_entry)
# fetches all entries
    def all_items(self):
        return self.Entries
# returns an object as a string
    def __str__(self):
        return(str(self.Entries))
# returns the length of an object
    def __len__(self):
        return len(self.Entries)
# this method allows us to undex an object
    def __getitem__(self,i):
        return self.Entries[i]
# clears all data stored in Entries
    def clear_all(self):
        data = self.Entries
        del data[:]

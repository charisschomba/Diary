class Entry():
    """
    This class will store diary entries 
    and also have methods that will manipulate 
    those entries.
    """
    Entries = []
    
    def get_by_id(self,entryId):
        self.entry = next(filter(lambda x: x['id'] == entryId, self.Entries), None)
        return self.entry

    def save(self,entry):
        self.Entries.append(entry)

    def delete_entry(self,entry):
        self.Entries.remove(entry)

    def update_entry(self,new_entry,id):
        self.entry = next(filter(lambda x: x['id'] == id, self.Entries), None)
        self.entry.update(new_entry)

    def all_items(self):
        return self.Entries

    def __str__(self):
        return(str(self.Entries))

    def __len__(self):
        return len(self.Entries)

    def __getitem__(self,i):
        return self.Entries[i]



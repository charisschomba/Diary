class Entry():
    """
    This class will store diary entries
    and also have methods that will manipulate
    those entries.
    """
    Entries = []
    """This method fetches entry by its id"""
    @classmethod
    def get_by_id(cls,entryId):
        cls.entry = next(filter(lambda x: x['id'] == entryId, cls.Entries), None)
        return cls.entry

    def save(self,entry):
        """Appends an entry to the list"""
        self.Entries.append(entry)

    def delete_entry(self,entry):
        """deletes an entry"""
        self.Entries.remove(entry)

    def update_entry(self,new_entry,id_):
        """updates a comment if it exists with new data"""
        self.entry = next(filter(lambda x: x['id'] == id_, self.Entries), None)
        self.entry.update(new_entry)

    def all_items(self):
        """fetches all entries"""
        return self.Entries

    def __str__(self):
        """returns an object as a string"""
        return(str(self.Entries))

    def __len__(self):
        """returns the length of an object"""
        return len(self.Entries)

    def __getitem__(self,i):
        """this method allows us to undex an object"""
        return self.Entries[i]

    def clear_all(self):
        """clears all data stored in Entries"""
        data = self.Entries
        del data[:]

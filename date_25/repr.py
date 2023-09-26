class database:
    def __init__(self):
        self.data = []
    def refresh(self):
        print("Refresh")
    def add(self, data):
        self.data.append(data)
    def commit(self):
        print("Committing changes")
    def __repr__(self):
        self.refresh()
        self.add('divya')
        self.commit()
        return f"{self.data}"
obj = database()
print(obj)

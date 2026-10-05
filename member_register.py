class MemberRegistry:
    def __init__(self):
        # Initializes an empty dictionary to store member data
        self.members = {}

    def register(self, member_id, name, email):
        # Validates that the name is not empty or just whitespace
        if not name or not name.strip():
            raise ValueError("Name is required")
        
        # Validates basic email structure (must contain '@' and a domain part)
        if '@' not in email or not email.split('@')[1]:
            raise ValueError("Invalid email")
        
        # Validates that the member ID does not already exist
        if member_id in self.members:
            raise ValueError("Member ID already exists")
        
        # Stores member details using the member_id as the unique key
        self.members[member_id] = {
            "name": name,
            "email": email
        }
        return True

    def count(self):
        # Returns the total number of registered members
        return len(self.members)

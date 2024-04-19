class Ticket:
    counter = 1
    ticket_list = []
    ticket_stats = {
        "created": 0,
        "resolved": 0,
        "open": 0
    }

    def __init__(self, staff_id, creator_name, email, issue_description):
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.email = email
        self.issue_description = issue_description
        self.ticket_number = Ticket.counter + 2000
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.counter += 1
        Ticket.ticket_list.append(self)
        Ticket.ticket_stats["created"] += 1
        Ticket.ticket_stats["open"] += 1

    def respond_to_ticket(self, response):
        self.response = response
        if "Password change" in self.issue_description:
            new_password = self.staff_id[:2] + self.creator_name[:3]
            self.response = f"New password generated: {new_password}"
            self.status = "Closed"
            Ticket.ticket_stats["resolved"] += 1
            Ticket.ticket_stats["open"] -= 1

    def resolve_password_change_request(self):
        new_password = self.staff_id[:2] + self.creator_name[:3]
        self.response = f"New password generated: {new_password}"
        self.status = "Closed"
        Ticket.ticket_stats["resolved"] += 1
        Ticket.ticket_stats["open"] -= 1

    def reopen_ticket(self):
        if self.status == "Closed":
            self.status = "Reopened"
            Ticket.ticket_stats["resolved"] -= 1
            Ticket.ticket_stats["open"] += 1

    @staticmethod
    def display_all_tickets():
        for ticket in Ticket.ticket_list:
            print("\nTicket Number:", ticket.ticket_number)
            print("Ticket Creator:", ticket.creator_name)
            print("Staff ID:", ticket.staff_id)
            print("Email Address:", ticket.email)
            print("Description:", ticket.issue_description)
            print("Response:", ticket.response)
            print("Ticket Status:", ticket.status)

    @staticmethod
    def display_ticket_stats():
        print("\nDisplaying Ticket Statistics\n")
        print("Tickets Created:", Ticket.ticket_stats["created"])
        print("Tickets Resolved:", Ticket.ticket_stats["resolved"])
        print("Tickets To Solve:", Ticket.ticket_stats["open"])


# Sample Tickets
ticket1 = Ticket("JIMMYS", "Jimmy", "jimmy@whitecliffe.co.nz", "My monitor stopped working")
ticket2 = Ticket("MIKAP", "Mika", "mika@whitecliffe.co.nz", "Request for a videocamera to conduct webinars")
ticket3 = Ticket("SCOTTR", "Scott", "scott@whitecliffe.co.nz", "Password change")

ticket3.resolve_password_change_request()

Ticket.display_ticket_stats()
Ticket.display_all_tickets()

ticket1.respond_to_ticket("The monitor has been replaced")
ticket2.respond_to_ticket("Will provide the camera soon")

Ticket.display_ticket_stats()
Ticket.display_all_tickets()

ticket2.reopen_ticket()

Ticket.display_ticket_stats()
Ticket.display_all_tickets()

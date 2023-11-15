class Waypoint:
    def __init__(self, location, description):
        self.location = location
        self.description = description
        self.next_waypoint = None
        self.prev_waypoint = None
    
    def set_next_waypoint(self, next_waypoint):
        self.next_waypoint = next_waypoint
    
    def set_prev_waypoint(self, prev_waypoint):
        self.prev_waypoint = prev_waypoint

class Route:
    def __init__(self):
        self.head = None

    def add_waypoint(self, location, description):
        waypoint = Waypoint(location, description)
    
        if not self.head:
            self.head = waypoint
            self.tail = waypoint
        
        else:
            current = self.head
            while current.next_waypoint:
                current = current.next_waypoint
            current.set_next_waypoint(waypoint)

    def insert_waypoint_after(self, target, location, description):
        waypoint = Waypoint(location, description)
        current = self.head
        while current:
            if current.location == target:
                waypoint.next_waypoint = current.next_waypoint
                current.next_waypoint = waypoint    
                if waypoint.next_waypoint:
                    waypoint.next_waypoint.prev_waypoint = waypoint
                waypoint.prev_waypoint = current
                break
            current = current.next_waypoint

    def remove_waypoint(self, location):
        current = self.head
        if current and current.location == location:
            self.head = current.next_waypoint
            if self.head:
                self.head.prev_waypoint = None
            return
        while current:
            if current.location == location:
                if current.next_waypoint:
                    current.next_waypoint.prev_waypoint = current.prev_waypoint
                if current.prev_waypoint:
                    current.prev_waypoint.next_waypoint = current.next_waypoint
                break
            current = current.next_waypoint

    

class BidirectionalRoute(Route):
    def traverse_forward(self):
        current = self.head
        while current:
            print(f"Your current Location is: {current.location}, Description: {current.description}")
            current = current.next_waypoint
            
    def traverse_backward(self):
        current = self.head
        while current and current.next_waypoint:
            current = current.next_waypoint
        while current:
            print(f"Your current Location is: {current.location}, Description: {current.description}")
            current = current.prev_waypoint

    

if __name__ == '__main__':
    route = BidirectionalRoute()
    
    while True:
        print("\nMenu:")
        print("0. ADD A WAYPOINT")
        print("1. INSERT A WAYPOINT AFTER")
        print("2. REMOVE A WAYPOINT")
        print("3. FORWARD TRAVERSAL")
        print("4. BACKWARD TRAVERSAL")
        print("5. END")

        choice = input("Enter your choice: ")

        if choice == "0":
            location = input("Enter location: ")
            description = input("Enter description: ")
            route.add_waypoint(location, description)
        elif choice == "1":
            target = input("Enter the location after which to insert: ")
            location = input("Enter new location: ")
            description = input("Enter new description: ")
            route.insert_waypoint_after(target, location, description)
        elif choice == "2":
            location = input("Enter the location to remove: ")
            route.remove_waypoint(location)
        elif choice == "3":
            print("\nForward Traversal:")
            route.traverse_forward()
        elif choice == "4":
            print("\nBackward Traversal:")
            route.traverse_backward()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

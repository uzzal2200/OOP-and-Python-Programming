from datetime import date
class Star_Cinema:
    __hall_list=[]
    __hall_no=[]
    @classmethod
    def entry_hall(cls,hall,hall_no):
        cls.__hall_list.append(hall)
        cls.__hall_no.append(hall_no)
    def view(self,h_no):
        view_hall=dict(zip(self.__hall_no,self.__hall_list))
        for key,value in view_hall.items():
            if h_no==key:
                hall_name=value
                print(" ___________________________")
                print("|                           |")
                print(f"|     {key}.{hall_name}       |")
                print("|___________________________|")
        print()
    def Add_list(self):
        hall=dict(zip(self.__hall_no,self.__hall_list))
        for key,val in hall.items():
            print(f"{key}.{hall[key]}",end=" | ")
        print()
class Hall(Star_Cinema):
    def __init__(self,name,row,col,hall_no):
        self._hall_name=name
        self.__rows=row
        self.__Column=col
        self._hall_No=hall_no
        self.__seats={}
        self.__show_list=[]
        Star_Cinema.entry_hall(self._hall_name,self._hall_No)
    def entry_show(self,name,id,time):
        show=(name,id,self._hall_name,time)
        self.__show_list.append(show)
        Key_value=[]
        for seat_row in range(self.__rows):
            Key_value.append([])
            for seat_col in range(self.__Column):
                set_seat=0
                Key_value[seat_row].append(set_seat)
        self.__seats[id]=Key_value
    def book_seats(self,id,seats_list):
        for book_seat in seats_list:
            row,col=book_seat
            if 0<=row<self.__rows and 0<=col<self.__Column:
                if self.__seats[id][row][col]==0:
                    self.__seats[id][row][col]=1
                    print("\nSeats booked successfully.\n")
                else:
                    print(f"This ({row},{col}) Seat already booked!!")
            else:
                print("Sorry!! Invalid Seats.\n")
    def View_Show_list(self):
        for show in self.__show_list:
            print(show[0],f"({show[1]})",f"    {date.today()}",f"   {show[3]}")
    def view_available_seats(self,id):
        show_found=False
        for show in self.__show_list:
            if show[1]==id:
                print(f"Available Seats for Movie name:{show[0]}({show[1]})")
                show_found=True
        if not show_found:
                print("Invalid Movie ID. Please enter a correct Movie ID!!!")
                return
        for i in range(1,self.__rows+1):
            for j in range(1,self.__Column+1):
                print(f"    Seats{i,j}")
        print(f"\nUpdate Seats for {self.__show_list[0][2]}\n")
        for key,val in self.__seats.items():
            for value in val:
                print(f"    {value}")   

hall1=Hall("Star Cineplex",5,5,1)
hall2=Hall("BLOCKBUSTERS",4,4,2)
hall3=Hall("Bashundhara City",4,4,3)
hall1.entry_show("12th Fail",111,"10:00 AM")
hall1.entry_show("Dream Scenario",222,"12:00 PM")
hall1.entry_show("Kho gaye hum kahan",333,"3:30 PM")
hall2.entry_show("Toby",121,"11:30 AM")
hall2.entry_show("Saltburn",212,"3:00 PM")
hall2.entry_show("12th Fail",313,"7:00 PM")
hall3.entry_show("Hidhimbha",311,"10:30 AM")
hall3.entry_show("12th Fail",211,"12:30 PM")
hall3.entry_show("Toby",100,"4:00 PM")

while True:
        
    print("1. View All Show Today")
    print("2. View Available Seats")
    print("3. Book Ticket")
    print("4. Exit\n")
    opt=int(input("Choose Your Option:"))
    print("\n")
    if opt==1:
        hall1.Add_list()
        print("\n")
        op=int(input("Please Choose Cinnema Hall No:"))
        print("\n")
        if op<=3:
            if op==1:
                hall1.view(op)
                print("\n")
                hall1.View_Show_list()
                print("\n")
            elif op==2:
                hall2.view(op)
                print("\n")
                hall2.View_Show_list()
                print("\n")
            elif op==3:
                hall3.view(op)
                print("\n")
                hall3.View_Show_list()
                print("\n")
        else:
            print("\nThere is No more Cinnema Hall!!\n")
    elif opt==2:
        hall1.Add_list()
        hall_no=int(input("\nChoose Your Hall No:"))
        if hall_no<=3:
            if hall_no==1:
                hall1.view(hall_no)
                print("\nFor this Hall Available Movie!!\n")
                hall1.View_Show_list()
                print("\n")
                User_id=int(input("\nPlease Input Movie Id no:"))
                print("\n")
                hall1.view_available_seats(User_id)
                print("\n")
            elif hall_no==2:
                hall2.view(hall_no)
                print("\nFor this Hall Available Movie!!\n")
                hall2.View_Show_list()
                print("\n")
                User_id=int(input("\nPlease Input Movie Id no:"))
                print("\n")
                hall2.view_available_seats(User_id)
                print("\n")
            elif hall_no==3:
                hall3.view(hall_no)
                print("\nFor this Hall Available Movie!!\n")
                hall3.View_Show_list()
                print("\n")
                User_id=int(input("\nPlease Input Movie Id no:"))
                print("\n")
                hall3.view_available_seats(User_id)
                print("\n")
        else:
            print("\nThere is No more Cinnema Hall!!\n")
    elif opt==3:
        hall1.Add_list()
        h_no=int(input("\nChoose Your Hall No:"))
        if h_no<=3:
            if h_no==1:
                hall1.view(h_no)
                print("\nFor this Hall Available Movie!!\n")
                hall1.View_Show_list()
                print("\n")
                User=int(input("\nPlease Input Movie Id no:"))
                ticket_no=int(input("Number of Ticket:"))
                seat_list=[]
                for tick in range(ticket_no):
                    Row=int(input("Enter seat Row:"))
                    Col=int(input("Enter Seat Column:"))
                    seat=(Row,Col)
                    seat_list.append(seat)
                hall1.book_seats(User,seat_list)
            elif h_no==2:
                hall2.view(h_no)
                print("\nFor this Hall Available Movie!!\n")
                hall2.View_Show_list()
                print("\n")
                User=int(input("\nPlease Input Movie Id no:"))
                ticket_no=int(input("Number of Ticket:"))
                seat_list=[]
                for tick in range(ticket_no):
                    Row=int(input("Enter seat Row:"))
                    Col=int(input("Enter Seat Column:"))
                    seat=(Row,Col)
                    seat_list.append(seat)
                hall2.book_seats(User,seat_list)
            elif h_no==3:
                hall3.view(h_no)
                print("\nFor this Hall Available Movie!!\n")
                hall3.View_Show_list()
                print("\n")
                User=int(input("\nPlease Input Movie Id no:"))
                ticket_no=int(input("Number of Ticket:"))
                seat_list=[]
                for tick in range(ticket_no):
                    Row=int(input("Enter seat Row:"))
                    Col=int(input("Enter Seat Column:"))
                    seat=(Row,Col)
                    seat_list.append(seat)
                hall3.book_seats(User,seat_list)
    elif opt==4:
        print("Thanks for visiting!!")
        break

import os
import sys
from restaurant import *
from user import *
from admin import *
from customer import *
from feedback import *
from item import *
from menu import *
from order import *
from owner import *

#Path to save the code
path = "C:/125"

#MonasEats class where the set and get functions are run.
class MonashEats():

    #declating the txt files where the data will be stored
    
    __filename_customer = 'customer.txt'
    __filename_owner= 'owner.txt'
    __filename_purchase_history ='purchase_history.txt'
    __filename_restaurant = 'restaurant.txt'
    __filename_menu = 'menu.txt'

    def __init__(self): #function (init) to initiate the storage of data
        self.fullPath_customer = os.path.join(path, self.__filename_customer)
        if not os.path.exists(self.fullPath_customer):
            open(self.fullPath_customer, 'w').close()

        self.fullPath_owner = os.path.join(path, self.__filename_owner)
        if not os.path.exists(self.fullPath_owner):
            open(self.fullPath_owner, 'w').close()

        self.fullPath_purchase_history = os.path.join(path, self.__filename_purchase_history)
        if not os.path.exists(self.fullPath_purchase_history):
            open(self.fullPath_purchase_history, 'w').close()

        self.fullPath_restaurant = os.path.join(path, self.__filename_restaurant)
        if not os.path.exists(self.fullPath_restaurant):
            open(self.fullPath_restaurant, 'w').close()

        self.fullPath_menu = os.path.join(path, self.__filename_menu)
        if not os.path.exists(self.fullPath_menu):
            open(self.fullPath_menu, 'w').close()


    def search_restaurant(self): #dunction to search restaurants
        try:
            question = int(input("1. Search restaurant by category\n"
                             "2. Search restaurant by suburb\n"
                             "3. Back to customer menu\n"
                             "0. Exit\n"
                             ""
                             "Type number of your choice: "))
            if question == 1:
                result_from_category = self.search_restaurant_by_category()
                return result_from_category
                #print(result)
            elif question == 2:
                result_from_suburb = self.search_restaurant_by_suburb()
                return result_from_suburb
                #print(result)
            elif question == 3:
                self.customer_menu()
            elif question == 0:
                sys.exit(0)
            else:
                print("Invalid option. Try again")
                self.search_restaurant()

        except Exception as e: #handling exception
            print("Something gets wrong. Try to search again.")
            self.search_restaurant()

    def register_owner_restaurant(self): #dunction to register owner of a restaurant
        try:
            # self.remove_last_empty_line()
            user = {"first_name": "",
                    "last_name": "",
                    "email": "",
                    "home_address": "",
                    "suburb": "",
                    "postcode": "",
                    "phone_number": "",
                    "password": ""}

            while True:
                first_name = input("Enter your first name: ")
                if self.check_empty(first_name) != False:
                    user["first_name"] = first_name
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                last_name = input("Enter your last name: ")
                if self.check_empty(last_name) != False:
                    user["last_name"] = last_name
                    break
                else:
                    print("Empty input.Please, enter details.")


            while True:
                email = input("Enter your email address: ").lower()
                if self.checkemail_owner(email) != True and self.check_empty(email) != False:
                    user["email"] = email
                    break
                elif self.checkemail_owner(email) == True:
                    print("Your email is already used. Try to login.")
                    MonashEats().login_options()
                else:
                    print("Empty input.Please, enter details.")

            while True:
                home_address = input("Enter your home address: ")
                if self.check_empty(home_address) != False:
                    user["home_address"] = home_address
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                suburb = input("Enter your suburb: ")
                if self.check_empty(suburb) != False:
                    user["suburb"] = suburb
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                postcode = int(input("Enter your postcode: "))
                if self.check_empty(postcode) != False:
                    user["postcode"] = postcode
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                phone_number = int(input("Enter your phone number: "))  # 0452050008
                if self.check_empty(phone_number) != False:
                    user["phone_number"] = phone_number
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                password = input("Enter your password: ")
                if self.check_empty(password) != False:
                    user["password"] = password
                    break
                else:
                    print("Empty input.Please, enter details.")

            print("You have been successfully registered.")
            self.__write_to_file_owner(user)
            return user


        except Exception as e: #exception for invalid input
            print("Error : ", e)
            self.register_owner_restaurant()

    def register_customer(self): #Function to register a customer
        try:
            user = {"first_name": "",
                    "last_name": "",
                    "email": "",
                    "home_address": "",
                    "suburb": "",
                    "postcode": "",
                    "phone_number": "",
                    "customer_type": "",
                    "payment_type": "",
                    "password": ""}
            while True:
                first_name = input("Enter your first name: ")
                if self.check_empty(first_name) != False:
                    user["first_name"] = first_name
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                last_name = input("Enter your last name: ")
                if self.check_empty(last_name) != False:
                    user["last_name"] = last_name
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                email = input("Enter your email address: ").lower()
                if self.check_empty(email) != False and self.checkemail_customer(email) != True:
                    user["email"] = email
                    break
                elif self.checkemail_customer(email) == True:
                    print("Your email is already used. Try to login.")
                    MonashEats().login_options()
                else:
                    print("Empty input.Please, enter details.")
            while True:
                home_address = input("Enter your home address: ")
                if self.check_empty(home_address) != False:
                    user["home_address"] = home_address
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                suburb = input("Enter your suburb: ")
                if self.check_empty(suburb) != False:
                    user["suburb"] = suburb
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                postcode = int(input("Enter your postcode: "))
                if self.check_empty(postcode) != False:
                    user["postcode"] = postcode
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                phone_number = int(input("Enter your phone number: "))  # 0452050008
                if self.check_empty(phone_number) != False:
                    user["phone_number"] = phone_number
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                question = int(input("If you are a student then type - 1, otherwise type - 2: "))
                if question == 1:
                    user["customer_type"] = int(1)
                    break
                elif question == 2:
                    user["customer_type"] = int(2)
                    break
                else:
                    print("Invalid choice.Please try again")
            while True:
                question = int(input("Type - 1 to pay by cash, otherwise type - 2 to pay by card: "))
                if question == 1:
                    user["payment_type"] = int(1)
                    break
                elif question == 2:
                    user["payment_type"] = int(2)
                    break
                else:
                    print("Invalid choice.Please try again")
            while True:
                password = input("Enter your password: ")
                if self.check_empty(password) != False:
                    user["password"] = password
                    break
                else:
                    print("Empty input.Please, enter details.")

            print("You have been successfully registered.")
            self.__write_to_file_customer(user)
            return user

        except Exception as e: #exception for invalid input
            print("Error : ", e)
            self.register_customer()

    def check_empty(self,input_string): #function to check empty input
        if input_string == "":
            return False

    def __remove_last_empty_line(self):
        with open(self.fullPath_customer,'r') as f:
            content = f.read().rstrip("\n")
            with open(self.fullPath_customer,'w') as new:
                new.write(content)

    def __write_to_file_owner(self,data): #Function to write the file to owner.txt
        f = open(self.fullPath_owner,'a+')
        for key,value in data.items():
            f.write('%s:%s\n' %(key,value))
        f.close()

    def __write_to_file_customer(self,data): #Function to write the file to customer.txt
        f = open(self.fullPath_customer,'a+')
        for key,value in data.items():
            f.write('%s:%s\n' %(key,value))
        f.close()

    def checkemail_owner(self,email): #function to check the mail of owner
        f = open(self.fullPath_owner)
        text = f.readlines()
        f.close()
        list_values=[]
        for line in text:
            line = line.strip()
            key, value = line.split(':')
            list_values.append(key + ":" + value)
      
        count = 0
        for item in list_values:
            for value in item:
                if value == ":":
                    index_of_item=item.index(value)
                    first_part = item[:index_of_item]
                    second_part = item[index_of_item+1:]
                    if first_part == "email" and second_part == email:
                        count += 1
        if count != 1:
            return False
        elif count == 1:
            return True

    def checkemail_customer(self,email): #Function to check the email of the customer
        f = open(self.fullPath_customer)
        text = f.readlines()
        f.close()
        list_values=[]
        for line in text:
            line = line.strip()
            key, value = line.split(':')
            list_values.append(key + ":" + value)
        count = 0
        for item in list_values:
            for value in item:
                if value == ":":
                    index_of_item=item.index(value)
                    first_part = item[:index_of_item]
                    second_part = item[index_of_item+1:]
                    if first_part == "email" and second_part == email:
                        count += 1
        if count != 1:
            return False
        elif count == 1:
            return True

    def login_owner_restaurant(self): #function for owner login
        email = input("Enter your email address: ").lower()
        password = input("Enter your password: ")
        f = open(self.fullPath_owner)
        text = f.readlines()
        f.close()
        list_values = []
        for line in text:
            key,value = line.strip().split(':')
            list_values.append(key + ":" + value)
        count = 0
        for item in list_values:
            for value in item:
                if value == ":":
                    index_of_item=item.index(value)
                    first_part = item[:index_of_item]
                    second_part=item[index_of_item+1:]
                    if first_part == "email" and second_part == email:
                        count +=1
                    elif first_part =="password" and second_part == password:
                        count+=1
                    else:
                        continue
        if count == 2:
            print("Login successfully")
            return True
        else:
            print ("Login failed. Try again")
            return False

    def login_customer(self): #login functon for the customer to login
        email = input("Enter your email address: ").lower()
        password = input("Enter your password: ")
        f = open(self.fullPath_customer)
        text = f.readlines()
        f.close()
        list_values = []
        for line in text:
            key,value = line.strip().split(':')
            list_values.append(key + ":" + value)
        count = 0
        for item in list_values:
            for value in item:
                if value == ":":
                    index_of_item=item.index(value)
                    first_part = item[:index_of_item]
                    second_part=item[index_of_item+1:]
                    if first_part == "email" and second_part == email:
                        count +=1
                    elif first_part =="password" and second_part == password:
                        count+=1
                    else:
                        continue
        if count == 2:
            print("Login successfully")
            return True
        else:
            print ("Login failed. Try again")
            return False

    def login_options(self): #Function to display the login Menu
        print("Login options")
        try:
            question = int(input("1. Login as customer\n"
                             "2. Login as owner\n"
                            "3. Back to home page\n"
                             "0. Exit\n"
                             ""
                             "Type number of your choice: "))
            if question == 1:
                if self.login_customer() == True:
                    self.customer_menu()
                else:
                    self.login_options()
            elif question == 2:
                if self.login_owner_restaurant() == True:
                    self.owner_menu()
                else:
                    self.login_options()
            elif question == 3:
                main()
            elif question == 0:
                sys.exit(0)
            else:
                print("Invalid option. Try again")
                self.login_options()

        except Exception as e: #Function to handle exception for invalid input
            print("Something gets wrong. Try again.")
            self.login_options()

    def register_options(self): #Function to Register Menu
        print("Register options")
        try:
            question = int(input("1. Register customer\n"
                                "2. Register owner of a restaurant\n"
                                "3. Back to home page\n"
                                "0. Exit\n"
                                "Type number of your choice: "))
            if question == 1:
                self.register_customer()
                main()
                    # print(result)
            elif question == 2:
                self.register_owner_restaurant()
                main()
                # print(result)
            elif question == 3:
                main()
            elif question == 0:
                sys.exit(0)
            else:
                print("Invalid option. Try again")
                self.register_options()

        except Exception as e:
            print("Something gets wrong. Try again.")
            self.register_options()

    def customer_menu(self):
        print("Customer menu: \n"
              "1. Search restaurant\n"
              "2. Manage profile\n"
              "3. Purchase history\n"
              "4. Back to home page\n"
              "0. Exit")
        try:
            question = int(input("Type number of your choice: "))
            if question == 1:
                #restaurant= Restaurant()
                restaurant_name = self.search_restaurant()
                #print(restaurant_name)
                if restaurant_name is not None:
                    self.chosen_restaurant(restaurant_name)
                else:
                    self.customer_menu()
            elif question == 2:
                self.manage_profile()
                # call menu of manage profile
            elif question == 3:
                self.purchase_history()
                self.customer_menu()
            elif question == 4:
                main()
            elif question == 0:
                print("Good bye. Hopefully, will see you again!")
                sys.exit(0)
            else: #exception for invalid input
                print("Invaid option. Try again.")
                self.customer_menu()

        except Exception as e:  #Function to handle exception for invalid input
            print("Something gets wrong. Try again.")
            self.customer_menu()

    def owner_menu(self): #Function for owner menu.
        print("Owner menu\n"
              "1. Register restaurant\n"
              "2. Register menu\n"
              "3. Manage order\n"
              "0. Back to home page")
        try:
            while True:
                question = int(input("Type number of your choice: " ))
                if question == 1:
                    self.register_restaurant()
                    self.owner_menu()
                    break
                elif question == 2:
                    self.register_menu()
                    self.owner_menu()
                    break
                elif question == 3:
                    self.manage_order()
                    break
                elif question == 0:
                    main()
                    break
                else:
                    print("Invaid option. Try again.")
        except Exception as e:  #Function to handle exception for invalid input
            print("Something gets wrong. Try again.")
            self.owner_menu()

    def manage_order(self): #Function for manage order menu
        print("Manage order: \n"
              "1. Send receipt to customer\n"
              "2. Cancel order\n"
              "3. Back to owner menu")
        try:
            while True:
                question = int(input("Type number of your choice: "))
                if question == 1:
                    self.receipt_to_email()
                    self.manage_order()
                    break
                elif question == 2:
                    self.manage_order()
                    break
                elif question == 3:
                    self.owner_menu()
                    break
                else: #exception for invalid input
                    print("Invalid option. Try again.")

        except Exception as e:  #Function to handle exception for invalid input
            print("Something gets wrong. Try again.")
            self.owner_menu()

    def manage_profile(self): #Function for manage profile
        print("Manage profile: \n"
              "1. Change password\n"
              "2. Back to customer menu")
        try:
            question = int(input("Type number of your choice: "))
            if question == 1:
                self.change_password()
                self.manage_profile()
            elif question == 2:
                self.customer_menu()
            else:
                print("Invalid option. Try again.")
                self.customer_menu()
        except Exception as e:  #Function to handle exception for invalid input
            #print("Error : ",e)
            print("Something gets wrong. Try again.")
            self.customer_menu()

    def write_purchase_information(self,purchase_informaton): #Function to write the order purchase informate to the file
        f = open(self.fullPath_purchase_history, 'a+')
        for item in purchase_informaton:
            f.write(item+"\n")
        f.close()

    def change_password(self): #Fucntion for changing the password
        try:
            email = input("Enter your email address: ")
            password = input("Enter your current password: ")
            f = open(self.fullPath_customer,"r+")
            text = f.readlines()
            f.close()
            list_values = []
            for line in text:
                key, value = line.strip().split(':')
                list_values.append(key + ":" + value)
            count = 0
            for item in list_values:
                for value in item:
                    if value == ":":
                        index_of_item = item.index(value)
                        first_part = item[:index_of_item]
                        second_part = item[index_of_item + 1:]
                        if first_part == "email" and second_part == email:
                            count += 1
                        elif count ==1 and first_part == "password" and second_part == password:
                            count += 1
                        else:
                            continue
            if count !=2:
                print("The email address or password you entered is not valid. Please, try again")
            elif count == 2:
                while True:
                    new_password = input("Enter your new password: ")
                    if self.check_empty(new_password) != False:
                        pass
                        break
                    else:
                        print("Empty input.Please, enter details.")

                confirm_password = input("Confirm your new password: ")
                if new_password != confirm_password:
                    print("The new password and confirmation password do not match. Please, try again.")
                elif new_password == confirm_password:
                    question = input("Do you confirm to change your password? Type \"y\" to confirm or \"n\" to cancel: ").lower()
                    if question == "n":
                        print("Your password has not been modified")
                        return False
                    elif question == "y":
                        with open(self.fullPath_customer,"r+") as file:
                            state=0
                            combine_word_one = "email:"+email
                            combine_word_two = "password:"+password
                            new_list=[]
                            for item in list_values:
                                if item == combine_word_one:
                                    state+=1
                                elif state == 1 and item == combine_word_two:
                                        new_word = "password:"+new_password
                                        index_of_password = list_values.index(item)
                                        list_values[index_of_password] = new_word
                                        for item in list_values:
                                            file.write(item + "\n")

                                        file.close()
                                        print("Your password has been modified successfully")
                                        return True

            self.__remove_last_empty_line()

        except Exception as e:  #Function to handle exception for invalid input
            print("Something gets wrong. Try again.")
            self.customer_menu()

    def make_order(self,total_price,purchase_information): #Function to make order.
        print("Total price of your order is:", int(total_price))
        try:
            while True:
                question = input("We give half price of order for students."
                    "If you are a student, type Y, otherwise type N: ").lower()
                if question == 'y':
                    total_price = float(total_price/2)
                    print("Total price for you is:", total_price)
                    break
                elif question == 'n':
                    pass
                    break
                else:
                    print("Invalid answer. Try again")
            while True:
                second_question = input("If you have a coupon, type Y, otherwise type N: ")
                if second_question == "y":
                    sale = 5
                    total_price = float(total_price - sale)
                    break
                elif second_question == "n":
                    pass
                    break
                else:
                    print("Invalid answer. Try again")
            print("Total price of your order is:",total_price)
            while True:
                third_question = int(input("Type 1 to make payment or type 0 to go back to customer menu: "))
                if third_question == 1:
                    self.make_payment(purchase_information)
                    break
                elif third_question == 0:
                    self.customer_menu()
                    break
                else:
                    print("Invalid choice. Try again")
        except Exception as e:  #Function to handle exception for invalid input
            #print("Error : ",e)
            print("Something gets wrong. Try again.")
            self.customer_menu()


    def make_payment(self, purchase_information): #Function to initiate payment method
        print("Make payment options\n"
              "1. Credit card\n"
              "2. Cash\n"
              "0. Customer menu")
        try:
            while True:
                question = int(input("Type number of your choice: "))
                if question == 1:
                    if self.credit_card_payment() == True:
                        print("Your order has been accepted. Thank you!")
                        self.write_purchase_information(purchase_information)
                        self.customer_menu()
                        # CAll owner to send email reciept to customer
                    else:
                        print("Unfortunaltely, your order has not been accepted. Try again later.")
                        self.customer_menu()
                    break
                elif question == 2:
                    print("Your order has been accepted. Thank you!")
                    self.write_purchase_information(purchase_information)
                    self.customer_menu()
                    break
                elif question == 0:
                    self.customer_menu()
                    break
                else:
                    print("Invalid choice. Try again.")
        except Exception as e:  #Function to handle exception for invalid input
            # print("Error : ",e)
            print("Something gets wrong. Try again.")
            self.customer_menu()

    def credit_card_payment(self, ): #function for credit card payment menu
        print("Credit card payment\n"
                  "Please, enter credit card details below: \n"
                  "Full name: \n"
                  "Card number : \n"
                  "CVV: ")
        try:
            while True:
                question = int(input("Type 1 to confirm credit card details or type 0 to cancel: "))
                if question == 1:
                    return True
                elif question == 0:
                    return False
                else:
                    print("Invalid choice. Try again.")
        except Exception as e:
            # print("Error : ",e)
            print("Something gets wrong. Try again.")
            self.customer_menu()

    def purchase_history(self): #Function to read purchase history
        f = open(self.fullPath_purchase_history, 'r')
        text = f.readlines()
        f.close()
        list_values = []
        for line in text:
            key, value = line.strip().split(':')
            list_values.append(key + ":" + value)
        #print(list_values)
        email_used = input("Type email that you used to order food: ")
        history = []
        email_indexes = []
        email_list=[]
        for item in list_values:
            for i in range(len(item)):
                if item[i] == ":":
                    #index_of_item = item.index(i)
                    first_part = item[:i]
                    second_part = item[i:]
                    if first_part == "email":
                        email_list.append(item)
        for item in range(len(list_values)):
            for i in email_list:
                if list_values[item]==i and item not in email_indexes:
                    email_indexes.append(item)
        key_word = 'email:' + str(email_used)

        for num in email_indexes:
            for item in range(len(list_values)):
                if num == item and len(history)==0:
                    history.append(list_values[:num+1])
                    last_position = num
                elif num == item and len(history)!=0:
                    history.append(list_values[last_position+1:num+1])
                    last_position = num
        position = []
        for item in range(len(history)):
            for i in history[item]:
                if key_word == i:
                    position.append(item)
        customer_information = []
        for i in range(len(history)):
           if i in position:
               customer_information.append(history[i])
        for item in customer_information:
            del item[-1]

        if len(customer_information) == 0:
            print("Your purchase history is empty")
        else:
            for item in customer_information:
                print(item)

    def __write_to_file_restaurant(self, data): #Function to write the restaurant data to text
        f = open(self.fullPath_restaurant, 'a+')
        for key, value in data.items():
            f.write('%s:%s\n' % (key, value))
        f.close()

    def check_id_restaurant(self, rest_id):#Function to check the restaurant ID to avoide repeatance.
        f = open(self.fullPath_restaurant)
        text = f.readlines()
        f.close()
        list_values = []
        for line in text:
            line = line.strip()
            key, value = line.split(':')
            list_values.append(key + ":" + value)
        count = 0
        for item in list_values:
            for value in item:
                if value == ":":
                    index_of_item = item.index(value)
                    first_part = item[:index_of_item]
                    second_part = item[index_of_item + 1:]
                    if first_part == "rest_id" and int(second_part) == int(rest_id):
                        count += 1

        if count != 1:
            return False
        elif count == 1:
            return True

    def register_restaurant(self): #Function to register restaurant data
        try:
            restaurant = {"rest_id": "",
                          "name": "",
                          "category": "",
                          "phone_number": "",
                          "address": "",
                          "suburb": "",
                          "postcode": ""}

            while True:
                rest_id = int(input("Enter id of restaurant: "))
                if self.check_id_restaurant(rest_id) == False:
                    restaurant['rest_id'] = rest_id
                    break
                else:
                    print("Id already exists.Try another id.")
            while True:
                name = input("Enter restaurant name: ")
                if self.check_empty(name) != False:
                    restaurant["name"] = name
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                category = input("Enter category: ").lower()
                if self.check_empty(category) != False:
                    restaurant["category"] = category
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                phone_number = int(input("Enter phone number: "))
                if self.check_empty(phone_number) != False:
                    restaurant["phone_number"] = phone_number
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                address = input("Enter restaurant address: ")
                if self.check_empty(address) != False:
                    restaurant["address"] = address
                    break
                else:
                    print("Empty input.Please, enter details.")

            while True:
                suburb = input("Enter suburb: ")
                if self.check_empty(suburb) != False:
                    restaurant["suburb"] = suburb
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                postcode = int(input("Enter postcode: "))
                if self.check_empty(postcode) != False:
                    restaurant["postcode"] = postcode
                    break
                else:
                    print("Empty input.Please, enter details.")

            print("Your restaurant have been successfully registered.")
            self.__write_to_file_restaurant(restaurant)
            return restaurant

        except Exception as e:  #Function to handle exception for invalid input
            print("Something went wrong. Try again.")
            self.register_restaurant()

    def receipt_to_email(self): #Function to print the receipt.
        try:
            f = open(self.fullPath_purchase_history, 'r')
            text = f.readlines()
            f.close()
            list_values = []
            for line in text:
                key, value = line.strip().split(':')
                list_values.append(key + ":" + value)
            list_email = []
            for item in list_values:
                for i in item:
                    if i == ":":
                        index_of_item = item.index(i)
                        first_part = item[:index_of_item]
                        second_part = item[index_of_item + 1:]
                        if first_part == "email":
                            list_email.append(second_part)
            question = input("Type customer's email to send receipt: ")
            if question in list_email:
                print("Receipt has been sent to", question, "email address")
            else:
                print("this email", question, "is not in the purchase history")

        except Exception as e: #Function to handle exception for invalid input
            print("Something gets wrong. Try again.")
            self.owner_menu()

    def chosen_restaurant(self, rest_id): #Function to select restaurant
        f = open(self.fullPath_restaurant, 'r')
        text = f.readlines()
        f.close()
        list_values = []
        for line in text:
            key, value = line.strip().split(':')
            list_values.append(key + ":" + value)
        text.clear()
        chosen_restaurant = []
        for item in range(len(list_values)):
            if list_values[item] == rest_id:
                chosen_restaurant.append(list_values[item:item+7])
        result = ""
        list_values.clear()
        for item in chosen_restaurant:
            for i in item:
                result+=str(i)+"\n"
        print("Restaurant's information:")
        print(result)

        try:
            question = int(input("Type 0 to go back to customer menu or type 1 to view menu: "))
            if question == 0:
                self.customer_menu()
            elif question == 1:
                self.view_menu_restaurant(rest_id)
            else:
                print("Invalid option. Try again.")
                self.customer_menu()

        except Exception as e: #Function to handle exception for invalid input
            print("Something gets wrong. Try again.")
            self.customer_menu()

    def view_menu_restaurant(self,rest_id): #Function to view the menu of a restaurant.
        try:
            filename_menu =self.fullPath_menu
            f = open(filename_menu, 'r')
            text = f.readlines()
            f.close()
            list_values = []
            for line in text:
                key, value = line.strip().split(':')
                list_values.append(key + ":" + value)
            chosen_restaurant_menu = []
            for i in range(len(list_values)):
                if list_values[i] == rest_id:
                    chosen_restaurant_menu.append(list_values[i:i+6])
            result = []
            for item in chosen_restaurant_menu:
                for i in item:
                    result.append(i)
            chosen_restaurant_menu.clear()
            print("Item details:")
            item_price=[]
            for item in range(len(result)):
                if result[item] == rest_id:
                    print(result[item+1:item+6])
                    chosen_restaurant_menu.append(result[item+1])
                    item_price.append(result[item+1])
                    item_price.append(result[item+4])
            only_id=[]
            for item in chosen_restaurant_menu:
                for i in range(len(item)):
                    if item[i] == ":":
                        only_id.append(item[i+1::])

            list_items=[]

            while True:
                question = input("Enter id of the item to order: ")
                if question.isdigit() == False:
                    print("Please, type only numbers")
                elif question not in only_id:
                    print("id of the item is not in the given list")
                else:
                    if question not in list_items:
                        list_items.append(question)
                next_question = input("Type any number to continue entering items or type 0 to finish: ")
                if int(next_question) == 0:
                    break
            price_per_item = []
            for item in list_items:
                for i in range(len(item_price)):
                    if "id_item:"+item == item_price[i]:
                        price_per_item.append(item_price[i+1])
            total_price = []
            for item in price_per_item:
                for i in range(len(item)):
                    if item[i] == ":":
                        total_price.append(item[i+1::])
            sum = 0
            for price in total_price:
                sum = sum + int(price)

            purchase_information = []
            for i in list_items:
                for item in range(len(result)):
                    if result[item] == "id_item:"+i:
                        purchase_information.append(result[item-1])
                        purchase_information.append(result[item])
                        purchase_information.append(result[item+1])
                        purchase_information.append(result[item+3])
            sum_for_customer = "total_price:"+str(sum)
            purchase_information.append(sum_for_customer)
            while True:
                if len(list_items)== 0:
                    print("Unfortunately, your shopping cart is empty \n")
                    question = int(input("Type 1 to back to customer menu \n"
                                     "type 0 to view menu again: "))
                    if question == 1:
                        self.customer_menu()
                        break
                    elif question == 0:
                        self.view_menu_restaurant(rest_id)
                        break
                    else:
                        print("Invalid option. Try again")

                elif sum < 25: #to check if the order item total is less than 25$
                    print("Unfortunately, your total price is less than $25 \n")
                    question = int(input("Type 1 to back to customer menu \n"
                                         "type 0 to view menu again: "))
                    if question == 1:
                        self.customer_menu()
                        break
                    elif question == 0:
                        self.view_menu_restaurant(rest_id)
                        break
                    else:
                        print("Invalid option. Try again")
                else:
                    print("ID of items in your shopping cart: ",list_items)
                    print("Total price is:",str(sum),"\n")
                    question = int(input("Type 2 to back to customer menu \n"
                                         "Type 1 to order \n"
                                         "type 0 to view menu again: "))
                    if question == 2:
                        self.customer_menu()
                        break
                    elif question == 1:
                        query_email = input("Please, type your email address: ")
                        email = "email:"+query_email
                        purchase_information.append(email)
                        self.make_order(sum,purchase_information)
                        break
                    elif question == 0:
                        self.view_menu_restaurant(rest_id)
                        break
                    else:
                        print("Invalid option. Try again")

        except Exception as e: #Function to handle exception for invalid input
            print("Something gets wrong. Try again.")
            self.customer_menu()

    def search_restaurant_by_suburb(self): #Function to search restaurant by suburb
        f = open(self.fullPath_restaurant, 'r')
        text = f.readlines()
        f.close()
        list_values = [] #lists the availabe restaurants in the suburb
    
        for line in text:
            key, value = line.strip().split(':')
            list_values.append(key + ":" + value)
      
        name_restaurant = []
        postcode = input("Type your postcode: ")
        keyword = "postcode:"+str(postcode)
        exist = False
      
        for item in range(len(list_values)):
            if list_values[item] == keyword:
                #print(list_values[item])
                name_restaurant.append(item-6)
                exist = True
            elif list_values[item] != keyword:
                pass

        while True:
            if exist == True:
                list_restaurant=[]
                for item in range(len(list_values)):
                    for i in name_restaurant:
                        if item == i:
                            list_restaurant.append(list_values[item][0::])
               
                result =''
                con = 0
                for i in list_restaurant:
                    con += 1
                    result += str(con) + "." + str(i) + "\n"
                print(result)
                result_name = ""
                check = False
                answer = input("Type 0 to search again or type number of your choice: ")
                if answer.isdigit() == True and int(answer) == 0:
                    self.search_restaurant()
                elif answer.isdigit() == True and int(answer) != 0:
                    for i in range(len(list_restaurant)):
                            
                        if int(answer) - 1 == i:
                            result_name+= list_restaurant[i]
                            check = True
                           
                while True:
                    if check == True:
                        return result_name
                    else:
                        print("Invalid option. Try again")
                        break

                break
            else:
                print("Invalid option. Try again")
                break

    def search_restaurant_by_category(self): #Function to search restaurant by category
        try:
            f = open(self.fullPath_restaurant, 'r')
            text = f.readlines()
            f.close()
            list_values = [] #lists the values entered from add item item id , description,..
            for line in text:
                key, value = line.strip().split(':')
                list_values.append(key + ":" + value)
            list_of_categories = set()
            for item in list_values:
                for value in item:
                    if value == ":":
                        index_of_item = item.index(value)
                        first_part = item[:index_of_item]
                        second_part = item[index_of_item + 1:]
                        if first_part == "category":
                            list_of_categories.add(second_part)

            print("Categories of restaurants:")
            count = 0
            for i in list_of_categories:
                count+=1
                print(str(count)+'.'+str(i))
            answer = int(input("Type number of your choice: "))
            query = ""
            list_of_categories = list(list_of_categories)
            for i in range(len(list_of_categories)):
                if answer == i+1:
                    query+=list_of_categories[i]
                    #print(query)
            key_word = 'category:'+str(query)
            index_name = []
            exist = False
            for item in range(len(list_values)):
                if list_values[item] == key_word:
                    #print(list_values.index(item))
                    position = item-2
                    index_name.append(position)
                    exist = True
                elif list_values[item] != key_word:
                    pass
            while True:
                if exist != True:
                    print("Invalid option. Try again")
                    break
                   
                else:
                    name_restaurant = []
                    for item in range(len(list_values)):
                        for pos in index_name:
                            if item == pos:
                             
                                name_restaurant.append(list_values[item][0::])
                    result = ""
                    con = 0
                    for i in name_restaurant:
                        con+=1
                        result+= str(con) + "."+str(i)+"\n"
                    print(result)
                    result_name = ''
                    answer = input("Type 0 to search again or type number of your choice:")
                    check = False
                    if answer.isdigit() == True and int(answer) == 0:
                        self.search_restaurant()
                    elif answer.isdigit() == True and int(answer) != 0:
                        for i in range(len(name_restaurant)):
                            if int(answer)-1 == i:
                                result_name+= name_restaurant[i]
                                check = True
                            elif int(answer)-1 != i:
                                pass
                    else:  #to handle exception for invalid input
                        check = False
                    while True:
                        if check == True:
                            return result_name
                        else:
                            print("Invalid option. Try again")
                            break
                    break

        except Exception as e: #Function to handle exception for invalid input
            print("Something gets wrong. Try to search again.")
            self.search_restaurant_by_category()

    def __write_to_file_menu(self, data):#Function to write the data to file
        f = open(self.fullPath_menu, 'a+')
        for key, value in data.items():
            f.write('%s:%s\n' % (key, value))
        f.close()

    def check_id_menu(self, id_item):#Function to check the id of the item in menu
        f = open(self.fullPath_menu)
        text = f.readlines()
        f.close()
        list_values = []
        for line in text:
            line = line.strip()
            key, value = line.split(':')
            list_values.append(key + ":" + value)
        count = 0
        for item in list_values:
            for value in item:
                if value == ":":
                    index_of_item = item.index(value)
                    first_part = item[:index_of_item]
                    second_part = item[index_of_item + 1:]
                    if first_part == "id_item" and int(second_part) == int(id_item):
                        count += 1
        if count != 1:
            return False
        elif count == 1:
            return True

    def register_menu(self):#Function to register item to menu
        try:
            item = {"rest_id": "",
                    "id_item": "",
                    "name": "",
                    "description": "",
                    "price": "",
                    "category": ""}

            while True:
                rest_id = int(input("Enter your restaurant id: "))
                if self.check_empty(rest_id) != False:
                    item["rest_id"] = rest_id
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                id_item = int(input("Enter your item id: "))
                if self.check_id_menu(id_item) == False:
                    item["id_item"] = id_item
                    break
                else:
                    print("Id already exists. Try another id.")
            while True:
                name = input("Enter your item name: ")
                if self.check_empty(name) != False:
                    item["name"] = name
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                description = input("Enter your item description: ")
                if self.check_empty(description) != False:
                    item["description"] = description
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                price = int(input("Enter your item price: "))
                if self.check_empty(price) != False:
                    item["price"] = price
                    break
                else:
                    print("Empty input.Please, enter details.")
            while True:
                category = input("Enter category: ")
                if self.check_empty(category) != False:
                    item["category"] = category
                    break
                else:
                    print("Empty input.Please, enter details.")
            print("Your item have been successfully registered.")
            self.__write_to_file_menu(item)
            return item
        except Exception as e: #Function to handle exception for invalid input
            print("Something gets wrong. Try again.")
            self.register_menu()

def main(): #Main function to display the Home page 
    print ("Home page")
    try:
        question = int(input("1. Login\n"
                             "2. Register\n"
                             "0. Exit\n"
                             ""
                             "Type number of your choice: "))
        if question == 1:
            test = MonashEats()
            #test.login_options()
            if test.login_options() == True:
                test.customer_menu()
            # print(result)
        elif question == 2:
            test = MonashEats()
            test.register_options()
            # print(result)
        elif question == 0:
            print("Good bye. Hopefully, will see you again!")
            sys.exit(0)
        else:
            print("Invalid option. Try again")
            main()

    except Exception as e: #Function to handle exception for invalid input
        print("Something gets wrong. Try again.")
        main()

if __name__ == '__main__':
    main()



def menu():
   print("######################################")
   print("Bienvenidos a su horoscopo semanal, elige una de las opciones")
   print("1 Aries\n")
   print("2 Taurus\n")
   print("3 Gemini\n")
   print("4 Cancer\n")
   print("5 Leo\n")
   print("6 Virgo\n")
   print("7 Libra\n")
   print("8 scorpio\n")
   print("9 Sagittarius\n")
   print("10 Capricornus\n")
   print("11 Aquarius\n")
   print("12 Pisces\n") 
   print("13 color de la suerte")
   
user_input = ""

def read_file(texto):
    file = open("signs/" + texto, "r")
    for line in file:
        print(line)
    

while user_input != "exit":
   menu()
    
        

   user_option = input("selecciona cual es tu signo\n")

   if user_option == "1":
      read_file("aries.txt")
   elif user_option == "2":
      read_file("taurus.txt")
   elif user_option == "3":
      read_file("geminis.txt")
   elif user_option == "4":
      read_file("cáncer.txt")
   elif user_option == "5":
       read_file("signs/leo.txt")
   elif user_option == "6":
      read_file("virgo.txt")
   elif user_option == "7":
      read_file("libra.txt")
   elif user_option == "8":
      read_file("escorpio.txt")
   elif user_option == "9":
      read_file("sagittarius.txt")
   elif user_option == "10":
      read_file("capricornus.txt")
   elif user_option == "11":
      read_file("aquarius.txt")
   elif user_option == "12"
      read_file("pisces.txt")               
   elif user_input == "exit":
        print("hasta luego")
        exit()
   
   else:
      print("opcion incorrecta") 
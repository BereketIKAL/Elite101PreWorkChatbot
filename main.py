def Movie():
    print("So let's get started with a question")
    favoriteMovie = input("What is your favorite movie?:  ")
    print("umm, the " + favoriteMovie + " is a cool movie in my opnion")
    print("My favorite movie is  Inception!")
    
def Sport():
    print("Let's get started with a question")
    print("What is your favorite sport?")
    fvorit = input("")
    print("That's is a cool sport!")
    if fvorite == "Basketball":
        print("My favorite sport is also Basketball!")

    print("My favorite sport is Basketball")
def music():
    print("Let's go a ahead and start with a question.")
    print("what music genre do you listen to?(For example: Rap, Jazz, and Rock):")
    genr = input("")
    print("That's a pretty cool music genre")
    print("My favorite music genre is Jazz. I still think that " + genr + "is pretty cool")
#Start of the code

print("Welcome to the Elite 101 chatbot!")
name = input("Hello! Welcome to this chatbot. What is your name?: ")
age = input("It is nice to meet you, " + name + ". How are old are you? ")
print("Greetings "+ name + ", what a pleasure it would be to be " + age + " again")
print("What would you like to speak about, " + name + "?")

print("Please select of the following option(Please select a number 1-4):")
one = "1. Movies"
two = "2. Sports"
three = "3. music"
four = "4. Exit the conversation"
print(one)
print(two)
print(three)
print(four)

print("Please select one of the following options(Enter 1-4):  ")

select = input("")

select = int(select)

if select == 1:
    Movie()


elif select == 4:
        print("I had a great time speaking to you " + name + " have a great day!")
        exit()

elif select == 3:
    music()

elif select == 2:
    Sport()


print("Have a good day! I wonder if we we will be able to continue this conversation some other day")
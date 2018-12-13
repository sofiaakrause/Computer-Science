import webbrowser as wb
import pyautogui as pg
import time as t

points = 0

show = pg.prompt("What is your favorite show? ")

if show == "Gossip Girl":
    pg.alert("That is a really good show!")
    t.sleep(8)
    wb.open("http://xox0gossipgirlrp.tumblr.com/gossipgirl")
    points += 10
elif show == "Friends":
    pg.alert("I love that show!")
    t.sleep(8)
    wb.open("http://www.friends-tv.org/")
    points += 3
elif show == "90210":
    pg.alert("OMG...")
    t.sleep(3)
    points += 5
elif show == "Hawaii Five 0":
    pg.alert("It is very action packed.")
    t.sleep(12)
    wb.open("https://www.youtube.com/watch?v=xy30TGdaEAE")
    points += 7
elif show == "Young and Hungary":
    pg.alert("Sofia and Gabby!")
    t.sleep(8)
    wb.open("https://freeform.go.com/shows/young-hungry/news")
    points += 10
elif show == "Pretty Little Liars":
    pg.alert("Ohhh... That show is scary!")
    t.sleep(12)
    wb.open("https://www.youtube.com/results?search_query=pretty+little+liars+")
    points += 3
else:
    pg.alert("Your favorite show is " + show)

food = pg.prompt("What is your favorite food?")

if food == "ice cream":
    pg.alert("I love ice cream!")
    t.sleep(8)
    wb.open("https://www.benjerry.com/flavors")
    points += 15
elif food == "cookies":
    pg.alert("Yummy!")
    t.sleep(8)
    wb.open("https://www.allrecipes.com/video/626/best-chocolate-chip-cookies/")
    points += 12
elif food == "pizza":
    pg.alert("Cheesy Goodness")
    t.sleep(8)
    wb.open("https://tasty.co/recipe/20-minute-one-pan-pizza")
    points += 10
elif food == "candy":
    pg.alert("I think everyone likes candy...")
    t.sleep(8)
    wb.open("https://www.candy.com/")
    points += 5
elif food == "hamburgers":
    pg.alert("BBQs are the best!")
    t.sleep(3)
    points += 8
elif food == "tacos":
    pg.alert("Delicious!")
    t.sleep(8)
    wb.open("https://www.allrecipes.com/recipes/1219/world-cuisine/latin-american/mexican/main-dishes/tacos/")
    points += 5
else:
    pg.alert("You enjoy eating " + food)
    
subject = pg.prompt("What is your favorite class?")

if subject == "7th English":
    pg.alert("#shakespear")
    t.sleep(8)
    wb.open("https://www.biography.com/people/william-shakespeare-9480323")
    points += 3
elif subject == "Math":
    pg.alert("I love that class!")
    t.sleep(8)
    wb.open("http://www.math.com/")
    points += 5
elif subject == "Science":
    pg.alert("Nature is amazing!")
    t.sleep(12)
    wb.open("https://www.youtube.com/channel/UCWkOjdpqIcKZrnjefwWMKAQ")
    points += 3
elif subject == "Spanish":
    pg.alert("HOLA")
    t.sleep(8)
    wb.open("http://www.spanishdict.com/")
    points += 10
elif subject == "History":
    pg.alert("It is fascinating:)")
    t.sleep(8)
    wb.open("https://www.history.com/")
    points += 12
elif subject == "Art":
    pg.alert("The most relaxing subject!")
    t.sleep(8)
    wb.open("https://www.historylists.org/art/20-of-the-world%E2%80%99s-most-famous-art-pieces.html")
    points += 15
else:
    pg.alert("You love " + subject)
    
place = pg.prompt("What is your favorite place?")

if place == "Mexico":
    pg.alert("What an amazing place!")
    t.sleep(12)
    wb.open("https://www.youtube.com/watch?v=J2vfi_xQpIw")
    points +=15
elif place == "Aspen":
    pg.alert("I love skiing there!")
    t.sleep(3)
    points += 15
elif place == "Africa":
    pg.alert("All the animals are amazing:)")
    t.sleep(8)
    wb.open("https://www.awf.org/wildlife-conservation/all")
    points += 5
elif place == "Italy":
    pg.alert("It is my favorite place to go during the summer!")
    t.sleep(8)
    wb.open("https://www.walksofitaly.com/blog/all-around-italy/the-16-most-iconic-foods-to-eat-in-italy")
    points += 10
elif place == "Dubai":
    pg.alert("You must go there!!!")
    t.sleep(3)
    points += 5
elif place == "Switzerland":
    pg.alert("The lakes there are amazing;)")
    t.sleep(8)
    wb.open("https://www.google.com/destination?q=switzerland&rlz=1C1GCEA_enUS752US761&site=search&output=search&dest_mid=/m/06mzp&sa=X&ved=0ahUKEwj31OSVi8XeAhWQneAKHdQOC9oQ6tEBCEIoBDAA#dest_mid=/m/06mzp&tcfs=EhwaGAoKMjAxOC0xMS0yNBIKMjAxOC0xMS0yOCAB")
    points += 10
else:
    pg.alert("My favorite place is " + place)

animal = pg.prompt("What is your favorite animal?")

if animal == "dog":
    pg.alert("They are so adorable!")
    t.sleep(8)
    wb.open("https://www.scritchspot.com/places/adopt/?gclid=EAIaIQobChMIyquNsovF3gIVUkwNCh1TrwurEAAYASAAEgK6ePD_BwE")
    points += 10
elif animal == "cat":
    pg.alert("You are special... not everyone likes them")
    t.sleep(12)
    wb.open("https://www.youtube.com/watch?v=XyNlqQId-nk")
    points += 7
elif animal == "squirrel":
    pg.alert("I really want a sugar glider")
    t.sleep(3)
    points += 3
elif animal == "pig":
    pg.alert("OINK!!!")
    t.sleep(3)
    points += 5
elif animal == "dolphin":
    pg.alert("They are my favorite marine animal...")
    t.sleep(8)
    wb.open("https://www.nationalgeographic.com/animals/mammals/c/common-bottlenose-dolphin/")
    points += 10
elif animal == "turtle":
    pg.alert(":( they are endangered")
    t.sleep(8)
    wb.open("https://www.turtleconservancy.org/")
    points += 5
else:
    pg.alert("My favorite animal is " + animal)

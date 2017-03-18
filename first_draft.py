import time

from ascii_images import bike_ascii
   

print """
    Quiz: What's the Best Workout for Your Personality Type
    """
print bike_ascii
time.sleep(1.5)
name = raw_input("What is your name? ")
time.sleep(0.5)
print "\n\nHello, %s!" % (name) + "\n"
time.sleep(1)

print "Today we are going to determine your personality type and associated exercise style.\n"
time.sleep(1.5)
print "Understanding the nature of your personality comes in handy for landing the perfect job or fine-tuning communication skills with your partner.\n"
time.sleep(2)
print "...but did you ever consider the role your personality type plays in determining your fitness preferences?\n"
time.sleep(2)
print "Research suggests that people who engage in personality-appropriate physical activity will do so more consistently, enjoy their workout more and ultimately have a greater overall fitness experience.\n"
time.sleep(2)
print "In the following quiz, you will be asked questions in each of these categories:\n"
time.sleep(1.5)

print "\t ACHIEVEMENT\n"
time.sleep(1.5)
print "\t STRESS MANAGEMENT\n"
time.sleep(1.5)
print "\t SELF ESTEEM\n"
time.sleep(1.5)
print "\t SEARCH FOR MEANING\n"
time.sleep(1.5)
print "\t MOOD AND TENSION\n"
time.sleep(1.5)
print "\t PLAYFULNESS\n"
time.sleep(2)

print "Answer each question by typing YES, NO, or IN BETWEEN.\n"
time.sleep(2)
print "Once you have answered all the questions, we will show you which section you score the highest, your personality type and the associated exercises to try and to avoid.\n"
time.sleep(2)
print "The area with your highest score is your personality match and motivator for exercise.\n\n\n"
time.sleep(2)

begin_prompt = raw_input("ARE YOU READY TO BEGIN? ").lower()
time.sleep(2)
if (begin_prompt == "yes" or "ok" or "y" or "sure"):
    print "\nOk %s! Lets get started.\n\n\n" % (name)
else:
    print "Too bad %s! You have gone too far to turn around!" % (name)

score_dict = {}

time.sleep(2)
print """
    ***Part One: ACHIEVEMENT***
    """
time.sleep(1.5)    
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" 
time.sleep(2)

total_ach = 0
statements = ["\n1) I like setting challenging goals and trying to achieve them. ", 
                "\n2) I challenge myself to do better in all areas of my life. ", 
                "\n3) I work best when I set tough yet realistic expectations for myself. ", 
                "\n4) I believe I need to set clear goals to have a successful life. ", 
                "\n5) I don't believe in the concept of failure. "]

for statement in statements:
    s1 = raw_input(statement).lower()
    if (s1 == "yes"):
        total_ach += 2
    elif (s1 == "in between"):
        total_ach += 1
    else:
        total_ach +=0 

score_dict["ACHIEVEMENT"] = total_ach
print total_ach

print "\n\nThat concludes the first section. Five more to go. Let's continue.\n\n"


time.sleep(1)
print """
    ***Part Two: STRESS MANAGEMENT***
    """
time.sleep(1)
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" #i want this to count regardless of cap or lowercase
time.sleep(2)

total_stress = 0
statements = ["\n1) My work is very stressful. ", 
                "\n2) There have been a lot of challenges in my life in the past 12 months. ", 
                "\n3) My life rarely feels even and relaxed. ", 
                "\n4) I have to cope with a lot of pressure on a daily basis. ", 
                "\n5) In the past year I have felt 'burned out' by stress. "]

for statement in statements:
    s1 = raw_input(statement).lower()
    if (s1 == "yes"):
        total_stress += 2
    elif (s1 == "in between"):
        total_stress += 1
    else:
        total_stress +=0         

score_dict["STRESS MANAGEMENT"] = total_stress
print total_stress

print "\n\nThat concludes the second section. Four more to go. Let's continue.\n\n"

time.sleep(1)
print """
    ***Part Three: SELF ESTEEM***
    """
time.sleep(2) 
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" #i want this to count regardless of cap or lowercase
time.sleep(1)

total_esteem = 0
statements = ["\n1) When I compare myself to others, I get the feeling they are somehow better than I am. ", 
                "\n2) I get upset with myself when I make mistakes. ", 
                "\n3) I have a hard time accepting myself as I am. ", 
                "\n4) If I could be anyone in the world, I would choose to be someone other than myself. ", 
                "\n5) I don't seem to say or do very much that is worthwhile. "]

for statement in statements:
    s1 = raw_input(statement).lower()
    if (s1 == "yes"):
        total_esteem += 2
    elif (s1 == "in between"):
        total_esteem += 1
    else:
        total_esteem +=0         

score_dict["SELF ESTEEM"] = total_esteem
print total_esteem

print "\n\nThat concludes the third section. Three more to go. Let's continue.\n\n"


time.sleep(1)
print """
    ***Part Four: SEARCH FOR MEANING***
    """
time.sleep(2)
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" #i want this to count regardless of cap or lowercase
time.sleep(1)

total_search = 0
statements = ["\n1) I feel something important is missing in my life. ", 
                "\n2) I often wonder what my life is all about. ", 
                "\n3) When I take time to reflect, I feel troubled by the shallowness of my lifestyle. ", 
                "\n4) There seems to be a deeper purpose to life that I have difficulty connecting to. ", 
                "\n5) I sometimes fear that as my life is ending I will realize I have completely missed the point. "]

for statement in statements:
    s1 = raw_input(statement).lower()
    if (s1 == "yes"):
        total_search += 2
    elif (s1 == "in between"):
        total_search += 1
    else:
        total_search +=0         

score_dict["SEARCH FOR MEANING"] = total_search
print total_search

print "\n\nThat concludes the fourth section. Two more to go. Let's continue.\n\n"


time.sleep(1)
print """
    ***Part Five: MOOD AND TENSION***
    """
time.sleep(1)
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" #i want this to count regardless of cap or lowercase
time.sleep(2)

total_mood = 0
statements = ["\n1) I am an anxious person. ", 
                "\n2) I suffer from feeling blue or depressed. ", 
                "\n3) My body feels tense a lot of the time. ", 
                "\n4) People who know me think I am a moody person. ", 
                "\n5) I worry a lot. "]

for statement in statements:
    s1 = raw_input(statement).lower()
    if (s1 == "yes"):
        total_mood += 2
    elif (s1 == "in between"):
        total_mood += 1
    else:
        total_mood +=0         

score_dict["MOOD AND TENSION"] = total_mood
print total_mood

print "\n\nThat concludes the fifth section. One more to go. Let's continue.\n\n"


time.sleep(1)
print """
    ***Part Six: PLAYFULNESS***
    """
time.sleep(1)
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" 
time.sleep(2)

total_play = 0
statements = ["\n1) I consider myself to be a playful person. ", 
                "\n2) People tell me I am fun to be around. ", 
                "\n3) I like to play games and sports just for the fun of it. ", 
                "\n4) My sense of humor is one of my most valued assets. ", 
                "\n5) I have an easy time getting into a playful spirit. "]

for statement in statements:
    s1 = raw_input(statement).lower()
    if (s1 == "yes"):
        total_play += 2
    elif (s1 == "in between"):
        total_play += 1
    else:
        total_play +=0         

score_dict["PLAYFULNESS"] = total_play
print total_play

print "\n\nThat concludes the last section!\n\n"
time.sleep(1.5)
print "\n\n\nTime for the results! Ready?\n\n\n"
print "\t3!"
time.sleep(0.5)
print " "
time.sleep(0.5)
print " "
time.sleep(0.5)
print " "
time.sleep(1)
print "\t2!"
time.sleep(0.5)
print " "
time.sleep(0.5)
print " "
time.sleep(0.5)
print " "
time.sleep(1)
print "\t1!\n\n"
time.sleep(1)

m = max(score_dict.values())
l = []

for key in score_dict:
    if (score_dict[key] == m):
        l.append(key)      

if len(l) == 1:
    print "The section you scored the highest on was ", l[0]
    print "\nNow lets find out more about you!"
    print " "
    time.sleep(0.5)
    print " "
    time.sleep(0.5)
    print " \n\n"
    time.sleep(0.5)
else:
    print "There was a tie! You scored highest in: ", " and ".join(l)
    time.sleep(2)
    print "\nLets find out about your potential personality types and likes. Read through and decide which is most applicable to your life.\n\n\n"    
    time.sleep(2)
    

for item in l:
    if item == "ACHIEVEMENT":
        print "\n\n\tYOUR PERSONALITY TYPE: TYPE A \n"
        time.sleep(2)
        print "\n\tYOUR FOCUS: Setting and achieving worthwhile goals\n"
        time.sleep(2)
        print "\n\tYOUR LOOK FOR: A personal challenge\n"
        time.sleep(2)
        print "\n\tYOU WILL ENJOY: Challenging activities with clear and measurable outcomes."
        print "\t\t\nExamples include:"
        time.sleep(1)
        print "\t\t-Track events"
        time.sleep(1)
        print "\t\t-Golf"
        time.sleep(1)
        print "\t\t-Rock Climbing"
        time.sleep(1)
        print "\t\t-Weight Training"
        time.sleep(1)
        print "\t\t-Lap Swimming"
        time.sleep(1)
        print "\t\t-Alpine Skiing"
        time.sleep(1)
        print "\t\t-Curling"
        time.sleep(1)
        print "\t\t    or"
        time.sleep(1)
        print "\t\t-Power Walking\n"  
        time.sleep(2)
        print "\n\tYOU WILL PROBABLY NOT ENJOY: Activities in which standards are vague or performance is unevaluated."
        print "\t\nExamples include:"
        time.sleep(1)
        print "\t\t-Aerobics"
        time.sleep(1)
        print "\t\t-Calisthenics"
        time.sleep(1)
        print "\t\t    or"
        print "\t\t-Leisure Swimming\n"
        time.sleep(2)
        print "\n...................................................................."

    elif item == "STRESS MANAGEMENT":
        print "\n\n\n\tYOUR PERSONALITY TYPE: TYPE C \n"
        time.sleep(2)
        print "\n\tYOUR FOCUS: Reducing stress level feelings to be more at ease \n"
        time.sleep(2)
        print "\n\tYOUR LOOK FOR: A chance to take a 'time out' and create mind/body release\n"
        time.sleep(2)
        print "\n\tYOU WILL ENJOY: Regular, aerobic activities which distract or control the mind."
        print "\t\nExamples include:"
        time.sleep(1)
        print "\t\t-Running"
        time.sleep(1)
        print "\t\t-Circuit Training"
        time.sleep(1)
        print "\t\t-Aerobics"
        time.sleep(1)
        print "\t\t-Skating"
        time.sleep(1)
        print "\t\t    or"
        time.sleep(1)
        print "\t\t-Synchronized Swimming\n" 
        time.sleep(2)
        print "\n\tYOU WILL PROBABLY NOT ENJOY: Activities which permit mental worry or which resemble life's stresses."
        print "\t\nExamples include:"
        time.sleep(1)
        print "\t\t-Racquet Sports"
        time.sleep(1)
        print "\t\t-Body Building"
        time.sleep(1)
        print "\t\t    or"
        time.sleep(1)
        print "\t\t-Highly competitive team sports (football, baseball, basketball, etc.)\n"
        time.sleep(2)
        print "\n...................................................................."    

    elif item == "SELF ESTEEM":
        print "\n\n\n\tYOUR PERSONALITY TYPE: TYPE B \n"
        time.sleep(2)
        print "\n\tYOUR FOCUS: Feeling better about yourself\n"
        time.sleep(2)
        print "\n\tYOUR LOOK FOR: Realistic and acheivable goals\n"
        time.sleep(2)
        print "\n\tYOU WILL ENJOY: Activities during which you set the standards and just show up." 
        print "\t\nExamples include:"
        time.sleep(1)
        print "\t\t-Walking"
        time.sleep(1)
        print "\t\t-Time-limited running"
        time.sleep(1)
        print "\t\t-Swimming"
        time.sleep(1)
        print "\t\t-Stationary Cycling"
        time.sleep(1)
        print "\t\t-Rowing"
        time.sleep(1)
        print "\t\t-Aerobics classes"
        time.sleep(1)
        print "\t\t    or"
        time.sleep(1)
        print "\t\t-Jogging\n" 
        time.sleep(2)
        print "\n\tYOU WILL PROBABLY NOT ENJOY: Activities with built-in performance standards of comparisions such as:"
        time.sleep(1) 
        print "\t\t-Ballet"
        time.sleep(1) 
        print "\t\t-Golf"
        time.sleep(1) 
        print "\t\t-Racquet Sports"
        time.sleep(1) 
        print "\t\t-Badminton"
        time.sleep(1) 
        print "\t\t-Tennis"
        time.sleep(1) 
        print "\t\t    or"
        time.sleep(1)
        print "\t\t-Handball\n"
        time.sleep(2)
        print "\n...................................................................."
    
    elif item == "SEARCH FOR MEANING":
        print "\n\n\n\tYOUR PERSONALITY TYPE: TYPE B \n"
        time.sleep(2)
        print "\n\tYOUR FOCUS: Experiencing a sense of purpose and meaning in life \n"
        time.sleep(2)
        print "\n\tYOUR LOOK FOR: An opportunity for an intensive inner journey \n"
        time.sleep(2)
        print "\n\tYOU WILL ENJOY: Activities that are rhythmical, repetitive and inner-directed."
        print "\n\tExamples include:"
        time.sleep(1)
        print "\t\t-Long-distance running"
        time.sleep(1)
        print "\t\t-Cycling"
        time.sleep(1)
        print "\t\t-Swimming"
        time.sleep(1)
        print "\t\t-Mountaineering"
        time.sleep(1)
        print "\t\t    or"
        time.sleep(1)
        print "\t\t-Canoe-ing\n" 
        time.sleep(2)
        print "\n\tYOU WILL PROBABLY NOT ENJOY: Activities such as:"
        time.sleep(1)
        print "\t\t-Racquet sports"
        time.sleep(1)
        print "\t\t-Golf"
        time.sleep(1)
        print "\t\t    or" 
        time.sleep(1)
        print "\t\t-Body building\n"
        time.sleep(2)
        print "\n...................................................................."

    elif item == "MOOD AND TENSION":
        print "\n\n\n\tYOUR PERSONALITY TYPE: TYPE C \n"
        time.sleep(2)
        print "\n\tYOUR FOCUS: Controlling your moods and easing tension \n"              
        time.sleep(2)
        print "\n\tYOUR LOOK FOR: Activities which offer tension-relief and stimulate positive feelings \n"
        time.sleep(2)
        print "\n\tYOU WILL ENJOY: Continuous movement, aerobic, oxygen-fueled activities."
        print "\n\tExamples include:"
        time.sleep(1)
        print "\t\t-Running"
        time.sleep(1)
        print "\t\t-Swimming"
        time.sleep(1)
        print "\t\t-Speed Walking"
        time.sleep(1)
        print "\t\t    or"
        time.sleep(1)
        print "\t\t-Aerobics\n" 
        time.sleep(2)
        print "\n\tYOU WILL PROBABLY NOT ENJOY: Activities which permit mental worry or which resemble life's stress."
        print "\n\tExamples include:"
        time.sleep(1)
        print "\t\t-Raquet sports"
        time.sleep(1)
        print "\t\t-Body building"
        time.sleep(1)
        print "\t\t    or"
        time.sleep(1)
        print "\t\t-Highly competitive team sports (football, baseball, basketball, etc.) \n"
        time.sleep(2)
        print "\n...................................................................."
    
    elif item == "PLAYFULNESS": 
        print "\n\n\n\tYOUR PERSONALITY TYPE: TYPE B \n"
        time.sleep(2)
        print "\n\tYOUR FOCUS: Having fun and encouraging your playful spirit \n"
        time.sleep(2)
        print "\n\tYOUR LOOK FOR: Non-goal-oriented, expressive and spontaneous movements \n"
        time.sleep(2)
        print "\n\tYOU WILL ENJOY: Activities which are game-like or which encourage self-expression."
        print "\n\tExamples include:"
        time.sleep(1)
        print "\t\t-Team Sports"
        time.sleep(1)
        print "\t\t-'Friendly' volleyball"
        time.sleep(1)
        print "\t\t-Badminton"
        time.sleep(1)
        print "\t\t-Horseshoes"
        time.sleep(1)
        print "\t\t-Shuffleboard"
        time.sleep(1)
        print "\t\t-Skating"
        time.sleep(1)
        print "\t\t-Frisbee"
        time.sleep(1)
        print "\t\t    or"
        time.sleep(1)
        print "\t\t-Hula hoop\n" 
        time.sleep(2)
        print "\n\tYOU WILL PROBABLY NOT ENJOY: Repetitive, rule-bound or performance-bound activites."
        print "\n\tExamples include:"
        time.sleep(1)
        print "\t\t-Stationary cycling"
        time.sleep(1)
        print "\t\t-'Running on a treadmill"
        time.sleep(1)
        print "\t\t    or"
        time.sleep(1)
        print "\t\t-Running in place\n" 
        time.sleep(2)
        print "\n...................................................................."    
    
    else:
        print "ERROR"   


   














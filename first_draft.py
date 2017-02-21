import time

print """
    Welcome to my quiz!\n
    """
time.sleep(0.5)
name = raw_input("What is your name? ")
time.sleep(0.5)
print "\n\nHello, %s!" % (name) + "\n"
time.sleep(1)

print "Today we are going to determine your personality type and the best type of exercise for you.\n"
time.sleep(1.5)

print "You will be asked questions surrounding the following personality traits:\n"
print "\t ACHIEVEMENT, STRESS MANAGEMENT, SELF ESTEEM, SEARCH FOR MEANING, MOOD AND TENSION, and PLAYFULNESS\n"
time.sleep(1.5)
print "Answer each question by typing YES, NO, or IN BETWEEN after the question.\n"
time.sleep(1.5)
print "Once you have answered all the questions, we will show you which personality traits have the highest scores.\n"
time.sleep(1.5)
print "The area with your highest score is your personality match and motivator for exercise.\n\n\n"

begin_prompt = raw_input("ARE YOU READY TO BEGIN? ").lower()
if (begin_prompt == "yes" or "ok" or "y" or "sure"):
    print "\nOk %s! Lets get started.\n\n\n" % (name)
else:
    print "Too bad %s! You have gone too far to turn around!" % (name)

score_dict = {}

print """
    ***Part One: ACHIEVEMENT***
    """
time.sleep(1)    
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" 
time.sleep(1)

total_ach = 0
statements = ["1) I like setting challenging goals and trying to achieve them. ", 
                "2) I challenge myself to do better in all areas of my life. ", 
                "3) I work best when I set tough yet realistic expectations for myself. ", 
                "4) I believe I need to set clear goals to have a successful life. ", 
                "5) I don't believe in the concept of failure. "]

for statement in statements:
    s1 = raw_input(statement).lower()
    if (s1 == "yes"):
        total_ach += 2
    elif (s1 == "in between" or "in-between"):
        total_ach += 1
    else:
        total_ach +=0 

score_dict["ACHIEVEMENT"] = total_ach

print "\n\nThat concludes the first section. Five more to go. Let's continue.\n\n"


time.sleep(1)
print """
    ***Part Two: STRESS MANAGEMENT***
    """
time.sleep(1)
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" #i want this to count regardless of cap or lowercase
time.sleep(1)

total_stress = 0
statements = ["1) My work is very stressful. ", "2) There have been a lot of challenges in my life in the past 12 months. ", "3) My life rarely feels even and relaxed. ", "4) I have to cope with a lot of pressure on a daily basis. ", "5) In the past year I have felt 'burned out' by stress. "]

for statement in statements:
    s1 = raw_input(statement).lower()
    if (s1 == "yes"):
        total_stress += 2
    elif (s1 == "in between" or "in-between"):
        total_stress += 1
    else:
        total_stress +=0         

score_dict["STRESS MANAGEMENT"] = total_stress

print "\n\nThat concludes the second section. Four more to go. Let's continue.\n\n"

time.sleep(1)
print """
    ***Part Three: SELF ESTEEM***
    """
time.sleep(1) 
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" #i want this to count regardless of cap or lowercase
time.sleep(1)

total_esteem = 0
statements = ["1) When I compare myself to others, I get the feeling they are somehow better than I am. ", "2) I get upset with myself when I make mistakes. ", "3) I have a hard time accepting myself as I am. ", "4) If I could be anyone in the world, I would choose to be someone other than myself. ", "5) I don't seem to say or do very much that is worthwhile. "]

for statement in statements:
    s1 = raw_input(statement).lower()
    if (s1 == "yes"):
        total_esteem += 2
    elif (s1 == "in between" or "in-between"):
        total_esteem += 1
    else:
        total_esteem +=0         

score_dict["SELF ESTEEM"] = total_esteem

print "\n\nThat concludes the third section. Three more to go. Let's continue.\n\n"


time.sleep(1)
print """
    ***Part Four: SEARCH FOR MEANING***
    """
time.sleep(1)
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" #i want this to count regardless of cap or lowercase
time.sleep(1)

total_search = 0
statements = ["1) I feel something important is missing in my life. ", "2) I often wonder what my life is all about. ", "3) When I take time to reflect, I feel troubled by the shallowness of my lifestyle. ", "4) There seems to be a deeper purpose to life that I have difficulty connecting to. ", "5) I sometimes fear that as my life is ending I will realize I have completely missed the point. "]

for statement in statements:
    s1 = raw_input(statement).lower()
    if (s1 == "yes"):
        total_search += 2
    elif (s1 == "in between" or "in-between"):
        total_search += 1
    else:
        total_search +=0         

score_dict["SEARCH FOR MEANING"] = total_search

print "\n\nThat concludes the fourth section. Two more to go. Let's continue.\n\n"


time.sleep(1)
print """
    ***Part Five: MOOD AND TENSION***
    """
time.sleep(1)
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" #i want this to count regardless of cap or lowercase
time.sleep(1)

total_mood = 0
statements = ["1) I am an anxious person. ", "2) I suffer from feeling blue or depressed. ", "3) My body feels tense a lot of the time. ", "4) People who know me think I am a moody person. ", "5) I worry a lot. "]

for statement in statements:
    s1 = raw_input(statement).lower()
    if (s1 == "yes"):
        total_mood += 2
    elif (s1 == "in between" or "in-between"):
        total_mood += 1
    else:
        total_mood +=0         

score_dict["MOOD AND TENSION"] = total_mood

print "\n\nThat concludes the fifth section. One more to go. Let's continue.\n\n"


time.sleep(1)
print """
    ***Part Six: PLAYFULNESS***
    """
time.sleep(1)
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" 
time.sleep(1)

total_play = 0
statements = ["1) I consider myself to be a playful person. ", "2) People tell me I am fun to be around. ", "3) I like to play games and sports just for the fun of it. ", "4) My sense of humor is one of my most valued assets. ", "5) I have an easy time getting into a playful spirit. "]

for statement in statements:
    s1 = raw_input(statement).lower()
    if (s1 == "yes"):
        total_play += 2
    elif (s1 == "in between" or "in-between"):
        total_play += 1
    else:
        total_play +=0         

score_dict["PLAYFULNESS"] = total_play

print "\n\nThat concludes the last section!\n\n"
time.sleep(0.5)
print "Time for the results! Ready?\n\n\n"
print "3!"
time.sleep(0.5)
print "2!"
time.sleep(0.5)
print "1!\n\n"
time.sleep(0.5)


highest_score = max(score_dict, key = score_dict.get)
print "The section you score the highest on was " + highest_score + ".\n\n"

if highest_score == "ACHIEVEMENT":
    print "\tPERSONALITY TYPE: A \n"
    time.sleep(1.5)
    print "\tYOUR FOCUS: Setting and achieving worthwhile goals\n"
    time.sleep(1.5)
    print "\tYOUR LOOK FOR: A personal challenge\n"
    time.sleep(1.5)
    print "\tYOU WILL ENJOY: Challenging activities with clear and measurable outcomes. Examples include: track events, golf, rock climbing, weight training, lap swimming, alpine skiing, curling or power walking \n"
    time.sleep(1.5)
    print "\tYOU WILL PROBABLY NOT ENJOY: Activities in which standards are vague or performance is unevaluated. Examples include: aerobics, calisthenics or leisure swimming \n" 
elif highest_score == "STRESS MANAGEMENT":
    print "\tPERSONALITY TYPE: C \n"
    time.sleep(1.5)
    print "\tYOUR FOCUS: Reducing stress level feelings to be more at ease \n"
    time.sleep(1.5)
    print "\tYOUR LOOK FOR: A chance to take a 'time out' and create mind/body release\n"
    time.sleep(1.5)
    print "\tYOU WILL ENJOY: Regular, aerobic activities which distract or control the mind. Example include: running, circuit training, aerobics, skating or synchronized swimming \n"
    time.sleep(1.5)
    print "\tYOU WILL PROBABLY NOT ENJOY: Activities which permit mental worry or which resemble life's stresses. Examples include: racquet sports, body building, and highly competitive team sports (football, baseball, basketball, etc.) \n"
elif highest_score == "SELF ESTEEM":
    print "\tPERSONALITY TYPE: B \n"
    time.sleep(1.5)
    print "\tYOUR FOCUS: Feeling better about yourself\n"
    time.sleep(1.5)
    print "\tYOUR LOOK FOR: Realistic and acheivable goals\n"
    time.sleep(1.5)
    print "\tYOU WILL ENJOY: Activities during which you set the standards and just show up. Examples include: walking, time-limited running, swimming, stationary cycling, rowing, aerobics classes and jogging\n"
    time.sleep(1.5)
    print "\tYOU WILL PROBABLY NOT ENJOY: Activities with built-in performance standards of comparisions such as ballet, golf, racquet sports, badminton, tennis or handball\n"
elif highest_score == "SEARCH FOR MEANING":
    print "\tPERSONALITY TYPE: B \n"
    time.sleep(1.5)
    print "\tYOUR FOCUS: Experiencing a sense of purpose and meaning in life \n"
    time.sleep(1.5)
    print "\tYOUR LOOK FOR: An opportunity for an intensive inner journey \n"
    time.sleep(1.5)
    print "\tYOU WILL ENJOY: Activities that are rhythmical, repetitive and inner-directed. Examples include: long-distance running, cycling, swimming, mountaineering or canoe-ing \n"
    time.sleep(1.5)
    print "\tYOU WILL PROBABLY NOT ENJOY: Activities such as racquet sports, golf and body building \n"
elif highest_score == "MOOD AND TENSION":
    print "\tPERSONALITY TYPE: C \n"
    time.sleep(1.5)
    print "\tYOUR FOCUS: Controlling your moods and easing tension \n"
    time.sleep(1.5)
    print "\tYOUR LOOK FOR: Activities which offer tension-relief and stimulate positive feelings \n"
    time.sleep(1.5)
    print "\tYOU WILL ENJOY: Continuous movement, aerobic, oxygen-fueled activities. Examples include: running, swimming, speed walking and aerobics \n"
    time.sleep(1.5)
    print "\tYOU WILL PROBABLY NOT ENJOY: Activities which permit mental worry or which resemble life's stress. Examples include: raquet sports, body building, and highly competitive team sports (football, baseball, basketball, etc.) \n"
elif highest_score == "PLAYFULNESS": 
    print "\tPERSONALITY TYPE: B \n"
    time.sleep(1.5)
    print "\tYOUR FOCUS: Having fun and encouraging your playful spirit \n"
    time.sleep(1.5)
    print "\tYOUR LOOK FOR: Non-goal-oriented, expressive and spontaneous movements \n"
    time.sleep(1.5)
    print "\tYOU WILL ENJOY: Activities which are game-like or which encourage self-expression. Examples include: team sports, 'friendly' volleyball, badminton, horseshoes, shuffleboard, skating, Frisbee or hula hoop \n"
    time.sleep(1.5)
    print "\tYOU WILL PROBABLY NOT ENJOY: Repetivie, rule-bound or performance-bound activites. Examples include: stationary cycling, running on a treadmill or running in place \n"             
else:
    print "\terror"    



















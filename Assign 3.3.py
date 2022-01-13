score = input("Enter Score: ")
score_float = float(score)
#try:
#    score_float = float(score)
#except:
#    print("Error: Please enter a number between 0.0 and 1.0")
#    quit()
if score_float >= 0.9:
    print("A")
elif score_float >= 0.8:
    print("B")
elif score_float >= 0.7:
    print("C")
elif score_float >= 0.6:
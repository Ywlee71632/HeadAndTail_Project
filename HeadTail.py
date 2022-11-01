import random

#Write a function that simulates flipping a coin (2 possible value: heads or tails) using a random number generator.
#It should continue "flipping" the coin until it lands on "heads" 3 times in a row.
#Once that has occurred, the function should print out the number of total flips that occurred. 
def headTail():
    results = []
    heads = 0
    while (heads != 3): 
        answer = random.randint(0,1)
        if (answer == 0):
            results.append("H")
            heads += 1
        else:
            results.append("T")
            heads = 0
    
    for x in results:
        print (x)

def main():
    headTail()

if __name__ == "__main__":
    main()

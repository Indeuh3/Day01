import random; import time; nb, guess = random.randint(1,100), int(input("Entrez un nb: ")); exec("""while guess!=nb : print("Plus petit") if nb<guess else print("Plus grand"); time.sleep(0.5); guess=int(input("Entrez un nb: "))"""); print("Bravo, tu as trouvé!")
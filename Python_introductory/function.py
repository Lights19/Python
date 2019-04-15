def ask_ok(prompt,tries=4,reminder="please try again!"): # def created a funcion ask_ok
    while True:
        ok=input(prompt)
        if ok in ('y','YES','yes'):
            return True
        if ok in ('n','no','nope'):
            return False
        tries=tries-1
        if tries<0:
            raise ValueError('you are in different direction')
        print(reminder)

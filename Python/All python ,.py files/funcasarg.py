def scott(ok):

    def some():
        print("i understand everything now")

        ok()

    return some

def mind():
    print("something is exactly missing when iam learning")


mind=scott(mind)#using function as arguments
print(mind())
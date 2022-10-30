def dec1(func):
    def nowExec():
        print("Executing Now")
        func()
        print("Executed")
    return nowExec


@dec1
def sample_function():
    print("This is Saurabh")


sample_function()


# ----------------------------------
# Executing Now
# This is Saurabh
# Executed
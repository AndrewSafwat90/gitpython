print("print from file 1")


if 1 == 1:
    print("true")
else:
    print("false")


if __name__ == "__main__":
    print("file 1 is run directly")

    def hello():
        print("Hello function from file 1")

else:
    print("file 1 is imported")


hello()

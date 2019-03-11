def main():
    f = open("user_data.csv", mode="r")

    data = f.read()

    f.close()

    print(data)
    print(type(f.read()))


if __name__ == '__main__':
    main()

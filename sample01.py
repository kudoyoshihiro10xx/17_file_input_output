def main():
    f = open("user_data.csv", mode="r")

    data = f.read()

    print("close()する前", f.closed)

    f.close()

    print("close()した後", f.closed)

    print(data)
    # print(type(f.read()))


if __name__ == '__main__':
    main()

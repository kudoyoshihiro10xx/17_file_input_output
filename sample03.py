def main():
    with open("user_data.csv", mode="r") as f:
        data = f.read()

    print(f.closed)
    print(data)


if __name__ == '__main__':
    main()

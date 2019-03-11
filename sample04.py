""""
課題

user_data.csv というテキストファイルに記載されている
ユーザー名をすべて出力して下さい

次のように出力されてばOK

Ken Tanaka
Tom Ford
Ieyasu Tokugawa

"""


def main():
    f = open("user_data.csv", mode="r")

    data = f.read()

    # print(type(data))
    #
    # print(data.split("\n"))

    records = data.split("\n")

    for data_list in records:
        name = data_list.split(",")[0]
        print(name)

        # for yyy in xxx.split(","):
        #     print(yyy)

    # print(records[0].split(",")[0])
    # print(records[1].split(",")[0])
    # print(records[2].split(",")[0])

    f.close()


if __name__ == '__main__':
    main()

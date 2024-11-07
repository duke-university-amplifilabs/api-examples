from client import DukeApi


def main():
    duke_api = DukeApi()
    states = duke_api.list_states()

    print("Available states: ", states)


if __name__ == "__main__":
    main()

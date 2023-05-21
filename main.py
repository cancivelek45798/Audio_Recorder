import Modules
while True:
    print("1: record audio\n2: play audio\n0: exit")
    choice = input(">")

    if choice == "1":
        while True:
            frec = input("enter frequency (default = 44100): ") or 44100
            duration = input("enter recording time length: ") or 5
            file_name = input("enter file name: ") or "recording0"
            try:
                Modules.record_audio(int(frec), int(duration), file_name)
                break
            except ValueError:
                print("Pay attention to the use of letters and numbers!")
        break
    elif choice == "2":
        file_name = input("enter file name: ")
        Modules.play_audio(file_name)
        break
    elif choice == "0":
        break
    else:
        print("incorrect choice!")

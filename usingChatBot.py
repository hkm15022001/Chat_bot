def main():
    valid_choices = ["1", "2", "3"]
    stt = input("1. PhoBert\n2. LogisticRegression\n3. NaiveBayes\nChon chatbot: ")
    while stt not in valid_choices:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.\n")
        stt = input("1. PhoBert\n2. LogisticRegression\n3. NaiveBayes\nChon chatbot: ")

    if stt == "1":
        from PhoBert.chat_using_PhoBert import chat_bot_PhoBERT
    elif stt == "2":
        from LogisticRegression.chat_using_LogisticRegression import chat_bot_LR
    elif stt == "3":
        from NaiveBayes.chat_using_NaiveBayes import chat_bot_NaiveBayes
    print("Bot: Hi! I'm your chat bot. Type 'exit' to end the conversation.")

    while True:
        # Nhận dữ liệu từ bàn phím
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        if stt == "1":
            response = chat_bot_PhoBERT(user_input)
        elif stt == "2":
            response = chat_bot_LR(user_input)
        elif stt == "3":
            response = chat_bot_NaiveBayes(user_input)

        print(f"Bot: {response}\n")


if __name__ == "__main__":
    main()

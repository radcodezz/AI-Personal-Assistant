from rag import ask_pdf

while True:

    question = input("\nAsk: ")

    if question.lower() == "exit":
        break

    answer = ask_pdf(question)

    print("\nAnswer:\n")
    print(answer)
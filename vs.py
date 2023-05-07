import openai

openai.api_key = "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"

while True:
        prompt = input("\Introduce una pregunta: ")

        if prompt == "exit":
                break

        completion= openai.Completion.create(
         engine="text-davinci-003",
         prompt=prompt,
         max_tokens=2023)

        print(completion.choices[0].text)
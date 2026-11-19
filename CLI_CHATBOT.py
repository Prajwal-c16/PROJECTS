import ollama

model_name="llama3.2:latest "
message=[
    {
        "role":"system",
        "content":"act as a high level llm model and help me to learn new topics."

    }
]

while True:
    user_input=input("user:")
    user_role={
        "role":"user",
        "content":user_input
    }

    message.append(user_role)

    A=ollama.chat(model=model_name,messages=message)
    P=(A.message.content)
    print("NINJA AI:",P)
    NINJA_AI={
        "role":"assistant",
        "content":P
    }
    message.append(NINJA_AI)

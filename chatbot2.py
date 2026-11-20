import ollama

model_name=llama3.2:latest
message=[
  {
    "role":"system",
    "content":"you are a frendly AI Assistent"
  }
]
while True:
  user_input=input("user:" )
  user_role={
  "role":"user",
  "content":user_input
  }
  message.append(user_role)
  P=ollama.chat(model=model_name,messages=message)
  print(P.message.content)

VARI_AI={
  "role":"assistant",
  "content":P
}
message.append(VARI_AI)

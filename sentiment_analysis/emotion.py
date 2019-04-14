import paralleldots
paralleldots.set_api_key("ASLpEycGzwLshxgSF5vZEcoZqvTvqwQ2snGDirHov5Q")
# for single sentence
text="I am trying to imagine you with a personality."
response=paralleldots.emotion(text)
print(response)



# for multiple sentence as array
text=["I am trying to imagine you with a personality.","This is shit."]
response=paralleldots.batch_emotion(text)
print(response)

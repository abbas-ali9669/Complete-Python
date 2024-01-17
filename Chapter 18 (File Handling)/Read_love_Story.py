# In this topic we will read about file including emojis. That how to read a file with includes emojis. The default encoding is ("cp1252") which cannot read emojis. For printing emojis we need the advance encoding ("UTF-8") which can easily print the emojis.
with open("file.txt", "r", encoding='UTF-8') as f:
    # print(f.encoding)    # Print the used encoding
    print(f.read())
    # Here are one more thing that we can tell the read method that we want to read only 100 words for doing this we use the arguments
    f.read(100)
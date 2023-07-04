import time
import random
sentences = [
    #paragraph 1
    "The quick brown fox jumps over the lazy dog. This sentence is often used as a typing exercise because it contains all the letters of the English alphabet. It's a great way to practice your typing speed and accuracy. Remember to use proper finger placement and maintain a steady rhythm as you type. With practice, you'll be able to type this sentence quickly and effortlessly.",
    #paragraph 2
    "Typing is an essential skill in today's digital age. Whether you're writing an email, creating a document, or chatting with friends, being able to type quickly and accurately is important. By practicing regularly, you can improve your typing speed and efficiency. Start with simple exercises and gradually increase the difficulty level. Over time, you'll notice significant improvements in your typing skills.",
    #paragraph 3
    "In addition to speed, accuracy is equally crucial when it comes to typing. While it's tempting to rush through a document, it's important to focus on accuracy to avoid errors. Take your time and ensure that each keystroke is deliberate and precise. Use the correct finger placement and pay attention to punctuation and capitalization. With practice, you'll develop muscle memory and become a proficient typist.",
    #paragraph 4
    "There are several online resources available to help you improve your typing skills. Websites offer typing games, exercises, and lessons that are designed to make learning enjoyable and engaging. Many of these resources also provide real-time feedback on your typing speed and accuracy, allowing you to track your progress over time. Take advantage of these tools to enhance your typing abilities.",
    #paragraph 5
    "Remember that typing speed is not the only measure of proficiency. While it's impressive to type quickly, it's equally important to maintain accuracy and clarity. Focus on developing a balance between speed and precision. With practice and dedication, you can become a skilled typist who can effortlessly handle any typing task that comes your way. Keep practicing, and you'll see continuous improvement in your typing abilities."
]

def wpm(user_input, elapsed_time):
    words = user_input.split()
    elapsed_time = elapsed_time / 60
    return int(len(words)//elapsed_time)

def matchSentence(user_input, sentence):
    mistake = 0
    try:
        for i in range(len(sentence)):
            if user_input[i] != sentence[i]:
                mistake = mistake + 1
    except:
        mistake = mistake+1
    
    accuracy = len(sentence) - mistake
    accuracy =  accuracy/len(sentence)*100
    return mistake, accuracy

print("\n\t\t||**** Typing Test ****||")
input('\n\tPress Enter to Start....\n')
time1 = time.time()
sentence = random.choice(sentences)
user_input = input(f"{sentence}\n\nStart Typing from here: ")
time2 = time.time()
elapsed_time = time2-time1
# print(f'Elaspsed Time {elapsed_time}')
mis, acc = matchSentence(user_input, sentence)

print(f"RESULT\nNo. of Mistakes: {mis}\nAccuracy: {acc}")
print(f"WPM: {wpm(user_input, elapsed_time)}")
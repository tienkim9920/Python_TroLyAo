import speech_recognition
from gtts import gTTS
import os
import time
import playsound
import pyttsx3
from datetime import date
from datetime import datetime


robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm Listening")
		audio = robot_ear.listen(mic)

	print("Robot: ...")

	try:
		you = robot_ear.recognize_google(audio, language = 'vi-VN')
	except:
		you = "Tôi không hiểu bạn đang nói gì..."

	print("You: " + you)

	if you == "":
		robot_brain = "Tôi không thể nghe bạn, hãy thử lại"
	elif "Xin chào bạn" in you:
		robot_brain = "xin chào bạn"
	elif "xin chào" in you:
		robot_brain = "xin chào bạn"
	elif "Xin chào" in you:
		robot_brain = "xin chào bạn"
	elif "Cho mình hỏi bạn là ai" in you:
		robot_brain = "Tôi là Robot do ông chủ Nguyễn Kim Tiền đã tạo ra"
	elif "bạn là ai" in you:
		robot_brain = "Tôi là Robot do ông chủ Nguyễn Kim Tiền đã tạo ra"
	elif "Bạn là ai" in you:
		robot_brain = "Tôi là Robot do ông chủ Nguyễn Kim Tiền đã tạo ra"
	elif "đẹp trai không" in you:
		robot_brain = "Ông chủ Tiền rất là đẹp trai"
	elif "ông chủ có đẹp trai không" in you:
		robot_brain = "Ông chủ Tiền rất là đẹp trai"
	elif "Ông chủ có đẹp trai không" in you:
		robot_brain = "Ông chủ Tiền rất là đẹp trai"
	elif "sinh năm bao nhiêu" in you:
		robot_brain = "Ông chủ Tiền sinh năm 2000"
	elif "ông chủ sinh năm bao nhiêu" in you:
		robot_brain = "Ông chủ Tiền sinh năm 2000"
	elif "Ông chủ sinh năm bao nhiêu" in you:
		robot_brain = "Ông chủ Tiền sinh năm 2000"
	elif "Hôm nay là thứ mấy" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "mấy giờ rồi" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S second")
	elif "Mấy giờ rồi" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S second")
	elif "tổng thống là ai" in you:
		robot_brain = "Donald Trump"
	elif "tổng thống" in you:
		robot_brain = "Donald Trump"
	elif "Tổng thống" in you:
		robot_brain = "Donald Trump"	
	elif "president" in you:
		robot_brain = "Donald Trump"
	elif "tạm biệt" in you:
		break
	elif "bạn có ngu không" in you:
		robot_brain = "Bạn ngu thì có"
	elif "Bạn có ngu không" in you:
		robot_brain = "Bạn ngu thì có"
	elif "bạn có bị ngu không" in you:
		robot_brain = "Bạn ngu thì có"
	elif "Bạn có bị ngu không" in you:
		robot_brain = "Bạn ngu thì có"
	elif "bạn có người yêu chưa" in you:
		robot_brain = "Tôi là Robot do Tiền Kim đã tạo ra nên không có trai tim"
	elif "Bạn có người yêu chưa" in you:
		robot_brain = "Tôi là Robot do Tiền Kim đã tạo ra nên không có trai tim"
	elif "địt con mẹ bạn luôn" in you:
		robot_brain = "địt mẹ bạn đấy"
	elif "Địt con mẹ bạn luôn" in you:
		robot_brain = "địt mẹ bạn đấy"
	else:
		robot_brain = "I'm fine thank you and you"

	print("Robot: " + robot_brain)

	voices = robot_mouth.getProperty("voices")

	robot_mouth.setProperty("voice", voices[1].id)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()

	# robot_mouth.say(robot_brain)
	# robot_mouth.runAndWait()
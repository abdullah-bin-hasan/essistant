import requests
from functions.web_calls import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
from functions.system_calls import open_camera, open_notepad, open_browser, open_cmd
from pprint import pprint


if __name__ = '__main__':
	greet_user()
	while True:
		query = take_user_input().lower()


		if 'open notepad' in query:
			open_notepad()


		elif 'open command prompt' in query:
			open_cmd()
		

		elif 'open browser'min query:
			open_browser()
		

		elif 'open camera' in query:
			open_camera()
 		

 		elif 'ip address' in query:
 			ip_address = find_my_ip()
 			speak(f'Your ip address is {ip_address}.\n For your convenience, The address is also printed on the screen!')
 			print('This is your IP address', ip_address)


 		elif 'wikipedia' in query:
 			speak('what do you want to search on wikipedia?')
 			search_query = take_user_input().lower()
 			results = search_on_wikipedia(search_query)
 			speak(f"according to wikipedia, {results}. \n For your convenience, The information is also printed on the screen!'")
 			print(results)
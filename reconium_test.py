from selenium import webdriver
import reconium
import time
import platform


if(platform.system()=='Linux'):
	driver_path = 'resources/geckodriver'
elif(platform.system()=='Windows'):
	driver_path = 'resources/geckodriver.exe'


driver = webdriver.Firefox(executable_path=driver_path)
fps=20

rc = reconium.Recorder(driver,fps)
rc.start()

# record here selenium test
driver.get("https://www.google.com")
time.sleep(10)
driver.quit()

rc.stop()
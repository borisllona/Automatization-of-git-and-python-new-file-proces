#Create-project-automatization

import os
from selenium import webdriver

projectName = input('Write the name of the new project: ')
description = input('Set a description of the project: ')
browser = webdriver.Chrome(executable_path=r"C:\Users\boris\Google Drive\Proyectos Programacion\Proyectos Python\Automatization of git and python new file proces\chromedriver.exe")
browser.get('https://github.com/login')

def createProject():
	#Creates the dir with the python file.
	newPath = r"C:\Users\boris\Google Drive\Proyectos Programacion\Proyectos Python\{}".format(projectName)
	#os.makedirs(newPath)
	#f = open(r'{}\{}.py'.format(newPath,projectName),'w+')
	#f.write('if __name__ == "__main__":	pass')
	login()
	newRepository()
	#os.startfile(r'{}\{}.py'.format(newPath,projectName))

def login():
	#Logs into github account
	logg = browser.find_element_by_xpath('//*[@id="login_field"]')
	logg.send_keys('borisllonalonso@gmail.com')
	pswd = browser.find_element_by_xpath('//*[@id="password"]')
	pswd.send_keys('HqWT2k8G4hqYZaa')
	button = browser.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[4]')
	button.click()

def newRepository():
	#Creates repo and adds the python File
	button = browser.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div/div/h2/a')
	button.click()
	repoName = browser.find_element_by_xpath('//*[@id="repository_name"]')
	repoName.send_keys(projectName)
	descript = browser.find_element_by_xpath('//*[@id="repository_description"]')
	descript.send_keys(description)
	button = browser.find_element_by_xpath('//*[@id="repository_visibility_private"]')
	button.click()
	button = browser.find_element_by_xpath('//*[@id="repository_auto_init"]')
	button.click()
	button = browser.find_element_by_css_selector('button.first-in-line')
	button.submit()
	button = browser.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[3]/div[2]/a[1]')
	button.click()
	button = browser.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[2]/form[2]/file-attachment/p/input')
	button.click()




if __name__ == "__main__":
    createProject()
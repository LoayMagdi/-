import subprocess
import time
import re
import os
import pyperclip
import requests
import time
from colorama import Fore
import uiautomator2 as u2
import os
import csv
import json
from faker import Faker
from rich.console import Console
from flask import Flask, jsonify
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from uiautomator2 import Device
console = Console()

# DPI MUST SET TO 220

def LOGO():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear console for Windows and Unix
    console.print("""
[bold #CC00CC]██╗      ██████╗  █████╗    ██╗   ██╗
[bold #CC00CC]██║      ██╔═══██╗██╔══██╗  ██║   ██║
[bold #CC00CC]██║      ██║   ██║███████║  ██║   ██║
[bold #CC00CC]██║      ██║   ██║██╔══██║╚ ██╗   ██╔╝
[bold #CC00CC]███████  ╚██████╔╝██║  ██║  ╚████╔██║╝ 
[bold #CC00CC]╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚═══╝██║
[bold #CC00CC]                            ████████
[bold #FFD700]Coded By LoayMagdy
[bold #7289DA]Discord:scorepion
[underline green]WhatsApp:+201100575125""", style="bold bright_white")

LOGO()

d = u2.connect()


def list_emulators():
    devices = os.popen("adb devices").read().strip().split("\n")[1:]
    return [device.split()[0] for device in devices if "emulator" in device]

def select_emulator():
    emulators = list_emulators()

    if not emulators:
        print(Fore.RED + "No emulators found. Exiting.")
        exit()

    print(Fore.BLUE + "Select an emulator from the following list:")
    for idx, emulator in enumerate(emulators):
        print(f"{Fore.CYAN}{idx + 1}. {emulator}")

    choice = int(input(Fore.MAGENTA + "Enter the emulator number: ")) - 1
    if 0 <= choice < len(emulators):
        return emulators[choice]
    else:
        print(Fore.RED + "Invalid selection. Exiting.")
        exit()
select_emulator()


def generate_random_names():
    fake = Faker()
    name1 = fake.first_name() 
    name2 = fake.last_name_male() 
    return name1, name2



with open('config.json', 'r') as f:
    config = json.load(f)


password = config['security']['password']
ans1 = config['security']['ans1']
ans2 = config['security']['ans2']
ans3 = config['security']['ans3']


year = str(config['personal_info']['dob']['year'])
month = str(config['personal_info']['dob']['month'])
day = str(config['personal_info']['dob']['day'])

def read_emails_from_file(filename):
    with open(filename, "r") as file:
        emails = file.readlines()
    return [email.strip() for email in emails]


def save_email_to_done_file_with_details(email, password, dob, answer1, answer2, answer3, done_filename="done.csv"):
    with open(done_filename, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, password, dob, answer1, answer2, answer3])

def save_email_to_bad_file(email, bad_filename="bad.csv"):
    with open(bad_filename, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email])

def save_email_to_used_file(email, used_filename="used.csv"):
    with open(used_filename, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email])

def delete_used_email_from_file(email, filename="emails.txt"):
    with open(filename, "r") as file:
        emails = file.readlines()
    emails = [e for e in emails if e.strip() != email]
    
    with open(filename, "w") as file:
        file.writelines([e + "\n" for e in emails])


emails = read_emails_from_file("emails.txt")


for email in emails:
    while True:  
        
        d.keyevent("3") 
        element = d(text="Device Emulator Pro").click()
        element = d.xpath('//android.widget.TextView[@content-desc="Random all"]').click()
        time.sleep(0.5)
        element = d.xpath('//android.widget.TextView[@content-desc="Fast Reboot"]').click()
        time.sleep(0.5)
        element = d.xpath('//android.widget.Button[@resource-id="android:id/button1"]').click()
        time.sleep(0.5)
        d.keyevent("3")  
        package_name = "com.apple.android.music"
        os.system(f"adb shell pm clear {package_name}")  # Clear app data
        element = d(text="Apple Music").click()
        time.sleep(4)
        element = d(text="Agree").click()
        element = d(text="Continue").click()
        element = d(text="DON'T SEND").click()
        element = d(text="NOT NOW").click()
        time.sleep(5)
        eelement = d.xpath('//android.widget.Button[@content-desc="Try It Now"]').click()
        element = d.xpath('//android.widget.Button[@content-desc="Start Trial"]').click()
        element = d(text="Create New").click
        element = d.xpath('//android.widget.Button[@text="Create New Apple ID"]').click()
        
        
        email_field = d.xpath('//android.widget.EditText[@resource-id="acAccountName"]')
        email_field.set_text(email)
        password_field = d.xpath('//android.widget.EditText[@resource-id="acAccountPassword"]')
        password_field.set_text(password)
        verify_field = d.xpath('//android.widget.EditText[@resource-id="verifyPassword"]')
        verify_field.set_text(password)
        time.sleep(1)
        thilandbutton =d.xpath('//android.view.View[@content-desc="Country​/​Region"]').click()
        time.sleep(1)
        thilandbutton2 =d.xpath('//android.view.View[@content-desc="Country​/​Region"]')
        time.sleep(2)
        thilandbutton2.set_text("t")
        time.sleep(2)
        select= d.xpath('//android.widget.Spinner[@content-desc="Taiwan"]').click()
        time.sleep(1)
        thialndselect=d.xpath('//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="    Thailand"]').click()
        time.sleep(1)
        agree = d(description="Agree to Terms and Conditions").click()
        time.sleep(1)
        next_button = d(description="Next").click()
        time.sleep(3)


        email_error_element = d.xpath('//android.view.View[@content-desc="This email address is not available. You may already have an Apple Account associated with this address. Please try again or sign in using your existing Apple Account."]')
        
        if email_error_element.exists:
            save_email_to_used_file(email)
            delete_used_email_from_file(email)
            print(f"Email {email} is already used.")
            break  

        
        name1, name2 = generate_random_names()
        first_name_field = d.xpath('//android.widget.EditText[@resource-id="firstName"]')
        first_name_field.set_text(name1)
        last_name_field = d.xpath('//android.widget.EditText[@resource-id="lastName"]')
        last_name_field.set_text(name2)

        year_field = d.xpath('//android.widget.EditText[@content-desc="YYYY"]')
        year_field.set_text(year)
        day_field = d.xpath('//android.widget.EditText[@content-desc="DD"]')
        day_field.set_text(day)
        month_field = d.xpath('//android.widget.EditText[@content-desc="MM"]')
        month_field.set_text(month)


        q1 = d.xpath('//android.widget.Spinner[@resource-id="question1"]').click()
        q1_select = d.xpath('//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="    What was the name of your best friend as a teenager?"]').click()
        answer_q1 = d.xpath('//android.widget.EditText[@resource-id="answer1"]')
        answer_q1.set_text(ans1)

        q2 = d.xpath('//android.widget.Spinner[@resource-id="question2"]').click()
        q2_select = d.xpath('//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="    What is your dream job?"]').click()
        answer_q2 = d.xpath('//android.widget.EditText[@resource-id="answer2"]')
        answer_q2.set_text(ans2)

        q3 = d.xpath('//android.widget.Spinner[@resource-id="question3"]').click()
        q3_select = d.xpath('//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="    In what city did your parents meet?"]').click()
        answer_q3 = d.xpath('//android.widget.EditText[@resource-id="answer3"]')
        answer_q3.set_text(ans3)

        device_id = "emulator-5554"  
        os.system(f"adb -s {device_id} shell input swipe 300 1000 300 500")

        next_button = d(description="Next").click()
        none_button = d.xpath('//android.widget.RadioButton[@content-desc="None "]').click()

        os.system(f"adb -s {device_id} shell input swipe 300 1000 300 500")

        street = d.xpath('//android.widget.EditText[@resource-id="addressOfficialLineFirst"]')
        street.set_text("Street Cairo 1351")

        city = d.xpath('//android.widget.EditText[@resource-id="addressOfficialCity"]')
        city.set_text("Zamalek")

        government = d.xpath('//android.widget.Spinner[@content-desc="Select"]').click()
        government_select = d.xpath('//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="    Bangkok"]').click()
        
        postcode = d.xpath('//android.widget.EditText[@resource-id="addressOfficialPostalCode"]')
        postcode.set_text("16242")
        
        area_code = d.xpath('//android.widget.EditText[@resource-id="phoneOfficeAreaCode"]')
        area_code.set_text("02")
        
        phone = d.xpath('//android.widget.EditText[@resource-id="phoneOfficeNumber"]')
        phone.set_text("7136136")

        next_button = d(description="Next").click()


        print(f"Finished processing email: {email}")
        
        user_response = input(f"Do you want to mark this email as done (y),or retry (n)? ")

        if user_response.lower() == 'y':
            dob = f"{day}/{month}/{year}"
            save_email_to_done_file_with_details(email, password, dob, ans1, ans2, ans3)
            delete_used_email_from_file(email)
            print(f"Email {email} moved to done.")
            break  

        elif user_response.lower() == 'n':
            print(f"Retrying email {email}...")
            continue
        else:
            print("Invalid input, please enter 'y', 'n")
            continue  
print("DONE")

app = Flask(__name__)
otp_code = ""

@app.route('/get_otp', methods=['GET'])
def get_otp():
    return jsonify({"otp": otp_code})

# قراءة الحسابات من الملف
def read_accounts():
    accounts = []
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    accounts.append((parts[0], parts[1]))
    except FileNotFoundError:
        print("❌ ملف accounts.txt غير موجود!")
    return accounts

# استخراج OTP من Gmail
def fetch_otp_from_gmail(account, password):
    global otp_code

    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--incognito")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-extensions")
    options.add_argument("window-size=800,900")
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        wait = WebDriverWait(driver, 10)
        driver.get("https://accounts.google.com/")

        email_field = wait.until(EC.element_to_be_clickable((By.ID, "identifierId")))
        email_field.send_keys(account)
        email_field.send_keys(Keys.RETURN)
        time.sleep(2)

        password_field = wait.until(EC.element_to_be_clickable((By.NAME, "Passwd")))
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)
        
        driver.get("https://mail.google.com/mail/u/0/#inbox")
        time.sleep(5)
        
        emails = driver.find_elements(By.CSS_SELECTOR, ".zA")
        for email in emails:
            try:
                subject_element = email.find_element(By.CSS_SELECTOR, "span.bog")
                if "Apple" in subject_element.text:
                    email.click()
                    time.sleep(2)
                    email_body = driver.find_element(By.CSS_SELECTOR, ".a3s").text
                    match = re.search(r'\b\d{6}\b', email_body)
                    if match:
                        otp_code = match.group(0)
                        pyperclip.copy(otp_code)
                        print(f"✅ OTP found: {otp_code}")
                        driver.quit()
                        send_otp_to_emulator(otp_code, selected_emulator)
                        return True
            except:
                continue
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()
    return False

# إرسال OTP إلى المحاكي
def list_emulators():
    devices = os.popen("adb devices").read().strip().split("\n")[1:]
    return [device.split()[0] for device in devices if device.strip()]

def select_emulator():
    emulators = list_emulators()
    if not emulators:
        print("❌ لا يوجد أي محاكيات متاحة.")
        exit()
    print("📱 المحاكيات المتاحة:")
    for idx, emulator in enumerate(emulators):
        print(f"{idx + 1}. {emulator}")
    choice = int(input("➡️ اختر رقم المحاكي: ")) - 1
    return emulators[choice] if 0 <= choice < len(emulators) else exit()

def send_otp_to_emulator(otp, emulator):
    try:
        command = f'adb -s {emulator} shell input text "{otp}"'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ OTP تم إرساله بنجاح!")
        else:
            print("❌ فشل في إرسال OTP:", result.stderr)
    except Exception as e:
        print("⚠️ حدث خطأ أثناء إرسال OTP:", str(e))

# ✅ **تحديد المحاكي في بداية السكريبت**
selected_emulator = select_emulator()
print(f"🎯 سيتم استخدام المحاكي: {selected_emulator}")

# 🔍 **محاولة استخراج الـ OTP تلقائيًا**
print("⌛️ في انتظار الكود OTP...")
time.sleep(5)  # تأخير بسيط لمحاكاة انتظار الكود

# قراءة الحسابات من الملف
accounts = read_accounts()
if not accounts:
    print("❌ لا توجد حسابات في ملف accounts.txt!")
else:
    for gmail_account, gmail_password in accounts:
        print(f"🔍 محاولة تسجيل الدخول بحساب: {gmail_account}")
        if fetch_otp_from_gmail(gmail_account, gmail_password):
            break  # بعد ما نلاقي OTP لأول حساب، نوقف

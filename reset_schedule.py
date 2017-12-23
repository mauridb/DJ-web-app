import schedule
import time
import subprocess


def reset_booking():
    print 'I am working..'
    subprocess.call(["python", "manage.py", "resetbooking"])


def cancel_lecture():
    print 'I am working..'
    subprocess.call(["python", "manage.py", "checklectures"])


# schedule.every(30).seconds.do(job)
schedule.every().sunday.at("00:00").do(reset_booking)

# TODO: i supposed that lectures have 09:00 to 13:00 to implement logic of lecture.starter_date - 2
schedule.every().hour.at("07:00").do(cancel_lecture)
schedule.every().hour.at("08:00").do(cancel_lecture)
schedule.every().hour.at("09:00").do(cancel_lecture)
schedule.every().hour.at("10:00").do(cancel_lecture)
schedule.every().hour.at("11:00").do(cancel_lecture)
# schedule.every(5).seconds.do(cancel_lecture) # to test job

while 1:
    schedule.run_pending()
    time.sleep(1)

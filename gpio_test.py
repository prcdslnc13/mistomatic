from flask import Flask
from flask import render_template
import RPi.GPIO as GPIO

app=Flask(__name__)

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.output(4,1)
status=GPIO.HIGH

@app.route('/')
def readPin():
    global status
    global response
    try:
        if status==GPIO.LOW:
            status=GPIO.HIGH
            print('ON')
            response="Pin is high"
        else:
            status=GPIO.LOW
            print('OFF')
            response="Pin is low"
    except:
        response="Error reading pin"

    GPIO.output(4, status)

    templateData= {
        'title' : 'Status of Pin' + status,
        'response' : response
        }

    return render_template('pin.html', **templateData)

if __name__=="__main__":
    app.run('192.168.1.152')

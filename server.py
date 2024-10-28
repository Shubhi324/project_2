from flask import Flask, Response
import cv2

app = Flask(__name__)

# Capture from camera or stream
cap = cv2.VideoCapture(0)  # Replace with your stream URL if needed

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Encode frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
            # Concatenate frame one by one and show result
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    # Video streaming route
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "selon-x140"

"""
test
test
"""

import cv2,time
import cognitive_face as CF

# wait time[ms]
WAIT_TIME = 5000

# config
with open('AZURE_FACE_KEY', 'r', encoding='utf-8')as f:
    subscription_key = f.readline().strip()

CF.Key.set(subscription_key)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)

# 感情(表情)の種類
emotion_dict = {
    'anger': '😠', 
    'contempt': '😞', 
    'disgust': '😬', 
    'fear': '😨', 
    'happiness': '😀', 
    'neutral': '😐', 
    'sadness': '😢', 
    'surprise': '😯'
}

# 撮影
cap = cv2.VideoCapture(0)

while(True):
    # 確認
    time.sleep(2)
    _, frame = cap.read()
    cv2.imshow("Captured", frame)
    
    # APIに画像を送るときは，urlかpathの方が簡単.
    cv2.imwrite("./img/tmp.jpg", frame)
    
    try:
        # Detect
        faces = CF.face.detect("./img/tmp.jpg", attributes='emotion') 
        print(faces)
        
    except Exception as e:
        print(e)
        print("Emotion API ERROR")
        if cv2.waitKey(WAIT_TIME) & 0xFF == ord('q'):
            break

    # 推定された表情の種類を指定．
    if not face:
        print("No detection")
        pass
    else:
        result = {i:k for i,(k,v) in enumerate(sorted(faces[0]['faceAttributes']['emotion'].items(), key=lambda x:x[1], reverse=True))}[0]
        print(f'Your Reaction: {result}')
        print(f'Computer Reaction: {emotion_dict[result]}')

    if cv2.waitKey(WAIT_TIME) & 0xFF == ord('q'):
        break

# リリース
cap.release()
cv2.destroyAllWindows()

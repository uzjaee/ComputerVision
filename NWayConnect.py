import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('sample.png')

# image 출력
plt.imshow(img)
plt.show()

four_way_flag_list = [] # 같은 픽셀 건너뛰기 위한 리스트 
def four_connect(img):
  x,y = img.shape[:2]
  canvas = img.copy()
  label = [100,100,100] # 맨 처음 색깔 값 설정 
  for h in range(x):
    for w in range(y):
      if (h,w) in four_way_flag_list:
        continue
      if (canvas[h,w] == [255,255,255]).all(): # 이미지 내에서 픽셀 값이 흰색 값 
        four_way_flag_list.append((h,w))  # 같은 픽셀 건너뛰기 위해 flag_list 내 좌표값 저장
        canvas[h,w] = label
        # 4방향 확인 
        flood_fill(h,w+1,label,canvas)
        flood_fill(h,w-1,label,canvas)
        flood_fill(h+1,w,label,canvas)
        flood_fill(h-1,w,label,canvas)
        label = list(np.random.choice(range(256), size=3))

  return canvas
  # 특정 좌표에 대한 확인하는 코드 (재귀함수)
def flood_fill(h,w,label,canvas):
  if (h,w) in four_way_flag_list:
    return
  if (canvas[h,w] == [255,255,255]).all():
    four_way_flag_list.append((h,w))
    canvas[h,w] = label
    # 좌표를 기점으로 다시 4방향 확인 
    flood_fill(h,w+1,label,canvas)
    flood_fill(h,w-1,label,canvas)
    flood_fill(h+1,w,label,canvas)
    flood_fill(h-1,w,label,canvas)

# 4방향과 로직 동일 
eight_way_flag_list =[]
def eight_connect(img):
  x,y = img.shape[:2]
  canvas = img.copy()
  label = [100,100,100]
  for h in range(x):
    for w in range(y):
      if (h,w) in eight_way_flag_list:
        continue
      if (canvas[h,w] == [255,255,255]).all():
        eight_way_flag_list.append((h,w))
        canvas[h,w] = label
        # 4방향에서 확인하는 경우의 수 8방향으로 증가 
        flood_fill(h,w+1,label,canvas)
        flood_fill(h,w-1,label,canvas)
        flood_fill(h+1,w,label,canvas)
        flood_fill(h-1,w,label,canvas)
        flood_fill(h+1,w-1,label,canvas)
        flood_fill(h+1,w+1,label,canvas)
        flood_fill(h-1,w+1,label,canvas)
        flood_fill(h-1,w-1,label,canvas)
        label = list(np.random.choice(range(256), size=3))


  return canvas
def flood_fill(h,w,label,canvas):
  if (h,w) in eight_way_flag_list:
    return
  if (canvas[h,w] == [255,255,255]).all():
    eight_way_flag_list.append((h,w))
    canvas[h,w] = label
    flood_fill(h,w+1,label,canvas)
    flood_fill(h,w-1,label,canvas)
    flood_fill(h+1,w,label,canvas)
    flood_fill(h-1,w,label,canvas)
    flood_fill(h+1,w-1,label,canvas)
    flood_fill(h+1,w+1,label,canvas)
    flood_fill(h-1,w+1,label,canvas)
    flood_fill(h-1,w-1,label,canvas)

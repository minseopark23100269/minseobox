import cv2 as cv

# 비디오 캡처 객체 생성 (기본 웹캠: 0)
video = cv.VideoCapture(0)

# 캡처 객체 확인
if not video.isOpened():
    print("웹캠에 연결할 수 없습니다.")
    exit()

# 동영상 저장 설정
fps = 20.0  # 프레임 속도
frame_size = (int(video.get(cv.CAP_PROP_FRAME_WIDTH)), int(video.get(cv.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv.VideoWriter_fourcc(*'XVID')  # 코덱 설정
video_writer = cv.VideoWriter('flipped_output.avi', fourcc, fps, frame_size)

recording = False
flip_enabled = False  # 상하 반전 초기값: 비활성화

while True:
    ret, frame = video.read()
    if not ret:
        print("프레임을 가져올 수 없습니다.")
        break

    # flip 기능 활성화 여부에 따라 상하 반전 적용
    if flip_enabled:
        flipped_frame = cv.flip(frame, 0)  # 상하 반전 적용
    else:
        flipped_frame = frame  # 원본 프레임 유지

    # Record 모드 시 빨간색 원 표시
    if recording:
        cv.circle(flipped_frame, (50, 50), 20, (0, 0, 255), -1)

    # 프레임 화면에 표시
    cv.imshow('Video Recorder', flipped_frame)

    # Record 모드일 때 반전된 영상 저장
    if recording:
        video_writer.write(flipped_frame)

    # 키 입력 처리
    key = cv.waitKey(1) & 0xFF
    if key == 27:  # ESC 키: 프로그램 종료
        break
    elif key == 32:  # Space 키: Preview ↔ Record 모드 전환
        recording = not recording  # 모드 전환
    elif key == ord('f'):  # 'f' 키로 flip 기능 활성화/비활성화 전환
        flip_enabled = not flip_enabled

# 자원 해제
video.release()
video_writer.release()
cv.destroyAllWindows()

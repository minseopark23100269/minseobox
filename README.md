# minseobox
 My simple but precious video recorder using OpenCV
# 상하반전 기능이 포함된 비디오 레코더

OpenCV를 사용하여 실시간으로 카메라 영상을 상하 반전(Vertical Flip)할 수 있는 비디오 레코더입니다. 사용자는 영상 미리보기, 상하 반전 기능 활성화/비활성화, 그리고 녹화 기능을 활용할 수 있습니다.

## 주요 기능
- **실시간 미리보기**: 카메라 영상을 실시간으로 표시합니다.
- **녹화 모드**: space키를 누르면 파일로 저장합니다.
- **상하 반전 기능**: `f` 키로 상하 반전 기능을 활성화 또는 비활성화할 수 있습니다.
- **키보드 조작**:
  - `Space` 키: 미리보기와 녹화 모드 전환.
  - `f` 키: 상하 반전 기능 활성화/비활성화.
  - `ESC` 키: 프로그램 종료.

## 필요 조건
- **Python 3.x**: Python이 설치되어 있어야 합니다.
- **OpenCV 라이브러리**: 아래 명령어로 설치 가능합니다.
  ```bash
  pip install opencv-python

## 데모 동영상 (YouTube)
- 이 영상은 opencv.py 코드를 실행해서 미리보기와 녹화 모드를 실행하고 flip기능을 보여주며 프로그램을 종료하는 과정을 담은 영상입니다.
- 파일 크기가 커서 유튜브링크를 통해 볼 수 있게 했습니다.
-[YouTube에서 데모 보기](https://www.youtube.com/watch?v=msiHSx5hX5E)

## 데모 동영상 (저장소 파일)
- 이 영상은 opencv를 통해 녹화된 영상입니다.
- 파일 크기가 커서 웹 인터페이스에서 바로 볼 수가 없습니다.
- View raw를 클릭하면 볼 수 있습니다!!
-[동영상 다운로드 및 보기](video/flipped_output.avi)


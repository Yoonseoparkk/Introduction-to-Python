# "from test_package import *"로
# 모듈을 읽어올 때 가져올 모듈
__all__ = ["module_a", "module_b"]  # ==> * 사용 시 읽어올 모듈의 목록

# 또는, 패키지를 읽어 들일 때 처리를 작성할 수 있다.
print(
    "test_package를 읽어왔습니다."
)  # main.py 파일로 패키지를 읽어올 때 __init__.py를 가장 먼저 실행

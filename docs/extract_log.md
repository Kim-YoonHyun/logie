
# extract_log

Python 파일 내의 `#` + `@log:` 주석에서 로그 메시지를 추출하는 함수.

파일을 읽어서 `#` + `@log:` 로 시작하는 주석의 내용만 리스트로 반환한다.
개발 중 작업 로그를 수집하거나 문서화할 때 유용하다.
이하 예시에서는 이 문서 내부의 주석을 추출하지 않기 위해서 `# + @log:` 로 표시한다.

## Parameters

| 입력변수    | type  | default |
| ----------- | ----- | ------- |
| `file_path` | `str` | -       |

## return

| 출력 type | 설명                               |
| --------- | ---------------------------------- |
| `list`    | 추출된 로그 메시지 문자열 리스트   |

## 사용예시

```python
import logie.docsutils as du

# Python 파일에서 로그 추출
logs = du.extract_log("/project/src/main.py")
print(logs)
"""
['사용자 인증 함수 추가', '로그인 API 구현', '세션 관리 기능 추가']
"""
```

```python
# 원본 파일 예시 (main.py)
"""
# + @log: 사용자 인증 함수 추가
def authenticate(user):
    pass

# 이것은 일반 주석입니다
# + @log: 로그인 API 구현
def login(username, password):
    pass

# @done_log: 이미 완료된 작업
def completed_function():
    pass

# + @log: 세션 관리 기능 추가
class SessionManager:
    pass
"""

# 추출 실행
logs = du.extract_log("/project/main.py")
print(logs)
# ['사용자 인증 함수 추가', '로그인 API 구현', '세션 관리 기능 추가']
```

```python
# 여러 파일에서 로그 수집
import os
import logie.docsutils as du

all_logs = []
src_path = "/project/src"

for root, dirs, files in os.walk(src_path):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            logs = du.extract_log(file_path)
            for log in logs:
                all_logs.append(f"{file}: {log}")

print("\n".join(all_logs))
"""
main.py: 사용자 인증 함수 추가
main.py: 로그인 API 구현
utils.py: 유틸리티 함수 리팩토링
auth.py: 권한 검증 로직 추가
"""
```

## Parameters detail

> `file_path` | type : `str`
>
> 로그를 추출할 Python 파일의 절대경로.
> UTF-8 인코딩된 텍스트 파일이어야 한다.
>
> 추출 규칙:
> - `# log:` 로 시작하는 주석 라인만 대상
> - 콜론(`:`) 뒤의 내용만 추출 (앞뒤 공백 제거)
> - 빈 메시지는 무시됨
> - `@done_log`, 일반 주석 등은 추출되지 않음
> - 파일 읽기 실패시 빈 리스트 반환
>
> ```python
> # 추출되는 예시
> "# log: 새 기능 추가" -> "새 기능 추가"
> "# log:    공백이 많은 메시지   " -> "공백이 많은 메시지"
>
> # 추출되지 않는 예시
> "# @done_log: 완료된 작업" -> @log가 아니므로 무시
> "# 일반 주석" -> @log가 아니므로 무시
>
> # 에러 처리
> du.extract_log("/nonexistent/file.py")  # []
> du.extract_log("/binary/file.dat")      # []
> ```

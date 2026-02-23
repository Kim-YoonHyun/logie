
# log2donelog

Python 파일 내의 `#` + `@log:` 주석을 `# @done_log:` 또는 `# [version] @done_log:` 로 변환하는 함수.

개발 중 작업 로그를 추적하다가 작업이 완료되면 완료 표시로 전환할 때 사용한다.
원본 파일은 수정하지 않고 .tmp 파일을 생성한다.
이 문서의 주석을 추출하지 않기 위해 이하 예시에서는 `# + @log:` 로 표시한다.
실제 사용시에는 + 가 아닌 단순 띄어쓰기로 붙여 쓰면 된다.

## Parameters

| 입력변수    | type  | default |
| ----------- | ----- | ------- |
| `file_path` | `str` | -       |
| `version`   | `str` | `None`  |

## return

| 출력 type | 설명        |
| --------- | ----------- |
| `None`    | 반환값 없음 |

## 사용예시

```python
import logie.docsutils as du

# 버전 없이 변환
du.log2donelog("/project/src/main.py")
# 결과: main.py.tmp 파일 생성
# # + @log: 함수 추가" -> "# @done_log: 함수 추가"

# 버전과 함께 변환
du.log2donelog("/project/src/utils.py", version="1.2.0")
# 결과: utils.py.tmp 파일 생성
# "# + @log: 버그 수정" -> "# [1.2.0] @done_log: 버그 수정"
```

```python
# 원본 파일 예시
"""
# + @log: 사용자 인증 함수 추가
def authenticate(user):
    pass

# + @log: 로그인 API 구현
def login(username, password):
    pass
"""

# 변환 실행
du.log2donelog("/project/auth.py", version="2.0.0")

# 생성된 auth.py.tmp 내용
"""
# [2.0.0] @done_log: 사용자 인증 함수 추가
def authenticate(user):
    pass

# [2.0.0] @done_log: 로그인 API 구현
def login(username, password):
    pass
"""
```

```python
# 여러 파일 일괄 변환
import os
import logie.docsutils as du

version = "1.5.0"
src_path = "/project/src"

for root, dirs, files in os.walk(src_path):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            du.log2donelog(file_path, version=version)

# 모든 Python 파일의 @log 가 @done_log 로 변환됨
```

## Parameters detail

> `file_path` | type : `str`
>
> 로그를 추출할 파일의 절대경로.
> 파일의 확장자는 상관없으며, 파일 내부의 `# + @log:` 패턴을 찾아 변환한다.
>
> - 원본 파일은 수정되지 않음
> - `{file_path}.tmp` 파일이 생성됨
> - 디렉토리 경로가 입력되면 IsADirectoryError 로 무시됨

> `version` | type : `str` | default : `None`
>
> 완료된 작업의 버전 번호.
> None 이 아닌 경우 `[version]` 형태로 버전 정보가 추가된다.
>
> - None: `# + @log:` → `# @done_log:`
> - "1.0.0": `# + @log:` → `# [1.0.0] @done_log:`
>
> - 다른 주석이나 코드는 영향받지 않음
> 
> ```python
> # version=None 인 경우
>du.log2donelog("/file.py")
> # "# + @log: 새 기능" -> "# @done_log: 새 기능"
> 
> # version 지정한 경우
> du.log2donelog("/file.py", version="2.1.0")
># "# + @log: 새 기능" -> "# [2.1.0] @done_log: 새 기능"
> 
> # 일반 주석은 영향받지 않음
> # "# 일반 주석" -> "# 일반 주석" (변화 없음)
># "# @done_log: 이미 완료" -> "# @done_log: 이미 완료" (변화 없음)
> ```

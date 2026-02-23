
# delete_tmp

지정된 경로 내의 모든 .tmp 파일을 삭제하는 함수.

사용자에게 확인을 요청한 후, 동의하면 모든 .tmp 파일을 영구적으로 삭제한다.
임시 파일이 더 이상 필요하지 않을 때 정리 용도로 사용한다.

## Parameters

| 입력변수 | type  | default |
| -------- | ----- | ------- |
| `path`   | `str` | -       |

## return

| 출력 type | 설명        |
| --------- | ----------- |
| `None`    | 반환값 없음 |

## 사용예시

```python
import logie.docsutils as du

# 프로젝트 경로의 모든 .tmp 파일 삭제
du.delete_tmp("/path/to/project")
"""
.tmp 를 남기시겠습니까 삭제하시겠습니까?
0: 남김, 1: 삭제
"""
# 사용자가 1 입력시
# "생성된 모든 .tmp 파일을 삭제합니다." 출력
# 모든 .tmp 파일이 영구 삭제됨

# 사용자가 0 입력시
# "tmp 파일을 보존합니다." 출력
# 아무것도 삭제되지 않음
```

```python
# 임시 파일 검토 후 정리
import logie.docsutils as du

# 1. @log 변환 작업으로 .tmp 파일 생성
du.log2donelog("/project/src/main.py")

# 2. 검토 후 불필요한 .tmp 파일 삭제
du.delete_tmp("/project/src")
```

## Parameters detail

> `path` | type : `str`
>
> .tmp 파일을 검색하고 삭제할 대상 디렉토리의 절대경로.
> 해당 경로 내의 모든 하위 디렉토리를 재귀적으로 순회하여 .tmp 파일을 찾는다.
>
> - 사용자에게 확인을 요청하는 대화형 프롬프트가 표시됨
> - 1 입력시: 모든 .tmp 파일이 영구적으로 삭제됨 (복구 불가능)
> - 0 입력시: .tmp 파일이 보존됨
> - 삭제는 os.remove() 를 사용하여 수행됨
>
> ```python
> # 예시: 프로젝트 전체의 임시 파일 정리
> du.delete_tmp("/my/project")
>
> # 특정 폴더만 정리
> du.delete_tmp("/my/project/tests")
>
> # 주의: 삭제는 영구적이므로 신중하게 사용
> # .tmp 파일을 남겨야 하는 경우 프롬프트에서 0을 입력
> ```

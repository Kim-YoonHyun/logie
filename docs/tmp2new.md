
# tmp2new

지정된 경로 내의 모든 .tmp 파일을 원본 파일로 교체하는 함수.

사용자에게 확인을 요청한 후, 동의하면 모든 .tmp 파일의 확장자를 제거하여 원본 파일로 덮어씌운다.
코드 수정 작업 후 임시 파일을 일괄 적용할 때 유용하다.

## Parameters

| 입력변수 | type  | default |
| -------- | ----- | ------- |
| `path`   | `str` | -       |

## return

| 출력 type | 설명                                    |
| --------- | --------------------------------------- |
| `int`     | 0: 취소됨, 1: 진행됨                    |

## 사용예시

```python
import logie.docsutils as du

# 프로젝트 경로의 모든 .tmp 파일을 원본으로 교체
result = du.tmp2new("/path/to/project")
"""
모든 .tmp 파일을 원본으로 적용하시겠습니까?
0: 취소, 1: 진행
"""
# 사용자가 1 입력시
# /path/to/project/file.py.tmp -> /path/to/project/file.py 로 교체
# 결과: result = 1

# 사용자가 0 입력시
# 아무것도 변경되지 않음
# 결과: result = 0
```

```python
# log2donelog 함수와 함께 사용하는 경우
import logie.docsutils as du

# 1. @log 를 @done_log 로 변환 (모든 파일에 .tmp 생성)
du.log2donelog("/project/src/main.py", version="1.0.0")

# 2. 생성된 .tmp 파일들을 원본으로 일괄 적용
du.tmp2new("/project/src")
```

## Parameters detail

> `path` | type : `str`
>
> .tmp 파일을 검색하고 교체할 대상 디렉토리의 절대경로.
> 해당 경로 내의 모든 하위 디렉토리를 재귀적으로 순회하여 .tmp 파일을 찾는다.
>
> - 사용자에게 확인을 요청하는 대화형 프롬프트가 표시됨
> - 1 입력시: 모든 .tmp 파일이 원본 파일로 교체됨 (기존 파일 덮어씌움)
> - 0 입력시: 아무 변경도 일어나지 않음
> - 교체된 파일마다 "{파일경로} 저장되었습니다. (.tmp 삭제)" 메시지 출력
>
> ```python
> # 예시: 프로젝트 전체의 임시 파일 적용
> du.tmp2new("/my/project")
>
> # 특정 폴더만 적용
> du.tmp2new("/my/project/src")
>
> # 반환값으로 사용자 선택 확인 가능
> if du.tmp2new("/project") == 1:
>     print("파일들이 성공적으로 적용되었습니다.")
> else:
>     print("작업이 취소되었습니다.")
> ```


# documenting

버전 관리를 위한 문서(README 등)에 변경 이력을 자동으로 추가하는 함수.

날짜, 버전, 태그, 요약, 상세 내용을 포함한 형식화된 로그 항목을 생성하고,
지정된 문서 파일에 추가한다. 기본적으로 .tmp 파일을 생성하여 안전하게 작업한다.

## Parameters

| 입력변수       | type   | default       |
| -------------- | ------ | ------------- |
| `tag`          | `str`  | -             |
| `summary`      | `str`  | -             |
| `version`      | `str`  | -             |
| `log_contents` | `str`  | -             |
| `docs_path`    | `str`  | -             |
| `docs_name`    | `str`  | `"README.md"` |
| `overwrite`    | `bool` | `False`       |

## return

| 출력 type | 설명                                          |
| --------- | --------------------------------------------- |
| `str`     | 생성된 로그 항목 문자열 (overwrite=False 시) |

## 사용예시

```python
import logie.docsutils as du

# 기본 사용 - README.md.tmp 파일 생성
tag = "Feature"
summary = "사용자 인증 기능 추가"
version = "1.2.0"
log_contents = """
- 로그인 API 엔드포인트 추가
- JWT 토큰 인증 구현
- 사용자 세션 관리 기능
"""

log_entry = du.documenting(
    tag=tag,
    summary=summary,
    version=version,
    log_contents=log_contents,
    docs_path="/project/docs"
)

print(log_entry)
"""

## 2026-02-23 Version 1.2.0
**Tag:** @Feature<br>
**Summary:** 사용자 인증 기능 추가<br>
**Detail:**<br>

- 로그인 API 엔드포인트 추가
- JWT 토큰 인증 구현
- 사용자 세션 관리 기능
"""
```

```python
# 다른 문서 파일 사용
du.documenting(
    tag="Patch",
    summary="버그 수정",
    version="1.2.1",
    log_contents="- 로그인 에러 수정\n- 세션 만료 처리 개선",
    docs_path="/project/docs",
    docs_name="CHANGELOG.md"
)
# CHANGELOG.md.tmp 파일이 생성됨
```

```python
# 주의: overwrite=True 사용
du.documenting(
    tag="Release",
    summary="정식 출시",
    version="2.0.0",
    log_contents="- 메이저 버전 출시",
    docs_path="/project",
    overwrite=True
)
"""
⚠️ 덮어씌우기 인자가 활성화 되어 .tmp 없이 기존 파일 README.md 에 바로 변경이 적용됩니다. 진행하시겠습니까?
0:미진행 1:진행
"""
# 1 입력시 README.md 에 직접 추가됨 (.tmp 없음)
```

## Parameters detail

> `tag` | type : `str`
>
> 변경 사항의 유형을 나타내는 태그.
> 예: "Feature", "Patch", "Refactoring", "Major-Release" 등

> `summary` | type : `str`
>
> 변경 사항의 간단한 요약 설명.
> 한 줄로 주요 변경 내용을 설명한다.

> `version` | type : `str`
>
> 해당 변경이 적용된 버전 번호.
> semantic versioning 형식 권장 (예: "1.2.3")

> `log_contents` | type : `str`
>
> 변경 사항의 상세 내용.
> 여러 줄의 텍스트로 구체적인 변경 사항을 나열한다.
> 보통 마크다운 리스트 형식으로 작성한다.

> `docs_path` | type : `str`
>
> 문서 파일이 위치한 디렉토리의 절대경로.
> 이 경로에 docs_name 파일이 존재하거나 생성될 위치.

> `docs_name` | type : `str` | default : `"README.md"`
>
> 로그를 추가할 문서 파일명.
> 기본값은 "README.md" 이며, CHANGELOG.md 등 다른 파일도 지정 가능.

> `overwrite` | type : `bool` | default : `False`
>
> 원본 파일에 직접 쓸지 여부.
> - False (기본값): .tmp 파일을 생성하여 안전하게 작업
> - True: 원본 파일에 직접 추가 (확인 프롬프트 표시)
>
> ```python
> # 안전한 방식 (권장)
> du.documenting(..., overwrite=False)  # .tmp 파일 생성
>
> # 직접 적용 (주의 필요)
> du.documenting(..., overwrite=True)   # 원본 파일 변경
> ```
>
> 생성되는 로그 항목 형식:
> ```
> ## YYYY-MM-DD Version X.Y.Z
> **Tag:** @TagName<br>
> **Summary:** 요약 내용<br>
> **Detail:**<br>
> 상세 내용
> ```

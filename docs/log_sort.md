
# log_sort

변수 중 `rollover` 의 값을 `True` 로 한 경우 생성되는 이전 날짜 로그파일들에 대해서 새로운 디렉토리를 생성해 정리하는 함수.

{저장한 로그경로}_history 라는 새로운 폴더가 생성되고, 내부에 년, 월로 구분되어 이전 날짜의 로그가 정리된다.

수백개 이상의 로그 파일이 생성되어 로그에 대한 가시적인 구분이 어려운 경우, 로그 기록에 대한 체계적인 정리가 필요한 경우 활용 가능하다.

## Parameters

| 입력변수   | type  | default |
| ---------- | ----- | ------- |
| `log_path` | `str` | `None`  |

## return

| 출력 type             | 설명                         |
| --------------------- | ---------------------------- |
| logger 파일 저장 트리 | 날짜에 따라 생성된 폴더 트리 |

## 사용예시

```python
log_path = './log'
lu.log_sort(log_path)
```

## Parameters detail

> `log_path` | type : `str` | default : `None`
>
> 저장된 .log 파일의 날짜별 log 파일이 기록된 경로. 
>
> 기본값은 `None` 으로 되어있으며 자동으로 `작업디렉토리/log` 로 설정된다.
>
> 만약 구분할 log 파일이 없어도 구분만 되지 않을 뿐 정상 작동한다.
>
> ```python
> lu.log_sort()
> ```
>
> ```python
> '''
> ./log/app.log
> ./log/app.log.20250722
> ./log/error.log
> ./log/error.log.20250722
> ./log/info.log 
> ./log/info.log.20250722
> '''
> 
> -->
> 
> '''
> ./log/app.log
> ./log/error.log
> ./log/info.log 
> 
> ./log_history/2025/07/app.log.20250722
> ./log_history/2025/07/error.log.20250722
> ./log_history/2025/07/info.log.20250722
> '''
> ```

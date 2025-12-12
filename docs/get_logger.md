# get_logger

로그 수준의 `INFO` 보다 높은 수준을 전부 기록하는 전체 로그파일과 `INFO` 수준만을 기록하는 `info.log`, `error` 수준만을 기록하는 `error.log` 를 생성하는 함수. 모든 생성되는 로그파일에 있어서 `INFO` 보다 낮은 수준(`DEBUG`)은 기록하지 않는다.

## parameters

| 입력변수   | type   | default |
| ---------- | ------ | ------- |
| `log_path` | `str`  | `None`  |
| `log_name` | `str`  | `'app'` |
| `display`  | `bool` | `True`  |
| `rollover` | `bool` | `True`  |

## return

| 출력 type | 설명                                 |
| --------- | ------------------------------------ |
| logger    | logging 가능한 log 변수 및 .log 파일 |

## 사용예시

```python
import logie as lo
log = lo.get_logger()
# log = lu.get_logger(
#     log_path='./log',
#     log_name='whole', 
#     rollover=True
# )

log.debug("DEBUG 메시지입니다.")	# DEBUG 수준의 에러 로그는 기록되지 않는다.
log.info("INFO 메시지입니다.")
log.warning("WARNING 메시지입니다.")
log.error("ERROR 메시지입니다.")
log.critical("CRITICAL 메시지입니다.")
```

생성되는 모든 로그파일의 내부에는 [날짜 시간] [에러 코드],[라인 번호] [실행파일명] [로그 수준] [내용] 순으로 기록 된다. 

```
'''
작업디렉토리에 log 폴더 생성
app.log
2025-07-22 16:55:07,485 level:INFO test.py line 160 INFO 메시지입니다.
2025-07-22 16:55:07,485 level:WARNING test.py line 161 WARNING 메시지입니다.
2025-07-22 16:55:07,485 level:ERROR test.py line 162 ERROR 메시지입니다.
2025-07-22 16:55:07,485 level:CRITICAL test.py line 163 CRITICAL 메시지입니다.

error.log
2025-07-22 16:55:07,485 level:ERROR test.py line 162 ERROR 메시지입니다.

info.log
2025-07-22 16:55:07,485 level:INFO test.py line 160 INFO 메시지입니다.
'''
```
## Parameters detail

> `log_path`  | type : `str` | default : `None`
>
> .log 파일을 생성할 경로값을 입력한다. 이때 log 의 이름은 포함하지 않는다.
>
> 기본값은 `None` 으로 되어있으며 경로를 별도 설정하지 않는 경우 자동으로 `작업디렉토리/log` 로 설정된다.


> `log_name` | type : `str` | default : `'app'`
>
> .log 파일을 생성할때 만들어지는 전체 로그파일의 이름. 설정하지 않는 경우 app.log 가 자동 생성된다.
>
> 이 이름과는 별개로 info.log, error.log 가 자동으로 저장된다.

> `display` | type: `bool` | default : `True`
>
> log 메시지를 terminal 등의 콘솔 화면에 print 와 동일한 형태로 출력할지 여부.
>
> 기본적으로 True 로 설정되어있으며 만약 출력을 원하지 않는 경우 False 를 해두어야 한다.


> `rollover` | type : `bool` | default : `True`
>
> 날짜가 넘어가면 그 전에 생성된 에러 로그 파일을 새로운 파일로 저장할 지 여부를 정하는 기능.
>
> `True` 시 다음날짜로 넘어간 다음 로그 파일을 새로 생성하면 이전 파일은 파일명 제일 뒤에 해당 년월일이 생기면서 새로운 파일로 저장된다.
>
> ```
> # 2025년 7월 22일에 로그 생성
> # 경로는 ./log
> app.log
> error.log
> info.log
> 
> # 2025년 7월 23일에 로그 생성
> # 경로는 ./log
> app.log	# 오늘(7월 23일)의 로그 데이터
> app.log.20250722  # 어제(7월 22일)의 로그는 따로 분리됨
> error.log
> error.log.20250722 # 어제(7월 22일)의 로그는 따로 분리됨
> info.log 
> info.log.20250722 # 어제(7월 22일)의 로그는 따로 분리됨
> ```

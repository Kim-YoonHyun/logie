


## 2026-02-02 Version 0.1.0
**Tag:** @Feature<br>
**Summary:** 문서 관련 기능 추가<br>
**Detail:**<br>
- Modified: /home/kimyh/library/logie/src/logie/docsutils/docsutils.py
 - 함수 `tmp2new` 추가
 - 함수 `tmp2new` 에 정말로 실행할 것인지 여부 묻는 부분 추가
 - 함수 `delete_tmp` 추가
 - 기본적인 README 기록 형태를 제공하는 함수 `documenting` 추가
 - 함수 `documenting` 내부에 README.md.tmp 파일 생성 추가
 - 함수 `documenting` 에 덮어씌우기 인자 `overwrite` 추가
 - 함수 `documenting` 에 출력 값에 줄바꿈인자를 포함
 - 함수 `log2donelog` 에서 version 변수에 대한 입력 여부 결정 추가
 - `extract_logs_from_file` 의 함수명을 `extract_log` 로 변경
- New: /home/kimyh/library/logie/src/logie/utils/__init__.py
- New: /home/kimyh/library/logie/src/logie/utils/utils.py



## 2026-02-02 Version 0.1.1
**Tag:** @Patch<br>
**Summary:** import 오류 수정<br>
**Detail:**<br>
- Modified: /home/kimyh/library/logie/src/logie/docsutils/docsutils.py

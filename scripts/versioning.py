import sys
import os
import re
import json
import textwrap
import semver

# @log: toml_base 추가
toml_base = {
    # 빌드 시스템 의존성 정의 (패키지를 빌드하기 위해 필요한 것들)
    "[build-system]":{ 
        "requires" : '["setuptools>=61.0", "wheel"]',
        "build-backend" : "setuptools.build_meta"
    },
    "[project]":{
        # 패키지 이름 (pip install 시 사용될 이름)
        "name" : "logie",
        # 버전
        "version" : "0.2.0", 
        # 패키지 설명 (짧은 설명)
        "description" : "로그 활용 패키지", 
        # 긴 설명 (README.md 사용)
        "readme" : '{file = "README.md", content-type = "text/markdown"}', 
        # 최소 지원할 파이썬 버전
        "requires-python" : ">=3.7", 
        # 작성자 정보
        "authors" : '[{name = "kimyh", email = "kim_yh663927@naver.com"}]', 
        # 설치 시 같이 설치될 의존성 목록
        # 예시: "pandas>=1.3.0,<2.0.0"  # 버전 범위 설정 방법
        "dependencies" : ''' [
    # "torch==2.7.0",
    # "torchaudio==2.7.0",
    # "torchvision==0.22.0",
    # "pandas==2.2.3",
    # "tqdm==4.67.1"
]''',   
        # 패키지의 메타데이터
        "classifiers" :'''[  
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",   # MIT 대학 이름에서 유래한 자유 라이선스
    "Operating System :: OS Independent"
]'''
    },
    "[tool.setuptools]":{ 
        # 패키지 내 데이터 파일 포함 설정
        "include-package-data" : "true" 
    },
    "[tool.setuptools.packages.find]":{
        # find_packages() 와 동일하게 현재 디렉토리 기준 자동 검색
        "where" : '["."]', 
        # @log: bin, scripts 를 제외목록에 추가
        # 필요 시 제외할 패키지 지정 가능
        "exclude" : '["test/", "scripts/"]' 
    },
    # 특정 패키지에 포함할 정적 파일 지정 (globbing 지원)
    "[tool.setuptools.package-data]":{  
        # "mypackage" : '["*.pyc", "dir1/temp.json"]',
        # "mypackage.module1" : '["temp.json"]'
    }
}


def main():
    depend_list = [
        "semver>=3.0.4"
    ]
    scripts_path = os.path.dirname(os.path.abspath(__file__))
    pack_path = os.path.dirname(scripts_path)
    pack_name = os.path.basename(pack_path)

    with open(os.path.join(pack_path, "pyproject.toml"), "r", encoding="utf-8-sig") as f:
        sentence = f.readlines()
    
    new_sentence_list = []
    d_flag = 0
    for s in sentence:
        # 새 버전 적용
        if "version" in s:
            sys.path.append(pack_path)
            from logie.logutils.sourceutils import version_up
            pattern = r'"([^"]*)"'
            ver = re.findall(pattern, s)[0]
            new_ver, tag = version_up("a", ver)
            new_s = f'version = "{new_ver}"\n'
        # 새로운 패키지 리스트
        elif "dependencies" in s:
            d_flag = 1
            new_s = s
            continue
        elif d_flag == 1:
            if "]" in s:
                for depend in depend_list:
                    new_s += f"  {depend}\n"
                new_s += s
                d_flag = 0
            else:
                continue
        # 그 외 내용
        else:
            new_s = s

        new_sentence_list.append(new_s)
        
    
    for ns in new_sentence_list:
        print(ns)

    sys.path.append(pack_path)
    from logie.logutils.sourceutils import extract_logs_from_file
    # a = extract_logs_from_file(os.path.join(pack_path, pack_name))
    # print(a)
        




if __name__ == "__main__":
    main()
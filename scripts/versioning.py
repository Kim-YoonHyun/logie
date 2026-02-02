import sys
import os
import re
import json
import textwrap
import semver

import toml




def main():
    depend_list = [
        "semver>=3.0.4"
    ]
    scripts_path = os.path.dirname(os.path.abspath(__file__))
    pack_path = os.path.dirname(scripts_path)
    pack_name = os.path.basename(pack_path)

    with open(os.path.join(pack_path, "pyproject.toml"), "r", encoding="utf-8") as f:
        toml_info = toml.load(f)

    now_version = toml_info["project"]['version']

    
    print(now_version)
    sys.exit()
    
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
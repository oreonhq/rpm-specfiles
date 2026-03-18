#!/usr/bin/python3


FILE_TEMPLATE='''summary: Fonts related tests
discover:
  how: fmf
  url: https://src.fedoraproject.org/tests/fonts
prepare:
  name: tmt
  how: install
  package: {packagename}
execute:
  how: tmt
environment:
  PACKAGE: {packagename}
  FONT_ALIAS: {fontalias}
  FONT_FAMILY: {fontfamily}
  FONT_LANG: {fontlang}
'''


# file name, package name, font alias, font family, font lang
FILE_CONTENTS = [
    ("google-noto-sans-cjk-fonts-jp.fmf", "google-noto-sans-cjk-fonts", "sans-serif", "Noto Sans CJK JP", "ja"),
    ("google-noto-sans-cjk-fonts-mono-jp.fmf", "google-noto-sans-cjk-fonts", "monospace", "Noto Sans Mono CJK JP", "ja"),
    ("google-noto-sans-cjk-fonts-kr.fmf", "google-noto-sans-cjk-fonts", "sans-serif", "Noto Sans CJK KR", "ko"),
    ("google-noto-sans-cjk-fonts-mono-kr.fmf", "google-noto-sans-cjk-fonts", "monospace", "Noto Sans Mono CJK KR", "ko"),
    ("google-noto-sans-cjk-fonts-sc.fmf", "google-noto-sans-cjk-fonts", "sans-serif", "Noto Sans CJK SC", "zh-cn"),
    ("google-noto-sans-cjk-fonts-mono-sc.fmf", "google-noto-sans-cjk-fonts", "monospace", "Noto Sans Mono CJK SC", "zh-cn"),
    ("google-noto-sans-cjk-fonts-tc.fmf", "google-noto-sans-cjk-fonts", "sans-serif", "Noto Sans CJK TC", "zh-tw"),
    ("google-noto-sans-cjk-fonts-mono-tc.fmf", "google-noto-sans-cjk-fonts", "monospace", "Noto Sans Mono CJK TC", "zh-tw"),
    ("google-noto-sans-cjk-fonts-hk.fmf", "google-noto-sans-cjk-fonts", "sans-serif", "Noto Sans CJK HK", "zh-hk"),
    ("google-noto-sans-cjk-fonts-mono-hk.fmf", "google-noto-sans-cjk-fonts", "monospace", "Noto Sans Mono CJK HK", "zh-hk"),
]

def gen_plan_files():
    for item in FILE_CONTENTS:
        file_name = item[0]
        font_alias = item[2]
        plan_content = FILE_TEMPLATE.format(packagename=item[1], fontalias=font_alias, fontfamily=item[3], fontlang=item[4])
        with open(file_name, "w") as f:
            f.write(plan_content)
            if font_alias == "sans-serif":
                f.write("  DEFAULT_SANS: 1\n")
            if font_alias == "monospace":
                f.write("  DEFAULT_MONO: 1\n")
                f.write("  FONT_EXCLUDE: (Black|DemiLight|Light|Medium|Thin)\n")
            if font_alias == "serif":
                f.write("  DEFAULT_SERIF: 1\n")


if __name__ == "__main__":
    gen_plan_files()

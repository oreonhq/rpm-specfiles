# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 7898cfb54156cc0d8a2f2c00d5645c573ff367d03d29085bb495966d99d2529e
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# SPDX-License-Identifier: MIT

Epoch:   1
Version: 2.003
Release: 4%{?dist}
URL:     https://github.com/googlefonts/noto-cjk

BuildRequires:            python3

%global foundry           Google
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE

%global fontfamily        Noto Serif CJK VF
%global fontsummary       Google Noto Serif CJK Variable Fonts
%global fonts             *.ttc
%global fontconfs         65-0-%{fontpkgname}.conf %{SOURCE10}
%global fontdescription   %{expand:
Noto CJK fonts, supporting Simplified Chinese, Traditional Chinese, \
Japanese, and Korean. The supported scripts are Han, Hiragana, Katakana, \
Hangul, and Bopomofo. Latin, Greek, Cyrllic, and various symbols are also \
supported for compatibility with CJK standards.

The google-noto-serif-cjk-vf-fonts package contains Google Noto Serif CJK Variable fonts.
}

Source0:  https://github.com/googlefonts/noto-cjk/releases/download/Serif%{version}/02_NotoSerifCJK-OTF-VF.zip
Source1:  genfontconf.py
Source10: 65-%{fontpkgname}.conf

%global obsoletes_epoch_version_release 0:20201206-8

%global obsoletes_pkg()\
%define subpkgname %1\
Obsoletes:      %{subpkgname} < %{obsoletes_epoch_version_release}\
Provides:       %{subpkgname} = %{epoch}:%{version}-%{release}\

%global obsoletes_serif()\
%define langname %1\
%obsoletes_pkg google-noto-serif-cjk-%{langname}-fonts\
%obsoletes_pkg google-noto-serif-%{langname}-fonts\

%global fontpkgheader     %{expand:

%obsoletes_pkg google-noto-serif-cjk-ttc-fonts

%obsoletes_serif sc
%obsoletes_serif tc
%obsoletes_serif jp
%obsoletes_serif kr

}

%fontpkg

%prep
%oreon_verify_sources
%autosetup -c

cp -p Variable/OTC/NotoSerifCJK-VF.otf.ttc NotoSerifCJK-VF.ttc

cp %{SOURCE1} .

python3 genfontconf.py "ja" "serif" "Noto Serif CJK JP" \
        "ko" "serif" "Noto Serif CJK KR" \
        "zh-cn:zh-sg" "serif" "Noto Serif CJK SC" \
        "zh-tw:cmn:hak:lzh:nan" "serif" "Noto Serif CJK TC" \
        "zh-hk:zh-mo:yue" "serif" "Noto Serif CJK HK" \
    | xmllint --format - |tee 65-0-google-noto-serif-cjk-vf-fonts.conf


%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.003-4
- Prepare for Oreon 11 (RP1)

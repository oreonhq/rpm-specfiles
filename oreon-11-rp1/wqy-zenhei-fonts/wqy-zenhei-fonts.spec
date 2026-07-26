%global source0_hash 00e75d03af47fa3bf79a0fba2da93711c6c89a9313c8873ab1145a5fa3f845d0

# SPDX-License-Identifier: MIT

%global fontname wqy-zenhei

Version: 0.9.46
Release: 35%{?dist}
URL:     http://wenq.org/wqy2/index.cgi?ZenHei(en)

%global foundry           WQY
%global fontlicense       GPL-2.0-only WITH Font-exception-2.0
%global fontlicenses      COPYING
%global fontdocs          AUTHORS ChangeLog README

%global fontfamily        ZenHei
%global fontsummary       WenQuanYi Zen Hei CJK Font
%global fonts             *.ttc
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
WenQuanYi Zen Hei is a Hei-Ti style (sans-serif type) Chinese \
outline font. It is designed for general purpose text formatting \
and on-screen display of Chinese characters and symbols from \
many other languages. The embolden strokes of the font glyphs \
produces enhanced screen contrast, making it easier to read \
recognize. The embedded bitmap glyphs further enhance on-screen \
performance, which can be enabled with the provided configuration \
files. WenQuanYi Zen Hei provides a rather complete coverage to \
Chinese Hanzi glyphs, including both simplified and traditional \
forms. The total glyph number in this font is over 35,000, including \
over 21,000 Chinese Hanzi. This font has full coverage to GBK(CP936) \
charset, CJK Unified Ideographs, as well as the code-points \
needed for zh_cn, zh_sg, zh_tw, zh_hk, zh_mo, ja (Japanese) \
and ko (Korean) locales for fontconfig. Starting from version \
0.8, this font package has contained two font families, i.e. \
the proportionally-spaced Zen Hei, and a mono-spaced face \
named "WenQuanYi Zen Hei Mono".
}

Source0:  http://downloads.sourceforge.net/wqy/%{fontname}-%{version}-May.tar.bz2
Source10: 66-%{fontpkgname}.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{fontname}
%linuxtext -e GB18030 AUTHORS
%linuxtext -e ISO-8859-1 README

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog

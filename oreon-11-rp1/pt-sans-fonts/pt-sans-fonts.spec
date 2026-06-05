%global source0_hash 2758cf7a872827f39661cf8cc24188113c030447aefb5ca7145993650076ca8c
%global source1_hash 9cc831490532009bae2b3ce0d39c62adfc889060beb421593bfd9d2396d0f10a
%global source2_hash 3128bd5ecf01816e59a23d54c57a7a6b14615b07db53ff277c77376010265b05
%global source3_hash 5a90fe2d0cd798700935240580bdcc12c0ffc9102c0c7163b3418e13bc21debd
%global source4_hash 81ac221cdd02bccfa679c74adb122478e9d092e65a722e31ca11469961483785

# SPDX-License-Identifier: MIT
Version: 20141121
Release: 32%{?dist}
# https://company.paratype.com/pt-sans-pt-serif
URL:     http://www.paratype.com/public/

%global foundry           PT
%global fontlicense       OFL-1.1
%global fontlicenses      PTSSM_OFL.txt

%global fontfamily        PT Sans
%global fontsummary       PT Sans, a grotesque pan-Cyrillic font family
%global fontpkgheader     %{expand:
Obsoletes: paratype-pt-sans-fonts         <= %{version}-%{release}
Obsoletes: paratype-pt-sans-caption-fonts <= %{version}-%{release}

}
%global fonts             PT_Sans-Web-*.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
The PT Sans family was developed as part of the “Public Types of Russian
Federation” project. This project aims at enabling the peoples of Russia to
read and write their native languages, using free/libre fonts. It is
dedicated to the 300-year anniversary of the Russian civil type invented by
Peter the Great from 1708 to 1710, and was realized with financial support
from the Russian Federal Agency for Press and Mass Communications.

The fonts include support for all 54 ethnic languages of the Russian
Federation as well as more common Western, Central European and Cyrillic
blocks making them unique and a very important tool for modern digital
communications.

PT Sans is a grotesque font family based on Russian type designs of the second
part of the 20th century. However, it also includes very distinctive features
of modern humanistic design, fulfilling present day aesthetic and functional
requirements.

It was designed by Alexandra Korolkova, Olga Umpeleva and Vladimir Yefimov
and released by ParaType.}

Source0:  https://raw.githubusercontent.com/google/fonts/main/ofl/ptsans/OFL.txt
Source1:  https://raw.githubusercontent.com/google/fonts/main/ofl/ptsans/PT_Sans-Web-Regular.ttf
Source2:  https://raw.githubusercontent.com/google/fonts/main/ofl/ptsans/PT_Sans-Web-Bold.ttf
Source3:  https://raw.githubusercontent.com/google/fonts/main/ofl/ptsans/PT_Sans-Web-Italic.ttf
Source4:  https://raw.githubusercontent.com/google/fonts/main/ofl/ptsans/PT_Sans-Web-BoldItalic.ttf
Source10: 58-pt-sans-fonts.xml

%fontpkg


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
test "%{source4_hash}" = "none" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source4_hash}" || { echo "oreon: Source4 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T
install -m 0644 -vp %{SOURCE0} PTSSM_OFL.txt
install -m 0644 -vp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20141121-32
- Import

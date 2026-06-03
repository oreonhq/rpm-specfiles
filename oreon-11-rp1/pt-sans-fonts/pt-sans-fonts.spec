%global source21_hash dda0eb0c4c876b7be5fd3732fbf909600e852aabefd84b6d759a2ae8554c3bc4
%global source20_hash dda0eb0c4c876b7be5fd3732fbf909600e852aabefd84b6d759a2ae8554c3bc4
%global source0_hash 9c53ad6b9759208b6c8ee726cc939dabf97ea6f610c8308ceea0b9b954b410c3

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
%global fonts             PTS*.ttf PTN*.ttf PTC*.ttf
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

# This is now dead and ParaType still publishes an older version on its website
Source0:  http://www.fontstock.com/public/PTSansOFL.zip
Source10: 58-pt-sans-fonts.xml
Source20: http://rus.paratype.ru/system/attachments/647/original/ptsans55reg.pdf
Source21: http://rus.paratype.ru/system/attachments/650/original/ptsans75bold.pdf
Source22: http://rus.paratype.ru/system/attachments/648/original/ptsans56it.pdf
Source23: http://rus.paratype.ru/system/attachments/651/original/ptsans76bit.pdf
Source24: http://rus.paratype.ru/system/attachments/652/original/ptsanscaption55.pdf
Source25: http://rus.paratype.ru/system/attachments/653/original/ptsanscaption57bold.pdf
Source26: http://rus.paratype.ru/system/attachments/649/original/ptsans57narrow.pdf
Source27: http://rus.paratype.ru/system/attachments/655/original/ptsans77narrowbold.pdf

%fontpkg

%package doc
Summary:   Optional documentation files of %{source_name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{source_name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c
%linuxtext *.txt
install -m 0644 -vp %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} \
                    %{SOURCE24} %{SOURCE25} %{SOURCE26} %{SOURCE27} .

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license PTSSM_OFL.txt
%doc *.pdf

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20141121-32
- Import

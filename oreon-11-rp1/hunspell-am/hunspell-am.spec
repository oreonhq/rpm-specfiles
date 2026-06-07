%global source0_hash c6abf8b090c390257637433dfb4f3190eea4131d5c469f8774cf023e395b0a10

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-am
Summary: Amharic hunspell dictionaries
%global upstreamid 20090704
Version: 0.%{upstreamid}
Release: 33%{?dist}
URL: http://www.cs.ru.nl/~biniam/geez/index.php
License: GPL-1.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-am)

Source0:        https://www.cs.ru.nl/~biniam/geez/dict/am_ET.zip

%description
Amharic hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n am_ET

%build
tr -d '\r' < README.txt > README.txt.new
touch -r README.txt README.txt.new
mv -f README.txt.new README.txt

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p am_ET.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/

%files
%doc README.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-33
- Prepare for Oreon 11 (RP1)

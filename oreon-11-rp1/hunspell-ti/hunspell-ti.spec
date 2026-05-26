%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ti
Summary: Tigrigna hunspell dictionaries
%global upstreamid 20090911
Version: 0.%{upstreamid}
Release: 32%{?dist}
Source: http://www.cs.ru.nl/~biniam/geez/dict/ti_ER.zip
# oreon url source checksums begin
%global source0_sha256 81880aa7ab2ae91603ab5cfd5b02f1afa1cbac97f17154f9e8a5bf13f0491733
%global source0_file ti_ER.zip
# oreon url source checksums end
URL: http://www.cs.ru.nl/~biniam/geez/index.php
License: GPL-1.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ti)

%description
Tigrigna hunspell dictionaries.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ti_ER.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "81880aa7ab2ae91603ab5cfd5b02f1afa1cbac97f17154f9e8a5bf13f0491733" || { echo "oreon: Source0 SHA256 mismatch for ti_ER.zip" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -c

%build
tr -d '\r' < README.txt > README.txt.new
touch -r README.txt README.txt.new
mv -f README.txt.new README.txt

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p ti_ER.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
ti_ER_aliases="ti_ET"
for lang in $ti_ER_aliases; do
        ln -s ti_ER.aff $lang.aff
        ln -s ti_ER.dic $lang.dic
done


%files
%doc README.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-32
- Prepare for Oreon 11 (RP1)

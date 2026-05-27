%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || 0%{?oreon}
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-tet
Summary: Tetum hunspell dictionaries
%global upstreamid 20050108
Version: 0.%{upstreamid}
Release: 37%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/tet_ID.zip
URL: http://borel.slu.edu/crubadan/apps.html
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-tet)

%description
Tetum hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -c

%build
for i in README_tet_ID.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p tet_ID.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
tet_ID_aliases="tet_TL"
for lang in $tet_ID_aliases; do
        ln -s tet_ID.aff $lang.aff
        ln -s tet_ID.dic $lang.dic
done
popd


%files
%doc README_tet_ID.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20050108-37
- Import

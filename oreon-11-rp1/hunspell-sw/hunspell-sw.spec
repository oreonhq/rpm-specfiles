%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || 0%{?oreon}
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-sw
Summary: Swahili hunspell dictionaries
%global upstreamid 20050819
Version: 0.%{upstreamid}
Release: 36%{?dist}
# Following link is not working and is dead
# do not report any bugs for this
Source: http://www.it46.se/downloads/openoffice/dictionary/dictionary_myspell_sw_TZ_1.1.tar.gz
URL: http://www.it46.se
License: LGPL-2.1-or-later
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-sw)

%description
Swahili hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c

%build
for i in README_sw_TZ.txt; do
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
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
sw_TZ_aliases="sw_KE"
for lang in $sw_TZ_aliases; do
        ln -s sw_TZ.aff $lang.aff
        ln -s sw_TZ.dic $lang.dic
done
popd


%files
%doc README_sw_TZ.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20050819-36
- Import

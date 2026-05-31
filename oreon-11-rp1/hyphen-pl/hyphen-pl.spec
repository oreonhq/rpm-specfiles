%global source0_hash 03c167c60aeb5b7ee0c8314a7c42ace7e183acacd4613c52a6bd5ee02975cc28

Name: hyphen-pl
Summary: Polish hyphenation rules
%global upstreamid 20060726
Version: 0.%{upstreamid}
Release: 35%{?dist}
Source:        http://download.services.openoffice.org/contrib/dictionaries/hyph_pl_PL.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-pl)

%description
Polish hyphenation rules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c -n hyphen-pl

%build
for i in README_hyph_pl_PL.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_pl_PL.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README_hyph_pl_PL.txt
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20060726-35
- Import

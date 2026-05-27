%global source0_hash none

Name: hyphen-fo
Summary: Faroese hyphenation rules
%global upstreamid 20040420
Version: 0.%{upstreamid}
Release: 31%{?dist}
Source: http://fo.speling.org/filer/hyph_fo_FO-20040420a.zip
URL: http://fo.speling.org/
License: GPL-1.0-or-later
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-fo)

%description
Faroese hyphenation rules.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -c

%build
for i in README_hyph_fo_FO.txt; do
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
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_fo_FO.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README_hyph_fo_FO.txt
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20040420-31
- Import

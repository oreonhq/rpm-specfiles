%global source0_hash 9ad8d1c3ab427508766eadc3f60902b79ddac3325a5c6ece8f3d82d6dc539c2f

Name: hyphen-is
Summary: Icelandic hyphenation rules
%global upstreamid 20030920
Version: 0.%{upstreamid}
Release: 37%{?dist}
Source:        http://download.services.openoffice.org/contrib/dictionaries/hyph_is_IS.zip
Patch0: hyphen-is-lppl-license-fix.patch
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPL-2.1-or-later OR SISSL
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-is)

%description
Icelandic hyphenation rules.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c

%build
chmod -x *
for i in README_hyph_is_IS.txt; do
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
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README_hyph_is_IS.txt
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20030920-37
- Import

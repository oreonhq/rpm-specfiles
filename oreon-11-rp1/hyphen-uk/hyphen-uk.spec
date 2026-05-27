%global source0_hash none

Name: hyphen-uk
Summary: Ukrainian hyphenation rules
%global upstreamid 20030903
Version: 0.%{upstreamid}
Release: 34%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/hyph_uk_UA.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-uk)

%description
Ukrainian hyphenation rules.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README_hyph_uk_UA.txt
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20030903-34
- Import

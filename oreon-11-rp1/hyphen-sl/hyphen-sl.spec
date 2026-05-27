%global source0_hash none

Name: hyphen-sl
Summary: Slovenian hyphenation rules
%global upstreamid 20070127
Version: 0.%{upstreamid}
Release: 34%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/hyph_sl_SI.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-sl)

%description
Slovenian hyphenation rules.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c -n hyphen-sl

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_sl_SI.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README_hyph_sl_SI.txt
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20070127-34
- Import

%global source0_hash 8f6db89fddbabe7f6ea3644f6dd55db6597251e9d4b06535fd9235685b0c3fb6

Name: hyphen-da
Summary: Danish hyphenation rules
%global upstreamid 20070903
Version: 0.%{upstreamid}
Release: 35%{?dist}
Source:        http://download.services.openoffice.org/contrib/dictionaries/hyph_da_DK.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
Patch0: hyphen-da-lppl-license-fix.patch
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-da)

%description
Danish hyphenation rules.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c -n hyphen-da
chmod -x *

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_da_DK.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README_hyph_da_DK.txt
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20070903-35
- Import

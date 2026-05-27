%global source0_hash none

Name: hyphen-ga
Summary: Irish hyphenation rules
%global upstreamid 20040220
Version: 0.%{upstreamid}
Release: 34%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/hyph_ga_IE.zip
URL: http://borel.slu.edu/fleiscin/index.html
License: GPL-1.0-or-later
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-ga)

%description
Irish hyphenation rules.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c -n hyphen-ga

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_ga_IE.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README_hyph_ga_IE.txt
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20040220-34
- Import

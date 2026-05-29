%global source0_hash 53e91005ca223a43ad66d8a88158dc4d34ee4f0db62fb46fa9eb02bb34d63c97

%if 0%{?fedora} > 35 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-rw
Summary: Kinyarwanda hunspell dictionaries
%global upstreamid 20050109
Version: 0.%{upstreamid}
Release: 35%{?dist}
Source:        rw_RW.zip
URL: http://borel.slu.edu/crubadan/apps.html
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-rw)

%description
Kinyarwanda hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c -n hunspell-rw

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p rw_RW.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/


%files
%doc README_rw_RW.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20050109-35
- Import

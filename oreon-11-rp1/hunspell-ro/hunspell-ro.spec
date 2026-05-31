%global source0_hash 7f128d64ea06c9e6711c30b118c0afeefb014d8f33c92daccdf455aba2d04519

%if 0%{?fedora} > 35
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-ro
Summary: Romanian hunspell dictionaries
Version: 3.3.10
Release: 11%{?dist}
Source:        http://downloads.sourceforge.net/rospell/ro_RO.%{version}.zip
URL: http://rospell.sourceforge.net/
License: GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-ro)

%description
Romanian hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p ro_RO.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc COPYING.GPL COPYING.LGPL COPYING.MPL README
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.10-11
- Prepare for Oreon 11 (RP1)

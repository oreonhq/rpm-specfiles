%global source0_hash fcc9ca2934a484207dd41386ef9ee9966433bf77ca15f362b77c40f8ae2acc34

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-kn
Summary: Kannada hunspell dictionaries
Version: 1.0.3
Release: 35%{?dist}
URL: https://extensions.openoffice.org/project/kannada
License: GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-kn)

Source0:        https://downloads.sourceforge.net/project/aoo-extensions/2628/1/kannada.oxt

%description
Kannada hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -n hunspell-kn

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p kn_IN.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/

%files
%doc README_kn_IN.txt
%license COPYING COPYING.MPL COPYING.GPL COPYING.LGPL
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.3-35
- Prepare for Oreon 11 (RP1)

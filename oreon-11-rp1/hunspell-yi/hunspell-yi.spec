%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-yi
Summary: Yiddish hunspell dictionaries
Version: 1.1
Release: 34%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/3975/1/%{name}-%{version}.oxt
URL: http://extensions.services.openoffice.org/en/project/dict-yi
License: LGPL-2.1-or-later OR GPL-2.0-or-later OR MPL-1.1
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-yi)

%description
Yiddish hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/yi.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/yi_US.aff
cp -p dictionaries/yi.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/yi_US.dic


%files
%doc README_yi.txt
%license gpl-2.0.txt MPL-1.1.txt LICENSES-en.txt HACKING lgpl-2.1.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-34
- Prepare for Oreon 11 (RP1)

%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-uk
Summary: Ukrainian hunspell dictionaries
Version: 6.6.1
Release: 2%{?dist}
Source:        https://github.com/brown-uk/dict_uk/releases/download/v6.6.1/dict-uk_UA-6.6.1.oxt
URL: https://github.com/brown-uk/dict_uk/
# license tag information obtained from README_uk_UA.txt file
License: MPL-1.1
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-uk)

%description
Ukrainian hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p uk_UA/uk_UA.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p uk_UA/uk_UA.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc uk_UA/README_uk_UA.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.1-2
- Prepare for Oreon 11 (RP1)

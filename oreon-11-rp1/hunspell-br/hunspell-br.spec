%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-br
Summary: Breton hunspell dictionaries
Epoch: 1
Version: 0.15
Release: 20%{?dist}
URL: http://www.drouizig.org/
Source: https://downloads.sourceforge.net/project/aoo-extensions/2207/7/dict-br-0.15.oxt
License: LGPL-2.1-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-br)

%description
Breton hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c -n hunspell-br-%{version}

%build
chmod -x dictionaries/*

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/br_FR.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc package-description.txt
%license LICENSES-en.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.15-20
- Prepare for Oreon 11 (RP1)

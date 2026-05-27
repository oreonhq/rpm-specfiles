%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-mt
Summary: Maltese hunspell dictionaries
%global upstreamid 20110414
Version: 0.%{upstreamid}
Release: 20%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/5039/0/dict-mt-2011-04-14.oxt
URL: https://extensions.openoffice.org/en/project/maltese-spell-check-dictionary
License: LGPL-2.1-or-later
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-mt)

%description
Maltese hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p mt.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/mt_MT.dic
cp -p mt.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/mt_MT.aff


%files
%doc README_en.txt
%license licence.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-20
- Prepare for Oreon 11 (RP1)

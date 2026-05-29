%global source0_hash none

%if 0%{?fedora} > 35 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-shs
Summary: Shuswap hunspell dictionaries
%global upstreamid 20090828
Version: 0.%{upstreamid}
Release: 32%{?dist}
Source: http://secpewt.sd73.bc.ca/hunspell/hunspell-shs-ca.tar.gz
URL: http://secpewt.sd73.bc.ca/wordlist
License: GPL-2.0-or-later
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell
Supplements: (hunspell and langpacks-shs)

%description
Shuswap hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p hunspell/shs_CA.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc hunspell/COPYING hunspell/Copyright hunspell/README
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20090828-32
- Import

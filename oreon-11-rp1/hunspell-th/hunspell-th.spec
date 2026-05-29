%global source0_hash 31bd2fb43bf879b272908fe7d8f68fe113a5523488905f01d74dd84451b50bf6

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-th
Summary: Thai hunspell dictionaries
%global upstreamid 20061212
Version: 0.%{upstreamid}
Release: 36%{?dist}
Source:        http://download.services.openoffice.org/contrib/dictionaries/th_TH.zip
URL: https://wiki.openoffice.org/wiki/Dictionaries
License: LGPL-2.1-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-th)

%description
Thai hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -c -n hunspell-th

%build
#set encoding to IANA prefered name
sed -i -e 's/TIS620-2533/TIS620/g' th_TH.aff
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc README_th_TH.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20061212-36
- Import

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ms
Summary: Malay hunspell dictionaries
%global upstreamid 20050117
Version: 0.%{upstreamid}
Release: 36%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/ms_MY.zip
URL: https://wiki.openoffice.org/wiki/Dictionaries
# affix file is under GPL+
# rest package under GFDL
License: GFDL-1.1-or-later AND GPL-1.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ms)

%description
Malay hunspell dictionaries.

%prep
%autosetup -c -n hunspell-ms

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
ms_MY_aliases="ms_BN"
for lang in $ms_MY_aliases; do
        ln -s ms_MY.aff $lang.aff
        ln -s ms_MY.dic $lang.dic
done


%files
%doc README_ms_MY.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-36
- Prepare for Oreon 11 (RP1)

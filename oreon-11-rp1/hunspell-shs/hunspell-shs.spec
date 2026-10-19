%global source0_hash none
%if 0%{?fedora} > 35 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-shs
Summary:        Shuswap hunspell dictionaries
%global upstreamid 20090828
Version: 0.%{upstreamid}
Release:        1%{?dist}
URL: http://secpewt.sd73.bc.ca/wordlist
License: GPL-2.0-or-later
BuildArch: noarch
Requires: hunspell
Supplements: (hunspell and langpacks-shs)
Source0:        shs_CA.aff
Source1:        shs_CA.dic
Source2:        COPYING
Source3:        Copyright
Source4:        README
# oreon:deps
BuildRequires:  hunspell-devel
# /oreon:deps
%description
Shuswap hunspell dictionaries.

%prep

%setup -q -c -T -n %{name}-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/shs_CA.aff
cp -p %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/shs_CA.dic
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20090828-32
- Import

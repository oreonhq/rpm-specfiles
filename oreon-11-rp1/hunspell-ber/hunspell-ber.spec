%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ber
Summary: Amazigh hunspell dictionaries
%global upstreamid 20080210
Version: 0.%{upstreamid}
Release: 34%{?dist}
Source: http://ayaspell.sourceforge.net/data/hunspell-am_test.tar.gz
URL: http://ayaspell.sourceforge.net/am.html
License: GPL-1.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ber)

%description
Amazigh hunspell dictionaries.

%prep
%setup -q -n spelling_tifinagh

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p tifinagh.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ber_MA.dic
cp -p tifinagh.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ber_MA.aff


%files
%doc README
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-34
- Prepare for Oreon 11 (RP1)

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-el
Summary: Greek hunspell dictionaries
Epoch: 1
Version: 0.9
Release: 20%{?dist}
Source: http://ispell.math.upatras.gr/files/ooffice/el_GR-%{version}.zip
URL: http://www.elspell.gr/
License: GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-el)

%description
Greek hunspell dictionaries.

%prep
%autosetup -c -n hunspell-el

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
el_GR_aliases="el_CY"
for lang in $el_GR_aliases; do
        ln -s el_GR.aff $lang.aff
        ln -s el_GR.dic $lang.dic
done


%files
%doc README_el_GR.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9-20
- Prepare for Oreon 11 (RP1)

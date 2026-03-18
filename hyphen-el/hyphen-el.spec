Name: hyphen-el
Summary: Greek hyphenation rules
%global upstreamid 20051018
Version: 0.%{upstreamid}
Release: 35%{?dist}
Source:  http://download.services.openoffice.org/contrib/dictionaries/hyph_el_GR.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPL-2.1-or-later
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-el)

%description
Greek hyphenation rules.

%prep
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
el_GR_aliases="el_CY"
for lang in $el_GR_aliases; do
        ln -s hyph_el_GR.dic hyph_$lang.dic
done


%files
%doc README_hyph_el_GR.txt
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-35
- Prepare for Oreon 11 (RP1)

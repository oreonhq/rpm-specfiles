%if 0%{?fedora} > 35
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-om
Summary: Oromo hunspell dictionaries
Epoch: 1
Version: 0.04
Release: 34%{?dist}
# Following links are dead now
# Please don't report any bugs for it
Source: http://borel.slu.edu/obair/%{name}-%{version}.oxt
URL: http://borel.slu.edu/crubadan/apps.html
License: GPL-3.0-or-later
BuildArch: noarch
Requires: hunspell
Supplements: (hunspell and langpacks-om)

%description
Oromo hunspell dictionaries.

%prep
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/om_ET.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
om_ET_aliases="om_KE"
for lang in $om_ET_aliases; do
        ln -s om_ET.aff $lang.aff
        ln -s om_ET.dic $lang.dic
done


%files
%doc dictionaries/README_om_ET.txt
%license LICENSES-en.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.04-34
- Prepare for Oreon 11 (RP1)

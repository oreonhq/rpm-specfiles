%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-mi
Summary: Maori hunspell dictionaries
%global upstreamid 20080630
Version: 0.%{upstreamid}
Release: 35%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/mi_NZ.zip
URL: https://wiki.openoffice.org/wiki/Dictionaries
License: GPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-mi)

%description
Maori hunspell dictionaries.

%prep
%autosetup -c -n hunspell-mi-%{version}

%build
for i in README_mi_NZ.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p mi_NZ.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/mi_NZ.aff
cp -p mi_NZ.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/mi_NZ.dic


%files
%doc README_mi_NZ.txt
%license LICENSE_mi_NZ.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-35
- Prepare for Oreon 11 (RP1)

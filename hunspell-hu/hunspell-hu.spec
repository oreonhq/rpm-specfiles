%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-hu
Summary: Hungarian hunspell dictionaries
Version: 1.9
Release: 1%{?dist}
Source0: https://github.com/LibreOffice/dictionaries/raw/refs/heads/master/hu_HU/hu_HU.dic
Source1: https://github.com/LibreOffice/dictionaries/raw/refs/heads/master/hu_HU/hu_HU.aff
URL: http://magyarispell.sourceforge.net
# License information extracted from hu_HU.aff file
License: LGPL-2.1-or-later OR GPL-2.0-or-later OR MPL-1.1

BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-hu)

%description
Hungarian hunspell dictionaries.

%prep
%autosetup -c -T

%build
# nothing to build here

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
cp -p %{SOURCE0} %{SOURCE1} %{buildroot}%{_datadir}/%{dict_dirname}


%files
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9-1
- Prepare for Oreon 11 (RP1)

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-bn
Summary: Bengali hunspell dictionaries
Version: 1.0.0
Release: 29%{?dist}
Epoch: 1
Source: http://anishpatil.fedorapeople.org/bn_in.%{version}.tar.gz
URL: https://gitorious.org/hunspell_dictionaries/hunspell_dictionaries.git
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-bn)

%description
Bengali hunspell dictionaries.

%prep
%autosetup -c -n bn_IN
# fix file permissions
chmod 644 bn_IN/*

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p bn_IN/*.dic bn_IN/*.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
bn_IN_aliases="bn_BD"
for lang in ${bn_IN_aliases}; do
    ln -s bn_IN.aff $lang.aff
    ln -s bn_IN.dic $lang.dic
done
popd


%files
%doc bn_IN/README
%license bn_IN/COPYING bn_IN/Copyright
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0-29
- Prepare for Oreon 11 (RP1)

%global source0_hash none

%if 0%{?fedora} > 35 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-smj
Summary: Lule Saami hunspell dictionaries
Version: 1.0
Release: 0.33.beta7%{?dist}
URL: http://www.divvun.no/index.html
License: GPL-3.0-only
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-smj)

# upstream http://divvun.no/static_files/hunspell-smj.tar.gz is dead
Source0:        smj.aff
Source1:        smj.dic
Source2:        README
Source3:        Copyright
Source4:        GPL-3

%description
Lule Saami hunspell dictionaries.

%prep
%setup -q -c -T -n %{name}-1.0beta7.20090316

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/smj_NO.aff
cp -p %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/smj_NO.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
smj_NO_aliases="smj_SE"
for lang in $smj_NO_aliases; do
        ln -s smj_NO.aff $lang.aff
        ln -s smj_NO.dic $lang.dic
done
popd

%files
%doc %{SOURCE2} %{SOURCE3} %{SOURCE4}
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-0.33.beta7
- Import

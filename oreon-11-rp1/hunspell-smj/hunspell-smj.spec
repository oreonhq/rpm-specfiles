%if 0%{?fedora} > 35 || 0%{?oreon}
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-smj
Summary: Lule Saami hunspell dictionaries
Version: 1.0
Release: 0.33.beta7%{?dist}
Source: http://divvun.no/static_files/hunspell-smj.tar.gz
URL: http://www.divvun.no/index.html
License: GPL-3.0-only
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-smj)

%description
Lule Saami hunspell dictionaries.

%prep
%setup -q -n %{name}-1.0beta7.20090316

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p smj.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/smj_NO.aff
cp -p smj.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/smj_NO.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
smj_NO_aliases="smj_SE"
for lang in $smj_NO_aliases; do
        ln -s smj_NO.aff $lang.aff
        ln -s smj_NO.dic $lang.dic
done


%files
%doc Copyright README GPL-3
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-0.33.beta7
- Import

%if 0%{?fedora} > 35
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-se
Summary: Northern Saami hunspell dictionaries
Version: 1.0
Release: 0.33.beta7%{?dist}
Source: http://divvun.no/static_files/hunspell-se.tar.gz
URL: http://www.divvun.no/index.html
License: GPL-3.0-only
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-se)

%description
Northern Saami hunspell dictionaries.

%prep
%setup -q -n %{name}-1.0beta7.20090316

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p se.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/se_NO.aff
cp -p se.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/se_NO.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
se_NO_aliases="se_SE se_FI"
for lang in $se_NO_aliases; do
        ln -s se_NO.aff $lang.aff
        ln -s se_NO.dic $lang.dic
done


%files
%doc Copyright README GPL-3
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-0.33.beta7
- Prepare for Oreon 11 (RP1)

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-af
Summary: Afrikaans hunspell dictionary
%global upstreamid 20080825
Version: 0.%{upstreamid}
Release: 35%{?dist}
# Following URL is dead now
Source: http://downloads.translate.org.za/spellchecker/afrikaans/myspell-af_ZA-0.%{upstreamid}.zip
URL: http://www.translate.org.za/
License: LGPL-2.1-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-af)

%description
Afrikaans hunspell dictionary

%prep
%setup -q -c -n hunspell-af_ZA

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
af_ZA_aliases="af_NA"
for lang in $af_ZA_aliases; do
        ln -s af_ZA.aff $lang.aff
        ln -s af_ZA.dic $lang.dic
done
popd


%files
%doc README_af_ZA.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-35
- Prepare for Oreon 11 (RP1)

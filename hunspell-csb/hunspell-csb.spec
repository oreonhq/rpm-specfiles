%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-csb
Summary: Kashubian hunspell dictionaries
# We are using here upstreamid date as upstream published source archive date
%global upstreamid 20190319
Version: 0.%{upstreamid}
Release: 8%{?dist}
Source: https://addons.thunderbird.net/firefox/downloads/latest/kashubian-spell-checker-poland/addon-222511-latest.xpi
URL: https://addons.thunderbird.net/en-us/firefox/addon/kashubian-spell-checker-poland/
License: GPL-2.0-only
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-csb)

%description
Kashubian hunspell dictionaries.

%prep
%autosetup -c %{name}-%{version}

%build
# nothing here to build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/Kaszebsczi.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/csb_PL.dic
cp -p dictionaries/Kaszebsczi.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/csb_PL.aff


%files
%doc dictionaries/Copyright
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-8
- Prepare for Oreon 11 (RP1)

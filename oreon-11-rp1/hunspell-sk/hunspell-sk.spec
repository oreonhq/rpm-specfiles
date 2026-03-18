%if 0%{?fedora} > 35
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-sk
Summary: Slovak hunspell dictionaries
Epoch: 1
%global upstreamid 20110228
Version: 0.%{upstreamid}
Release: 31%{?dist}
Source: http://www.sk-spell.sk.cx/files/hunspell-sk-%{upstreamid}.zip
URL: http://www.sk-spell.sk.cx/
License: LGPL-2.1-only OR GPL-2.0-only OR MPL-1.1
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-sk)

%description
Slovak hunspell dictionaries.

%prep
%setup -q -n %{name}-%{upstreamid}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc doc/*
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-31
- Prepare for Oreon 11 (RP1)

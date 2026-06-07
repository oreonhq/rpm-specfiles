%global source0_hash none

Name: hyphen-mi
Summary: Maori hyphenation rules
%global upstreamid 20080630
Version: 0.%{upstreamid}
Release: 34%{?dist}
Source0: mi.dic
Source1: mi.LICENSE
Source2: mi.README
URL: http://papakupu.maori.nz/
License: GPL-3.0-or-later
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-mi)

%description
Maori hyphenation rules.

%prep
%setup -q -c -T -n hyphen-mi-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_mi_NZ.dic

%files
%doc %{SOURCE1} %{SOURCE2}
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20080630-34
- Import

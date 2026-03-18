Name: hyphen-hu
Summary: Hungarian hyphenation rules
%global upstreamid 20090612
Version: 0.%{upstreamid}
Release: 37%{?dist}
# Source URL is dead now
# Source: http://download.github.com/nagybence-huhyphn-aa3fc85.tar.gz
Source: nagybence-huhyphn-aa3fc85.tar.gz
URL: http://www.tipogral.hu/
License: GPL-2.0-only
BuildArch: noarch
BuildRequires: make
Requires: hyphen
Supplements: (hyphen and langpacks-hu)

%description
Hungarian hyphenation rules.

%prep
%setup -q -n nagybence-huhyphn-aa3fc85
#disable for now as built-in patgen has too small a limit to rebuild
#ln -sf /usr/bin/patgen patgen
#touch words/*.txt

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_hu.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_hu_HU.dic


%files
%doc README doc/huhyphn.pdf
%license gpl.txt
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-37
- Prepare for Oreon 11 (RP1)

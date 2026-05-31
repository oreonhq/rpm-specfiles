%global source0_hash e2db16201e32c38fd02346d3f59a99ff559487c7afbd3843d1ff6203aaa57ae3

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20090612-37
- Import

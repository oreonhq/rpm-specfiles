Name: hyphen-ro
Summary: Romanian hyphenation rules
Version: 3.3.6
Release: 31%{?dist}
Source: http://downloads.sourceforge.net/rospell/hyph_ro_RO.3.3.6.zip
# oreon url source checksums begin
%global source0_sha256 80a7bd5abd2a0339272ce4e2be897ae7bc4458292e762cf5f9ca9cc641b2b381
%global source0_file hyph_ro_RO.3.3.6.zip
# oreon url source checksums end
URL: http://rospell.sourceforge.net/
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-ro)

%description
Romanian hyphenation rules.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/hyph_ro_RO.3.3.6.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "80a7bd5abd2a0339272ce4e2be897ae7bc4458292e762cf5f9ca9cc641b2b381" || { echo "oreon: Source0 SHA256 mismatch for hyph_ro_RO.3.3.6.zip" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/


%files
%doc COPYING.GPL README          
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.6-31
- Prepare for Oreon 11 (RP1)

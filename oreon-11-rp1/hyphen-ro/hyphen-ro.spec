# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 80a7bd5abd2a0339272ce4e2be897ae7bc4458292e762cf5f9ca9cc641b2b381
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name: hyphen-ro
Summary: Romanian hyphenation rules
Version: 3.3.6
Release: 31%{?dist}
Source: http://downloads.sourceforge.net/rospell/hyph_ro_RO.3.3.6.zip
URL: http://rospell.sourceforge.net/
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-ro)

%description
Romanian hyphenation rules.

%prep
%oreon_verify_sources
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

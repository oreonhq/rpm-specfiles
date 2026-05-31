%global source0_hash ed8148c37bdd5d4fa612f584529933cb79b5c69666d9e8515c07c0b4af79e424

Name: hyphen-id
Summary: Indonesian hyphenation rules
%global upstreamid 20040812
Version: 0.%{upstreamid}
Release: 34%{?dist}
Source:        http://download.services.openoffice.org/contrib/dictionaries/hyph_id_ID.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: GPL-1.0-or-later
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-id)

%description
Indonesian hyphenation rules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README_id_ID.txt
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20040812-34
- Import

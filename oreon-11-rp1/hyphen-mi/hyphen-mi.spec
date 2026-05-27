%global source0_hash none

Name: hyphen-mi
Summary: Maori hyphenation rules
%global upstreamid 20080630
Version: 0.%{upstreamid}
Release: 34%{?dist}
# Source is dead now
# Source: http://packages.papakupu.maori.nz/hunspell-hyphen/hunspell-hyphen-mi-0.1.%%{upstreamid}-beta.tar.gz
Source: hunspell-hyphen-mi-0.1.%{upstreamid}-beta.tar.gz
URL: http://papakupu.maori.nz/
License: GPL-3.0-or-later
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-mi)

%description
Maori hyphenation rules.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p mi.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_mi_NZ.dic


%files
%doc mi.LICENSE mi.README
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20080630-34
- Import

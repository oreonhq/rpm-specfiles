%global source0_hash 6c18a97d16343ea611c4a270f65295b462a6b795b1cac638fc3a6af630c0f7e4

Name: mythes-ne
Summary: Nepali thesaurus
Version: 1.1
Release: 32%{?dist}
Source0:        thes_ne_NP_v2.zip
URL: https://wiki.openoffice.org/wiki/Dictionaries
License: LGPL-2.0-or-later
BuildArch: noarch
BuildRequires: mythes-devel
Requires: mythes
Supplements: (mythes and langpacks-ne)

%description
Nepali thesaurus.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_ne_NP_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes/


%files
%doc README_th_ne_NP_v2.txt
%{_datadir}/mythes/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-32
- Import

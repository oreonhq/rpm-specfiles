%global source0_hash none

%if 0%{?fedora} > 35 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-qu
Summary: Quechua Ecuador hunspell dictionaries
Version: 0.9
Release: 32%{?dist}
# Following links is dead now
Source: http://extensions.services.openoffice.org/e-files/2121/8/qu_EC-0.9.oxt
URL: http://extensions.services.openoffice.org/project/KichwaSpellchecker
License: AGPL-3.0-only
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-qu)

%description
Quechua Ecuador hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p qu_EC.aff qu_EC.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc CURRENTVERSION.txt README.txt REVISION.txt
%license LICENSE.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9-32
- Import

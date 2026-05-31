%global source0_hash none

%if 0%{?fedora} > 35
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-sv
Summary: Swedish hunspell dictionaries
Version: 2.42
Release: 2%{?dist}
Source: https://extensions.libreoffice.org/assets/downloads/z/ooo-swedish-dict-2-42.oxt
URL: https://extensions.libreoffice.org/en/extensions/show/swedish-spelling-dictionary-den-stora-svenska-ordlistan
License: LGPL-3.0-only
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-sv)

%description
Swedish hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c -n hunspell-sv

%build
sed -i 's/\r$//' LICENSE_sv_SE.txt
sed -i 's/\r$//' LICENSE_en_US.txt

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/*.dic dictionaries/*.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc LICENSE_sv_SE.txt LICENSE_en_US.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.42-2
- Prepare for Oreon 11 (RP1)

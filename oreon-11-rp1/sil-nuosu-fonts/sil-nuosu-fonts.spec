%global source0_hash bba1007767f995ab652af49b94b50419a6b2e3595b0c7c9324d063c4f6c2e7da

# SPDX-License-Identifier: MIT

Version: 2.200
Release: 14%{?dist}
URL:     http://scripts.sil.org/SILYi_home

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          README.txt FONTLOG.txt

%global fontfamily        Nuosu SIL
%global fontsummary       The Nuosu SIL Font
%global fonts             NuosuSIL-Regular.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
The Nuosu SIL Font is a single Unicode font for the standardized Yi script used by a large ethnic group in southwestern China.
}

Source0:        https://github.com/silnrsi/font-nuosu/releases/download/v%{version}/NuosuSIL-%{version}.tar.xz
Source10: 66-sil-nuosu-fonts.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n NuosuSIL-%{version}
%linuxtext OFL.txt FONTLOG.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.200-14
- Prepare for Oreon 11 (RP1)

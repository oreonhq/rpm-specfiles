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

Source0:  https://github.com/silnrsi/font-nuosu/releases/download/v%{version}/NuosuSIL-%{version}.tar.xz
Source10: 66-sil-nuosu-fonts.conf
# oreon url source checksums begin
%global source0_sha256 bba1007767f995ab652af49b94b50419a6b2e3595b0c7c9324d063c4f6c2e7da
%global source0_file NuosuSIL-2.200.tar.xz
# oreon url source checksums end

%fontpkg

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/NuosuSIL-2.200.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bba1007767f995ab652af49b94b50419a6b2e3595b0c7c9324d063c4f6c2e7da" || { echo "oreon: Source0 SHA256 mismatch for NuosuSIL-2.200.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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

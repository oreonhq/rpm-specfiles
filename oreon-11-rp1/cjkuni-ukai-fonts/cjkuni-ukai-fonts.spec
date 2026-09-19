%global source0_hash b4968d73519f4f8747e85548fb85d21b665da1bf1ba900a7c499976e6a8ae3d2

# SPDX-License-Identifier: MIT

%define catalogue        %{_sysconfdir}/X11/fontpath.d

Version: 0.2.20080216.2
Release: 10%{?dist}
URL:     http://www.freedesktop.org/wiki/Software/CJKUnifonts

%global foundry           CJKUni
%global fontlicense       Arphic-1999

%global fontlicenses      license
%global fontdocs          CONTRIBUTERS FONTLOG KNOWN_ISSUES NEWS README TODO

%global fontfamily        UKai
%global fontsummary       Chinese Unicode TrueType font in Kai face

%global fonts             ukai.ttc
%global fontconfs         %{SOURCE10} %{SOURCE11}

%global fontdescription   %{expand:
CJK Unifonts are Unicode TrueType fonts derived from original fonts made \
available by Arphic Technology under "Arphic Public License" and extended by \
the CJK Unifonts project.

CJK Unifonts in Kai face.}

Source0:  http://deb.debian.org/debian/pool/main/f/fonts-arphic-ukai/fonts-arphic-ukai_%{version}.orig.tar.bz2
Source10: 65-%{fontpkgname}.conf
Source11: 90-%{fontpkgname}-embolden.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n fonts-arphic-ukai-%{version}

%build
%fontbuild

%install
%fontinstall

# catalogue
install -m 0755 -d %{buildroot}%{catalogue}
ln -s %{fontdir}/ %{buildroot}%{catalogue}/%{name}

%check
%fontcheck

%fontfiles
%{catalogue}/%{name}

%changelog
%autochangelog

%global source0_hash e3c19e04ea7a565b4acff6f1e4248084d2e10752e305bf7dd6c76e80860dc1db

# SPDX-License-Identifier: MIT

%global catalogue        %{_sysconfdir}/X11/fontpath.d

Version: 0.2.20080216.2
Release: 10%{?dist}
URL:     http://www.freedesktop.org/wiki/Software/CJKUnifonts

%global foundry           CJKUni
%global fontlicense       Arphic-1999
%global fontlicenses      license
%global fontdocs          CONTRIBUTERS FONTLOG KNOWN_ISSUES NEWS README

%global fontfamily        UMing
%global fontsummary       Chinese Unicode TrueType font in Ming face
%global fonts             uming.ttc

%global fontconfs         %{SOURCE10} %{SOURCE11}
%global fontdescription   %{expand:
CJK Unifonts are Unicode TrueType fonts derived from original fonts made \
available by Arphic Technology under "Arphic Public License" and extended by \
the CJK Unifonts project.

CJK Unifonts in Ming face.}

Source0:  http://deb.debian.org/debian/pool/main/f/fonts-arphic-uming/fonts-arphic-uming_%{version}.orig.tar.bz2
Source10: 65-%{fontpkgname}.conf
Source11: 90-%{fontpkgname}-embolden.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ttf-arphic-uming-%{version}
rm -rf license/.svn license/*/.svn

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

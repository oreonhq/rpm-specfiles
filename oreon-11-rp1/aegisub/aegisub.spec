%global source0_hash 10d0810429cd91b0483990fbad7d45b2ae8d799b034f2a40b731ace7f2ae4325
%global         altname         Aegisub
Name:           aegisub
Version:        3.4.2
Release:        1%{?dist}
Summary:        Tool for creating and modifying subtitles
License:        BSD-3-Clause AND ISC AND MIT
URL:            https://github.com/TypesettingTools/%{name}
Source0:        https://github.com/TypesettingTools/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch1:         0001-fix-Fallback-to-X11-if-lacks-EGL-support.patch
Requires: hicolor-icon-theme
ExcludeArch: ppc64le s390x
Provides: bundled(cajun-jsonapi) = 2.0.1
Provides: bundled(lua-lpeg) = 0.1.0
Provides: bundled(lua-luabins) = 0.3
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  libglvnd-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ffms2)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
Aegisub is an advanced subtitle editor which assists in the creation of
subtitles, timing, and editing of subtitle files. It supports a wide range
of formats and provides powerful visual typesetting tools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{altname}-%{version} -p1

# Strip out unused bundled library
find subprojects/ -mindepth 1 -depth ! -path "subprojects/luabins*" -exec rm -rv {} +
# Bundled: src/gl/glext.h (Provided by `libglvnd-devel`, unable to patch out due to upstream cross-platform modification)
# Strip unused packaging artifacts for other platform, which contains GPL code
rm -rv packages/{osx_bundle,osx_dmg,win_installer}
rm -rv tools/{osx-*,apply-manifest.py,*.ps1}
rm -rv osx-bundle.sed
# ./docs consists of project related document and tools, but not application manual
rm -rv docs/

%build

%meson -Denable_update_checker=false
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

%meson_test
%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/org.%{name}.%{altname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.%{name}.%{altname}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

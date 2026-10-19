%global source0_hash cbad15f9a16edd4c068ce14fb17f39cdb811dab0135fca80fafffa9a45732aec
%global appname CorsixTH
%global uuid    com.corsixth.%{appname}
%global forgeurl https://github.com/CorsixTH/CorsixTH
%global tag v%{version}
Name:           corsix-th
Version:        0.70.1
%forgemeta
Release:        1%{?dist}
Summary:        Open source clone of Theme Hospital
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{tag}/%{appname}-%{version}.tar.gz
Requires:       %{name}-data
Requires:       hicolor-icon-theme
Requires:       lua-filesystem
Requires:       lua-lpeg
Recommends:     fluid-soundfont-lite-patches
Recommends:     innoextract
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  lua-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(sdl2)
# /oreon:deps
%description

%package        data
Summary:        Data files for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description    data

Package contains data files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%cmake \
    -G Ninja \
    -DWITH_MOVIES=0 \
    %{nil}
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_datadir}/%{name}/LICENSE.txt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n corsix-th-data -f %{oreon_filedir}/corsix-th-data.list

%changelog

%autochangelog

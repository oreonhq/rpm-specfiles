%global source0_hash 29f0be1a15ecce658e647b8c3d3fe2e6acddf6fa2144b1e05c82984846f568a1
Name: fheroes2
Version: 1.1.17
Release:        1%{?dist}
Summary:        Free implementation of the popular game engine
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://github.com/ihhub/fheroes2
VCS: git:%{url}.git
Source0:        https://github.com/ihhub/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1: %{name}.autodlrc
Source2: %{name}.sh
Requires: autodownloader
Requires: hicolor-icon-theme
Requires: unzip
Provides: bundled(libsmacker) = 1.2.0
# oreon:deps
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_net-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  libpng-devel
BuildRequires:  make
# /oreon:deps
%description
This open source multiplatform project, written from scratch, is designed to
reproduce the original game with significant improvements in gameplay, graphics
and logic (including support for high-resolution graphics, improved AI,
numerous fixes and user interface improvements), breathing new life into one of
the most addictive turn-based strategy games.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
    -DFHEROES2_DATA="%{_datadir}/%{name}" \
    -DUSE_SDL_VERSION=SDL2 \
    -DENABLE_IMAGE=ON
%cmake_build
cd docs
FHEROES2_DATA=%{_datadir}/%{name}/data make
cd -
%install
%cmake_install
install -D -p -m 0644 docs/%{name}.6 %{buildroot}%{_mandir}/man6/%{name}.6
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}/%{name}.autodlrc
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}.bin
install -Dpm 0755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}
rm -f  %{buildroot}%{_docdir}/%{name}/LICENSE
rm -f  %{buildroot}%{_docdir}/%{name}/README.txt
rm -f  %{buildroot}%{_docdir}/%{name}/changelog.txt
rm -f  %{buildroot}%{_docdir}/%{name}/demo/download_demo_version.sh
rm -f  %{buildroot}%{_docdir}/%{name}/homm2/extract_homm2_resources.sh
rm -d  %{buildroot}%{_docdir}/%{name}/demo/
rm -d  %{buildroot}%{_docdir}/%{name}/homm2/
mkdir -p %{buildroot}%{_datadir}/%{name}/{anim,data,lang,maps}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

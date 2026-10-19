%global source0_hash 82357dd546d6614b4bc76a0b143a211e4475d009cabd48166dae12bb2712f1a8
Name:           tuxanci
Version:        0.21.0
Release:        1%{?dist}
Summary:        First Tux shooter multi-player network game
License:        GPL-1.0-or-later
Source0:        http://download.tuxanci.org/tuxanci-0.21.0.tar.bz2
Source1:        tuxanci.desktop
Source2:        tuxanci.appdata.xml
Source3:        screenshot.png
Patch1:         0001-SDLmain-is-no-more.patch
Patch2:         0002-dlopen-is-used-outside-server-too.patch
Patch3:         0003-Unbreak-DLIB_INSTALL_DIR.patch
Patch4:         0004-Make-the-icon-square.patch
Patch5:         tuxanci-0.21.0-Do-not-install-LICENSE.patch
Patch6:         tuxanci-0.21.0-Unbundle-fonts.patch
Patch7:         tuxanci-0.21.0-Port-to-ISO-C23.patch
Patch8:         tuxanci-0.21.0-Adapt-to-CMake-4.0.patch
Requires:       font(dejavusans)
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  zziplib-devel
# /oreon:deps
%description
Tuxanci is a first Tux shooter game supporting single player and multi-player
modes both on a single computer and over the network.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DCMAKE_FONT=%{_datadir}/fonts/dejavu-sans-fonts/DejaVuSans.ttf
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{scalable,48x48}/apps
install -pm644 data/tuxanci.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
convert -geometry 48x48 -depth 8 -background none data/tuxanci.svg \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/tuxanci.png
ln -s tuxanci-%{version} %{buildroot}%{_bindir}/tuxanci
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/appdata/
install -pm644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/appdata/tuxanci.appdata.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

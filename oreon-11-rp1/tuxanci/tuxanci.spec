%global source0_hash 82357dd546d6614b4bc76a0b143a211e4475d009cabd48166dae12bb2712f1a8

Name:           tuxanci
Version:        0.21.0
Release:        29%{?dist}
Summary:        First Tux shooter multi-player network game
# LICENCE:      GPLv2 text
## unused
# data/font/DejaVuSans.ttf: Bitstream Vera and Public Domain
License:        GPL-1.0-or-later
Source0:        http://download.tuxanci.org/tuxanci-0.21.0.tar.bz2
Source1:        tuxanci.desktop
Source2:        tuxanci.appdata.xml
# The screenshot URL is linked from tuxanci.appdata.xml
Source3:        screenshot.png
Patch1:         0001-SDLmain-is-no-more.patch
Patch2:         0002-dlopen-is-used-outside-server-too.patch
Patch3:         0003-Unbreak-DLIB_INSTALL_DIR.patch
Patch4:         0004-Make-the-icon-square.patch
# Do not install LICENCE file twice, we already put into license directory
Patch5:         tuxanci-0.21.0-Do-not-install-LICENSE.patch
# Do not install bundled fonts
Patch6:         tuxanci-0.21.0-Unbundle-fonts.patch
# Fix building with GCC 15, bug #2341467
Patch7:         tuxanci-0.21.0-Port-to-ISO-C23.patch
# Adapt to CMake 4.0, bug #2381617
Patch8:         tuxanci-0.21.0-Adapt-to-CMake-4.0.patch
BuildRequires:  cmake >= 3.5.0
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  ImageMagick
# libappstream-glib for appstream-util
BuildRequires:  libappstream-glib
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  zziplib-devel
Requires:       font(dejavusans)

%description
Tuxanci is a first Tux shooter game supporting single player and multi-player
modes both on a single computer and over the network.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DCMAKE_FONT=%{_datadir}/fonts/dejavu-sans-fonts/DejaVuSans.ttf
%cmake_build

%install
%cmake_install

# Install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{scalable,48x48}/apps
install -pm644 data/tuxanci.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
convert -geometry 48x48 -depth 8 -background none data/tuxanci.svg \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/tuxanci.png

# Launcher
ln -s tuxanci-%{version} %{buildroot}%{_bindir}/tuxanci
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# Appdata
mkdir -p %{buildroot}%{_datadir}/appdata/
install -pm644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/appdata/tuxanci.appdata.xml

%files
%license LICENCE
%doc %{_docdir}/tuxanci-%{version}
%{_bindir}/tuxanci
%{_bindir}/tuxanci-%{version}
%{_libdir}/tuxanci-%{version}
%{_datadir}/tuxanci-%{version}
%{_datadir}/icons/hicolor
%{_datadir}/applications/tuxanci.desktop
%{_datadir}/appdata/tuxanci.appdata.xml

%changelog
%autochangelog

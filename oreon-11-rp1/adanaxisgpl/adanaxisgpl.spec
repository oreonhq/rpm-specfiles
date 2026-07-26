%global source0_hash none

Summary:        Action game in four spatial dimensions
Name:           adanaxisgpl
Version:        1.2.5
Release:        55%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.mushware.com/
Source0:        http://www.mushware.com/files/%{name}-1.2.5.tar.gz
Patch0:         adanaxisgpl-1.2.5-const.patch
Patch1:         adanaxisgpl-1.2.5-gcc47.patch
Patch2:         adanaxisgpl-1.2.5-xdg-open.patch
Patch3:         adanaxisgpl-gcc11.patch
Patch4:         adanaxisgpl-gcc12.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  freeglut-devel
BuildRequires:  expat-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libvorbis-devel
BuildRequires:  pcre-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  libxcrypt-devel

%description
Adanaxis is a fast-moving first person shooter set in deep space, where the
fundamentals of space itself are changed.  By adding another dimension to
space this game provides an environment with movement in four directions
and six planes of rotation.  Initially the game explains the 4D control
system via a graphical sequence, before moving on to 30 levels of gameplay
with numerous enemy, ally, weapon and mission types.  Features include
simulated 4D texturing, mouse and joystick control, and original music.
Screenshots, movies and further information are available at
http://www.mushware.com/.

Hardware-accelerated 3D is recommended, ideally with support for OpenGL
Shading Language.

%prep
%autosetup -p1

%build
# adanaxisgpl's MushRuby component does a lot of bad things with incomplete
# C function prototypes which -std=gnu23 breaks, keep building it with -std=gnu17
export CFLAGS="${CFLAGS-} -std=gnu17"
export CXXFLAGS="${CXXFLAGS-} -std=gnu17"
%configure
make %{?_smp_mflags}

# Build .desktop files
cat > %{name}.desktop <<EOF
[Desktop Entry]
Name=Adanaxis GPL
Comment=An action game in four spatial dimensions
Exec=%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ActionGame;
EOF

%install
%make_install INSTALL="install -p" CPPROG="cp -p"

# Install desktop files
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{name}.desktop

# Icons
mkdir -p -m 755 %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
mkdir -p -m 755 %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
mkdir -p -m 755 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 x11/icons/%{name}-16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -p -m 644 x11/icons/%{name}-32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 644 x11/icons/%{name}-48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%files
%doc README ChangeLog AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_mandir}/man6/%{name}*.6*

%changelog
%autochangelog

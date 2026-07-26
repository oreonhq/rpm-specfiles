%global source0_hash 62d9604ed69c27b9ca2be1312bc705b36de8ed509c539c6d81193e7846272f18

Name:           tuxpuck
Version:        0.8.2
Release:        43%{?dist}
Summary:        3D Shufflepuck Pong Game

License:        GPL-2.0-only
URL:            http://www.efd.lth.se/~d00jkr/tuxpuck/
Source0:        http://www.efd.lth.se/~d00jkr/tuxpuck/%{name}-%{version}.tar.gz
Source1:        tuxpuck.desktop
Patch0:         tuxpuck-0.8.2-mandest.patch
Patch1:         tuxpuck-0.8.2-utils-werror.patch
Patch2:		tuxpuck-0.8.2-libpng15.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  SDL-devel, freetype-devel, libvorbis-devel
BuildRequires:  libpng-devel, libjpeg-devel, desktop-file-utils
BuildRequires:	ImageMagick

Requires: hicolor-icon-theme

%description
TuxPuck is a shufflepuck game written in C using SDL. The player moves a pad
around a board and tries to shoot down the puck through the opponents defense.
Easy to play, difficult to win.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0 -z .mandest
%patch -P1 -p0 -z .utils-werror
%patch -P2 -p0 -z .libpng15

%build
export CFLAGS="%{optflags}"
make
convert -transparent white data/icons/%{name}.ico %{name}.png

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Install icon and desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install %{name}.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications           \
        %{SOURCE1}

%files
%doc COPYING readme.txt bugs.txt thanks.txt todo.txt
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6.gz
%{_datadir}/applications/tuxpuck.desktop
%{_datadir}/icons/hicolor/32x32/apps/tuxpuck.png

%changelog
%autochangelog

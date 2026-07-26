%global source0_hash fbf016063430c0c47e091aa393dc698b5874e78fce34269c817b73ec67b31be5

Name:           xgalaxy
Version:        2.0.34
Release:        47%{?dist}
Summary:        Arcade game: shoot down the space ships attacking the planet
License:        GPL-1.0-or-later
URL:            http://sourceforge.net/projects/xgalaga/
Source0:        http://downloads.sourceforge.net/xgalaga/xgalaga_%{version}.orig.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}-hyperspace.desktop
Patch0:         http://ftp.debian.org/debian/pool/main/x/xgalaga/xgalaga_2.0.34-44.diff.gz
Patch1:         %{name}-2.0.34-fullscreen.patch
Patch2:         %{name}-2.0.34-%{name}.patch
Patch3:         %{name}-2.0.34-joy.patch
Patch4:         %{name}-2.0.34-fullscreen-viewport.patch
Patch5:         %{name}-2.0.34-alsa.patch
Patch6:         %{name}-2.0.34-dga-compile-fix.patch
Patch7:         xgalaxy-configure-c99.patch
BuildRequires: make
BuildRequires:  libXt-devel libXpm-devel libXmu-devel libXxf86vm-devel
BuildRequires:  alsa-lib-devel desktop-file-utils ImageMagick gcc
Requires:       hicolor-icon-theme
Obsoletes:      xgalaga <= %{version}
Provides:       xgalaga = %{version}-%{release}

%description
Arcade game for the X Window System where you have to shoot down the space
ships attacking the planet.
 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n xgalaga-%{version}
# many thanks to Debian for all their excellent work on xgalala
%patch -P0 -p1 -z .deb
%patch -P1 -p1 -z .fs
%patch -P2 -p1 -z .%{name}
%patch -P3 -p1 -z .joy
%patch -P4 -p1 -z .viewport
%patch -P5 -p1 -z .alsa
%patch -P6 -p1 -z .no-dga
%patch -P7 -p1 -z .c99
sed -e 's/Debian/Fedora/g' debian/README.Debian > README.fedora
cat >> README.fedora << EOF

The latest Fedora %{name} package also includes fullscreen support, start
%{name} with -window to get the old windowed behavior. You can switch on the
fly between window and fullscreen mode with alt+enter.
EOF

# Change the name everywhere as upstreams name has already been used for a game
# much like this one in the past, upstreams use of this is a legal gray area.
sed -i 's/xgalaga/xgalaxy/g' `grep -rls xgalaga .`
sed -i 's/XGalaga/XGalaxy/g' `grep -rls XGalaga .`

%build
export CFLAGS="$RPM_OPT_FLAGS -fsigned-char -DXF86VIDMODE -std=gnu17"
export LDFLAGS=-lXxf86vm
./configure --libdir=%{_libdir} --exec-prefix=%{_bindir} \
  --prefix=%{_datadir}/%{name}
sed -i s/xgal.sndsrv.oss/xgal.sndsrv.alsa/ Makefile
make %{?_smp_mflags} SOUNDLIBS=-lasound
convert images/player3.xpm %{name}.png

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
# move the sound-server binary out of %{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/xgal.sndsrv.alsa \
  $RPM_BUILD_ROOT%{_bindir}
ln -s ../../bin/xgal.sndsrv.alsa \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/xgal.sndsrv.alsa
# fix useless exec bit
chmod -x $RPM_BUILD_ROOT%{_datadir}/%{name}/*/*
# make install doesn't install the manpage
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 644 xgal.6x $RPM_BUILD_ROOT%{_mandir}/man6/%{name}.6

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install         \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
desktop-file-install        \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps
install -p -m 644 %{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps

%files
%doc CHANGES COPYING README README.fedora
%{_bindir}/%{name}*
%{_bindir}/xgal.sndsrv.alsa
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6.gz
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png

%changelog
%autochangelog

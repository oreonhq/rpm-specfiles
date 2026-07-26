%global source0_hash 78f5a9e1785e9e39f6dcb32134a3bd224372f572f191e7ed77bf50b109afb5f7

Name:           glaxium
Version:        0.5
Release:        48%{?dist}
Summary:        An OpenGL space shooter
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://xhosxe.free.fr/glaxium/
Source0:        http://xhosxe.free.fr/glaxium/%{name}_%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.appdata.xml
Patch0:         %{name}-0.5-fixes.patch
Patch1:         %{name}_0.5-allow-running-when-dsp-busy.patch
Patch2:         %{name}_0.5-glutInit.patch
Patch3:         %{name}_0.5-rh553067.patch
Patch4:         %{name}_0.5-64bit-crash.patch
Patch5:         %{name}_0.5-fighter2_meshes-fix.patch
# Fix crash with freeglut >= 3.0 (rhbz#1293048)
Patch6:         0001-Stop-mixing-glut-and-SDL-usage.patch
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  SDL_mixer-devel libpng-devel automake
BuildRequires:  desktop-file-utils libappstream-glib
BuildRequires: make
Requires:       hicolor-icon-theme opengl-games-utils

%description
Glaxium is an OpenGL-based space-ship "shoot-em-up" styled game.
It is designed to provide the same feel as the old 2D games 
of that type, but with 3D for the special effects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}_%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
autoreconf -ivf
sed -i 's|/games/glaxium|/glaxium|g' configure* Makefile.in
sed -i 's/\r//g' CHANGES.txt LICENSE README.txt

%build
%configure
make %{?_smp_mflags}

%install
# make install DESTDIR=$RPM_BUILD_ROOT doesn't work
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%makeinstall
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc CHANGES.txt LICENSE README.txt
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6.gz
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%changelog
%autochangelog

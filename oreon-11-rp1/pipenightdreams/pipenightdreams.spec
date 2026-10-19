%global source0_hash 302f8ce6e0eb32ebd779700527095cf086c2c7132d47095bae9a43c346245541
Name:           pipenightdreams
Version:        0.10.0
Release:        1%{?dist}
Summary:        Connect the waterpipes to create a proper pipeline
License:        GPL-2.0-or-later
URL:            http://www.libsdl.org/projects/pipenightdreams/
Source0:        http://www.libsdl.org/projects/pipenightdreams/packages/pipenightdreams-0.10.0.tar.bz2
Source1:        %{name}.desktop
Patch0:         pipenightdreams-0.10.0-gcc41.patch
Patch1:         pipenightdreams-0.10.0-datadir.patch
Patch2:         pipenightdreams-0.10.0-sanitize.patch
Patch3:         pipenightdreams-0.10.0-quit.patch
Patch4:         pipenightdreams-0.10.0-config.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  SDL_image-devel
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
PipeNightDreams is a puzzle-game where you must race against the clock to
connect the waterpipes to create a proper pipeline before the water starts
flowing. It has 25 levels with increasing difficulty, and you can create
your own by just editing text files. It has a lot of cool graphics, score,
lives, required pipes per level and an easy and fast interface.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -z .gcc41
%patch -P1 -p1 -z .datadir
%patch -P2 -p1 -z .sanitize
%patch -P3 -p1 -z .quit
%patch -P4 -p1 -z .config

%build

%configure
make %{?_smp_mflags} CXXFLAGS="$RPM_OPT_FLAGS -I/usr/include/SDL"
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_datadir}/games/%{name} $RPM_BUILD_ROOT%{_datadir}
rmdir $RPM_BUILD_ROOT%{_datadir}/games
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 images/pipes_space/horizontal.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

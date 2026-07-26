%global source0_hash a496ee28456f46ab8ab4b906771c688344d1624e6d7c5a88b488204b0cb4ce0b

Name:           scorchwentbonkers
Version:        1.3
Release:        27%{?dist}
Summary:        Realtime remake of Scorched Earth
License:        zlib
URL:            http://wasyl.eu/games/scorch-went-bonkers.html
Source0:        http://wasyl.eu/assets/dls/scorch-went-bonkers-src.zip
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.appdata.xml
Patch0:         %{name}-no-fmod.patch
Patch1:         %{name}-support-16bpp.patch
Patch2:         %{name}-unixify.patch
Patch3:         %{name}-gcc6.patch
Patch4:         %{name}-gcc11.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  alleggl-devel jpgalleg-devel dumb-devel AllegroOGG-devel 
BuildRequires:  libGLU-devel desktop-file-utils libappstream-glib
Requires:       hicolor-icon-theme

%description
As the name suggests, Scorch Went Bonkers is a remake of the old PC classic.
However, many things were changed and the type of fun delivered by the game is
different. Where Scorched Earth puts emphasis on tactics and careful
calculations, SWB requires quick thinking, perfect timing and only one finger
for controlling your tank. The game is real-time instead of turn based.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
%patch -P0 -p1 -z .no-fmod
%patch -P1 -p1 -z .16bpp
%patch -P2 -p1 -z .unix
%patch -P3 -p1
%patch -P4 -p1
mv src/menu/Splashscreen.h src/menu/SplashScreen.h

%build
make %{?_smp_mflags} PREFIX=%{_prefix} OPTFLAGS="$RPM_OPT_FLAGS -fsigned-char"

%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%changelog
%autochangelog

%global source0_hash 134a51773d5e441dc31aed4e57b3543afdefe2d8efedeaa05acb85cac0fa9c52

Name:           pachi
Version:        1.0
Release:        44%{?dist}
Summary:        Pachi El Marciano - Platform Game
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://dragontech.sourceforge.net/index.php?main=pachi&lang=en
Source0:        http://downloads.sourceforge.net/dragontech/pachi_source.tgz
Source1:        %{name}.desktop
# manpage from Debian
Source2:        %{name}.6
Source3:        %{name}.appdata.xml
Patch0:         %{name}-fixes.patch
Patch1:         %{name}-nosound.patch
Patch2:         %{name}-more-fixes.patch
Patch3:         %{name}-alt-warnigs-fix.patch
Patch4: pachi-configure-c99.patch
BuildRequires: make
BuildRequires:  gcc gcc-c++ SDL_mixer-devel
BuildRequires:  desktop-file-utils ImageMagick libappstream-glib
Requires:       hicolor-icon-theme

%description
Pachi El Marciano is a cool 2D platform game.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pachi
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p0
%patch -P4 -p1

%build
%configure
make %{?_smp_mflags}
convert Tgfx/icon.bmp %{name}.png

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# easier then patching the Makefile
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_var}/games
mv $RPM_BUILD_ROOT%{_var}/lib/games/%{name}/data/scores.dat \
   $RPM_BUILD_ROOT%{_var}/games/%{name}.hs

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man6

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc ChangeLog README
%license COPYING
%attr(2755,root,games) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_mandir}/man6/%{name}.6*
%config(noreplace) %attr (0664,root,games) %{_var}/games/%{name}.hs

%changelog
%autochangelog

%global source0_hash 01028954ac9eece39f8327aa62aca222209ab52de1393cc165c9ada629a6db9b

Name:           overgod
Version:        1.0
Release:        48%{?dist}
Summary:        Another arcade-style shoot-em-up
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.allegro.cc/depot/Overgod
Source0:        http://downloads.sourceforge.net/overgod/overgod.tar.gz
Source1:        overgod.desktop
Source2:        overgod.png
Source3:        overgod.appdata.xml
Patch0:         overgod-1.0.patch
Patch1:         overgod-1.0-format-string.patch
Patch2:         overgod-1.0-shield_bmp_array_overrun.patch
Patch3:         overgod-1.0-inline-use-fix.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  allegro-devel desktop-file-utils libappstream-glib
Requires:       hicolor-icon-theme

%description
For too long has humanity been ruled by cruel and disputatious gods!
Fly through the various layers of the Celestial Oversphere to unseat
those who control the universe.

In Overgod you control a little vehicle in the middle of the screen and fly
around and shoot things - a bit like asteroids, but the asteroids move
independently and shoot back. You can also upgrade your vehicle in various
ways.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -z .unix
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
sed -i 's/\r//' readme.txt licence.txt

%build
make %{?_smp_mflags} \
  CFLAGS="$RPM_OPT_FLAGS -Wno-unused-but-set-variable" PREFIX=%{_prefix}

%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc readme.txt licence.txt
%{_bindir}/overgod
%{_datadir}/overgod
%{_datadir}/appdata/overgod.appdata.xml
%{_datadir}/applications/overgod.desktop
%{_datadir}/icons/hicolor/48x48/apps/overgod.png

%changelog
%autochangelog

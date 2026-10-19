%global source0_hash 102516e8c312f6b0bbf6c623e1f01cbfbbc314ace8adfe1f201d47b15bd927ff
Name:           rott
Version:        1.1.2
Release:        1%{?dist}
Summary:        Rise of the Triad
License:        GPL-2.0-or-later
URL:            http://icculus.org/rott/
Source0:        http://icculus.org/rott/releases/rott-%{version}.tar.gz
Source1:        rott-shareware.sh
Source2:        rott-registered.sh
Source3:        rott.autodlrc
Source4:        rott-shareware.desktop
Source5:        rott-registered.desktop
Source6:        rott-shareware.appdata.xml
Source7:        rott-registered.metainfo.xml
Source8:        rott.png
# oreon:deps
BuildRequires:  SDL_mixer-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  make
# /oreon:deps
%description
This is the icculus.org Linux port of Apogee's classic 3d shooter Rise of the
Triad, which has been released under the GPL by Apogee. This version is
enhanced with the "high" resolution rendering from the winrott port.

%package        shareware
Summary:        Rise of the Triad shareware version
Requires:       hicolor-icon-theme autodownloader unzip
%description    shareware
This is the icculus.org Linux port of Apogee's classic 3d shooter Rise of the
Triad (RotT), which has been released under the GPL by Apogee. This version is
enhanced with the "high" resolution rendering from the winrott port.

This package contains the engine for the shareware version of RotT. In order to
play the shareware version, you will need the shareware datafiles. Which can
be freely downloaded from Apogee/3DRealms, but cannot be distributed as a part
of Fedora. When you start RotT for the first time it will offer to download
the datafiles for you.

%package        registered
Summary:        Rise of the Triad registered version
Requires:       hicolor-icon-theme zenity
%description    registered
This is the icculus.org Linux port of Apogee's classic 3d shooter Rise of the
Triad (RotT), which has been released under the GPL by Apogee. This version is
enhanced with the "high" resolution rendering from the winrott port.

This package contains the engine for the registered version of RotT. If you own
the registered version, this allows you to play the registered version under
Linux. Place the registered RotT datafiles in a dir and start rott-registered
from this dir.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

cp -a doc/rott.6 rott-shareware.6
cp -a doc/rott.6 rott-registered.6
sed -i.orig 's/rott/rott-shareware/g' rott-shareware.6
sed -i.orig 's/rott/rott-registered/g' rott-registered.6
touch -r rott-shareware.6.orig rott-shareware.6
touch -r rott-registered.6.orig rott-registered.6

%build

pushd rott
make %{?_smp_mflags} \
  EXTRACFLAGS="$RPM_OPT_FLAGS -std=gnu17 -Wno-unused -Wno-pointer-sign" \
  ROTT=rott-shareware.bin
make tidy
make %{?_smp_mflags} \
  EXTRACFLAGS="$RPM_OPT_FLAGS -std=gnu17 -Wno-unused -Wno-pointer-sign" \
  ROTT=rott-registered.bin SHAREWARE=0 SUPERROTT=1
popd
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -m 755 rott/rott-* $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}-shareware
install -p -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/%{name}-registered
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{name}-shareware.6 $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 644 %{name}-registered.6 $RPM_BUILD_ROOT%{_mandir}/man6
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE4}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE5}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE6} %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/*.xml
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE8} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rott-shareware -f %{oreon_filedir}/rott-shareware.list
%files -n rott-registered -f %{oreon_filedir}/rott-registered.list

%changelog

%autochangelog

%global source0_hash a57e19b51dc411ef3e659bfa62bd961d89a2f68ba0b76a1e89e18bae72b362df
%global _vpath_builddir .
Name:           vavoom
Version:        1.33
Release:        49%{?dist}
Summary:        Enhanced Doom, Heretic, Hexen and Strife source port - meta package
Source0:        http://downloads.sourceforge.net/vavoom/%{name}-%{version}.tar.bz2
Source1:        doom.autodlrc
Source2:        heretic.autodlrc
Source3:        hexen.autodlrc
Source4:        strife.autodlrc
Source5:        doom-shareware.sh
Source6:        heretic-shareware.sh
Source7:        hexen-demo.sh
Source8:        strife-demo.sh
Source9:        doom-shareware.desktop
Source10:       heretic-shareware.desktop
Source11:       hexen-demo.desktop
Source12:       strife-demo.desktop
Source13:       vavoom.desktop
Source14:       doom-shareware.appdata.xml
Source15:       heretic-shareware.appdata.xml
Source16:       hexen-demo.appdata.xml
Source17:       strife-demo.appdata.xml
Source18:       vavoom.appdata.xml
Source19:       vavoom.png
Source20:       doom-logo.png
Source21:       tux-b2f.png
Source22:       vavoom.6
Patch0:         vavoom-1.21-datadir.patch
Patch1:         vavoom-1.27-CMakeLists.patch
Patch2:         vavoom-1.33-format-security.patch
Patch3:         vavoom-1.33-dont-override-delete.patch
Patch4:         vavoom-1.33-default-iwaddir.patch
Patch5:         vavoom-1.33-gcc6.patch
Patch6:         vavoom-1.33-misc-fixes.patch
Patch7:         vavoom-1.33-cx11.patch
Patch8:         vavoom-1.33-crash-on-exit.patch
Patch9:         vavoom-1.33-wxwidgets3.0.patch
URL:            http://vavoom-engine.com/
License:        GPL-2.0-or-later
Requires:       %{name}-engine = %{version}-%{release}
Requires:       %{name}-doom-shareware = %{version}-%{release}
Requires:       %{name}-heretic-shareware = %{version}-%{release}
Requires:       %{name}-hexen-demo = %{version}-%{release}
Requires:       %{name}-strife-demo = %{version}-%{release}
# oreon:deps
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_net-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  flac-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libGLU-devel
BuildRequires:  libappstream-glib
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  mikmod-devel
BuildRequires:  openal-soft-devel
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
Vavoom is an enhanced open-source port of Doom. The "vavoom" meta-package
installs vavoom-engine, and launchers / menu-entries to download and play
doom-shareware, heretic-shareware, hexen-demo and strife-demo.

%package engine
Summary:        Enhanced Doom, Heretic, Hexen and Strife game engine
Requires:       timidity++-patches hicolor-icon-theme
%description engine
Vavoom is an enhanced open-source port of Doom. Allowing you to play not only
the classic 3D first-person shooter Doom, but also the Doom derived classics
Heretic, Hexen and Strife. Compared to the original games it adds extra
features such as translucency and freelook support and ofcourse the capability
to play these classics under Linux.

%package doom-shareware
Summary:        Doom shareware installer
BuildArch:      noarch
Requires:       %{name}-engine = %{version}-%{release}
Requires:       autodownloader unzip
%description doom-shareware
Doom is id Software's classic first person shooter follow-up to
Wolfenstein 3D. The Doom engine is Open Source. The original Doom datafiles
however are not Open Source. There is a gratis, but not Open Source shareware
version available on the internet.

This package contains an applications menu entry for playing Doom shareware
using the vavoom engine.  The first time you click this menu entry, it will
offer to download and install the Doom shareware datafiles for you.

%package heretic-shareware
Summary:        Heretic shareware installer
BuildArch:      noarch
Requires:       %{name}-engine = %{version}-%{release}
Requires:       autodownloader unzip
%description heretic-shareware
Heretic is Raven's classic dark fantasy first person shooter using a
modified Doom engine. The Heretic engine is Open Source. The original
Heretic datafiles however are not Open Source. There is a gratis, but not
Open Source shareware version available on the internet.

This package contains an applications menu entry for playing Heretic
shareware using the vavoom engine. The first time you click this menu
entry, it will offer to download and install the Heretic shareware
datafiles for you.

%package hexen-demo
Summary:        Hexen demo installer
BuildArch:      noarch
Requires:       %{name}-engine = %{version}-%{release}
Requires:       autodownloader unzip
%description hexen-demo
Hexen: Beyond Heretic is Raven's classic dark fantasy first person shooter
follow-up to Heretic. The Hexen engine is Open Source. The original Hexen
datafiles however are not Open Source. There is a gratis, but not Open
Source demo version available on the internet.

This package contains an applications menu entry for playing Hexen
demo using the vavoom engine. The first time you click this menu
entry, it will offer to download and install the Hexen demo
datafiles for you.

%package strife-demo
Summary:        Strife demo installer
BuildArch:      noarch
Requires:       %{name}-engine = %{version}-%{release}
Requires:       autodownloader unzip
%description strife-demo
Strife is Rogue Entertainment's classic first person shooter with
role-playing game elements. The Strife engine is Open Source. The original
Strife datafiles however are not Open Source. There is a gratis, but not
Open Source demo version available on the internet.

This package contains an applications menu entry for playing Strife
demo using the vavoom engine. The first time you click this menu
entry, it will offer to download and install the Strife demo
datafiles for you.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .datadir
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P9 -p1

%build

export CXXFLAGS="$RPM_OPT_FLAGS -std=gnu++98 -fno-strict-aliasing -Wno-unused -Wno-unused-but-set-variable -Wno-unused-result -Wno-sign-compare -Wno-reorder"
%cmake -DWITH_LIBMAD:BOOL=OFF
sed -i "s|#define FL_BASEDIR.*|#define FL_BASEDIR \"%{_datadir}/%{name}\"|" source/files.h
sed -i "s|#define CONFIG_FILE.*|#define CONFIG_FILE \"%{_sysconfdir}/timidity.cfg\"|" source/timidity/timidity.h
make -C source revision_check
make linespec
make VERBOSE=1
%install
make install \
        DESTDIR=$RPM_BUILD_ROOT \
        INSTALL_PARMS="-m 0755" \
        INSTALL_EXEPARMS="-m 0755" \
        INSTALL_DIRPARMS="-m 0755 -d"
mv $RPM_BUILD_ROOT%{_bindir}/%{name}.* $RPM_BUILD_ROOT%{_bindir}/%{name}
mv $RPM_BUILD_ROOT%{_bindir}/%{name}-dedicated.* $RPM_BUILD_ROOT%{_bindir}/%{name}-dedicated
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.png
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 755 %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}/doom-shareware
install -p -m 755 %{SOURCE6} $RPM_BUILD_ROOT%{_bindir}/heretic-shareware
install -p -m 755 %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}/hexen-demo
install -p -m 755 %{SOURCE8} $RPM_BUILD_ROOT%{_bindir}/strife-demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
for i in %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13}; do
  desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications "$i"
done
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
for i in %{SOURCE14} %{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18}; do
  install -p -m 644 "$i" $RPM_BUILD_ROOT%{_datadir}/appdata
  appstream-util validate-relax --nonet \
    $RPM_BUILD_ROOT%{_datadir}/appdata/$(basename "$i")
done
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{48x48,96x96}/apps
install -p -m 644 %{SOURCE19} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/96x96/apps/
install -p -m 644 %{SOURCE20} %{SOURCE21} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 644 %{SOURCE22} $RPM_BUILD_ROOT%{_mandir}/man6
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n vavoom-engine -f %{oreon_filedir}/vavoom-engine.list
%files -n vavoom-doom-shareware -f %{oreon_filedir}/vavoom-doom-shareware.list
%files -n vavoom-heretic-shareware -f %{oreon_filedir}/vavoom-heretic-shareware.list
%files -n vavoom-hexen-demo -f %{oreon_filedir}/vavoom-hexen-demo.list
%files -n vavoom-strife-demo -f %{oreon_filedir}/vavoom-strife-demo.list

%changelog

%autochangelog

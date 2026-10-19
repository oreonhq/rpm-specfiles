%global source0_hash 5547f80db067dea923ae693ba6bb88eb2b2eeac1da3ebec42fce453e31c290c0
Name:           calamares
Version:        3.3.14
Release:        1%{?dist}
Summary:        Installer from a live CD/DVD/USB to disk
License:        GPL-3.0-or-later
URL:            https://calamares.io/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source2:        show.qml
Source3:        calamares-auto_fr.ts
Source4:        calamares-auto_de.ts
Source5:        calamares-auto_it.ts
Patch1001:       calamares-3.3.14-default-settings.patch
Patch1002:       calamares-3.3.3-kdesu.patch
ExclusiveArch:  %{ix86} x86_64 aarch64 riscv64
%global __python %{__python3}
Requires(post): system-release
Requires(post): system-logos
Requires:       system-logos
Requires:       coreutils
Requires:       util-linux
Requires:       upower
Requires:       NetworkManager
Requires:       dracut
Requires:       grub2
%ifarch x86_64 aarch64 riscv64
%ifarch x86_64
Requires:       grub2-efi-x64
Recommends:     grub2-efi-ia32
%else
Requires:       grub2-efi
%endif
Requires:       efibootmgr
%endif
Requires:       console-setup
Requires:       setxkbmap
Requires:       os-prober
Requires:       e2fsprogs
Requires:       dosfstools
Requires:       ntfsprogs
Requires:       gawk
Requires:       systemd
Requires:       rsync
Requires:       shadow-utils
Requires:       dnf
Requires:       kdesu
Requires:       hicolor-icon-theme
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-webview < 3.0.0~
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(AppStreamQt)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KPMcore)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  kf6-rpm-macros
BuildRequires:  libpwquality-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  parted-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-jsonschema
BuildRequires:  python3-pyyaml
BuildRequires:  yaml-cpp-devel
# /oreon:deps
%description
Calamares is a distribution-independent installer framework, designed to install
from a live CD/DVD/USB environment to a hard disk. It includes a graphical
installation program based on Qt 6. This package includes the Calamares
framework and the required configuration files to produce a working replacement
for Anaconda's liveinst.

%package        libs
Summary:        Calamares runtime libraries
Requires:       %{name} = %{version}-%{release}
%description    libs
%{summary}.

%package        interactiveterminal
Summary:        Calamares interactiveterminal module
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       konsole-part
%description    interactiveterminal
Optional interactiveterminal module for the Calamares installer, based on the
KonsolePart (from Konsole 6)

%package        plasmalnf
Summary:        Calamares plasmalnf module
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       plasma-desktop
%description    plasmalnf
Optional plasmalnf module for the Calamares installer, based on the KDE Plasma
Desktop Workspace and its KDE Frameworks (KConfig, KPackage, Plasma)

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake
%description    devel
The %{name}-devel package contains libraries and header files for
developing custom modules for Calamares.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%{cmake_kf6} -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
             -DBUILD_TESTING:BOOL=OFF \
             -DWITH_PYBIND11:BOOL=OFF \
             -DWITH_QT6:BOOL=ON \
             %{nil}
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/calamares/branding/auto
touch %{buildroot}%{_datadir}/calamares/branding/auto/branding.desc
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/calamares/branding/auto/show.qml
mkdir -p %{buildroot}%{_datadir}/calamares/branding/auto/lang
lrelease-qt6 %{SOURCE3} -qm %{buildroot}%{_datadir}/calamares/branding/auto/lang/calamares-auto_fr.qm
lrelease-qt6 %{SOURCE4} -qm %{buildroot}%{_datadir}/calamares/branding/auto/lang/calamares-auto_de.qm
lrelease-qt6 %{SOURCE5} -qm %{buildroot}%{_datadir}/calamares/branding/auto/lang/calamares-auto_it.qm
mkdir -p %{buildroot}%{_sysconfdir}/calamares/modules
mkdir -p %{buildroot}%{_sysconfdir}/calamares/branding
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/calamares-dummypythonqt.mo
%find_lang calamares-python
%oreon_autofiles calamares-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles calamares-interactiveterminal usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles calamares-plasmalnf usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles calamares-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/calamares.desktop
%post

. %{_sysconfdir}/os-release
LOGO=%{_datadir}/pixmaps/fedora-logo.png
if [ -e %{_datadir}/pixmaps/fedora-logo-sprite.png ] ; then
  SPRITE="%{_datadir}/pixmaps/fedora-logo-sprite.png"
else
  SPRITE="%{_datadir}/calamares/branding/default/squid.png"
fi
if [ -e %{_datadir}/icons/hicolor/48x48/apps/fedora-logo-icon.png ] ; then
  ICON="%{_datadir}/icons/hicolor/48x48/apps/fedora-logo-icon.png"
else
  ICON="$SPRITE"
fi
if [ -n "$HOME_URL" ] ; then
  PRODUCTURL="$HOME_URL"
  HAVE_PRODUCTURL=" "
else
  PRODUCTURL="https://calamares.io/"
  HAVE_PRODUCTURL="#"
fi
if [ -n "$SUPPORT_URL" ] ; then
  SUPPORTURL="$SUPPORT_URL"
  HAVE_SUPPORTURL=" "
elif [ -n "$BUG_REPORT_URL" ] ; then
  SUPPORTURL="$BUG_REPORT_URL"
  HAVE_SUPPORTURL=" "
else
  SUPPORTURL="https://github.com/calamares/calamares/issues"
  HAVE_SUPPORTURL="#"
fi
cat >%{_datadir}/calamares/branding/auto/branding.desc <<EOF
---
componentName:  auto
welcomeStyleCalamares:   true
strings:
    productName:         "$NAME"
    shortProductName:    "$NAME"
    version:             "$VERSION"
    shortVersion:        "$VERSION_ID"
    versionedName:       "$NAME $VERSION"
    shortVersionedName:  "$NAME $VERSION_ID"
    bootloaderEntryName: "$NAME"
$HAVE_PRODUCTURL   productUrl:          "$PRODUCTURL"
$HAVE_SUPPORTURL   supportUrl:          "$SUPPORTURL"
images:
    productWelcome:      "$LOGO"
    productLogo:         "$SPRITE"
    productIcon:         "$ICON"
slideshow:               "show.qml"
style:
   sidebarBackground:    "#292F34"
   sidebarText:          "#FFFFFF"
   sidebarTextSelect:    "#292F34"
   sidebarTextHighlight: "#D35400"
EOF
%files -f %{oreon_filedir}/main.list
%files -n calamares-libs -f %{oreon_filedir}/calamares-libs.list
%files -n calamares-interactiveterminal -f %{oreon_filedir}/calamares-interactiveterminal.list
%files -n calamares-plasmalnf -f %{oreon_filedir}/calamares-plasmalnf.list
%files -n calamares-devel -f %{oreon_filedir}/calamares-devel.list

%changelog

%autochangelog

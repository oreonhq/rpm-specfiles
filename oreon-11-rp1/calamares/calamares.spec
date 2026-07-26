%global source0_hash 5547f80db067dea923ae693ba6bb88eb2b2eeac1da3ebec42fce453e31c290c0

Name:           calamares
Version:        3.3.14
Release:        5%{?dist}
Summary:        Installer from a live CD/DVD/USB to disk

License:        GPL-3.0-or-later
URL:            https://calamares.io/
Source0:        https://github.com/calamares/calamares/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/calamares-%{?snaphash}%{!?snaphash:%{version}}.tar.gz
Source2:        show.qml
# Run:
# lupdate-qt6 show.qml -ts calamares-auto_fr.ts
# then translate the template in linguist-qt6.
Source3:        calamares-auto_fr.ts
# Run:
# lupdate-qt6 show.qml -ts calamares-auto_de.ts
# then translate the template in linguist-qt6.
Source4:        calamares-auto_de.ts
# Run:
# lupdate-qt6 show.qml -ts calamares-auto_it.ts
# then translate the template in linguist-qt6.
Source5:        calamares-auto_it.ts

# Backports from upstream

# Fedora-specific changes
## adjust some default settings (default shipped .conf files)
Patch1001:       calamares-3.3.14-default-settings.patch
## use kdesu instead of pkexec (works around #1171779)
Patch1002:       calamares-3.3.3-kdesu.patch

# Calamares is only supported where live images (and GRUB) are. (#1171380)
# This list matches the arches where grub2-efi is used to boot the system
ExclusiveArch:  %{ix86} x86_64 aarch64 riscv64

# Macros
BuildRequires:  git-core
BuildRequires:  kf6-rpm-macros

# Compilation tools
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 5.245
BuildRequires:  gcc-c++ >= 9.0.0
BuildRequires:  pkgconfig
BuildRequires:  make

# Other build-time tools
BuildRequires:  desktop-file-utils
BuildRequires:  gettext

# Qt 6
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickWidgets)

# KF6
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)

# Plasma
BuildRequires:  cmake(Plasma)

# KPMcore
BuildRequires:  cmake(KPMcore) >= 4.2.0

# Python 3
BuildRequires:  python3-devel >= 3.3
BuildRequires:  python3-jsonschema
BuildRequires:  python3-pyyaml
BuildRequires:  boost-devel >= 1.55.0
%global __python %{__python3}

# Other libraries
BuildRequires:  cmake(AppStreamQt) >= 1.0.0
BuildRequires:  libpwquality-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  parted-devel
BuildRequires:  yaml-cpp-devel >= 0.5.1

# for automatic branding setup
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
# For x86 systems
Requires:       grub2-efi-x64
Recommends:     grub2-efi-ia32
%else
# For all non-x86 arches
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
# webview module is no longer available
Obsoletes:      %{name}-webview < 3.0.0~

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

%autosetup -S git_am -n %{name}-%{version}

%build
%{cmake_kf6} -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
             -DBUILD_TESTING:BOOL=OFF \
             -DWITH_PYBIND11:BOOL=OFF \
             -DWITH_QT6:BOOL=ON \
             %{nil}
%cmake_build

%install
%cmake_install

# create the auto branding directory
mkdir -p %{buildroot}%{_datadir}/calamares/branding/auto
touch %{buildroot}%{_datadir}/calamares/branding/auto/branding.desc
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/calamares/branding/auto/show.qml
mkdir -p %{buildroot}%{_datadir}/calamares/branding/auto/lang
lrelease-qt6 %{SOURCE3} -qm %{buildroot}%{_datadir}/calamares/branding/auto/lang/calamares-auto_fr.qm
lrelease-qt6 %{SOURCE4} -qm %{buildroot}%{_datadir}/calamares/branding/auto/lang/calamares-auto_de.qm
lrelease-qt6 %{SOURCE5} -qm %{buildroot}%{_datadir}/calamares/branding/auto/lang/calamares-auto_it.qm
# own the local settings directories
mkdir -p %{buildroot}%{_sysconfdir}/calamares/modules
mkdir -p %{buildroot}%{_sysconfdir}/calamares/branding
# delete dummypythonqt translations, we do not use PythonQt at this time
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/calamares-dummypythonqt.mo
%find_lang calamares-python

%check
# validate the .desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/calamares.desktop

%post
# generate the "auto" branding
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
# THIS FILE IS AUTOMATICALLY GENERATED! ANY CHANGES TO THIS FILE WILL BE LOST!
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
#   knownIssuesUrl:      "http://calamares.io/about/"
#   releaseNotesUrl:     "http://calamares.io/about/"

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

%files -f calamares-python.lang
%doc AUTHORS
%license LICENSES/*
%{_bindir}/calamares
%dir %{_datadir}/calamares/
%{_datadir}/calamares/settings.conf
%dir %{_datadir}/calamares/branding/
%{_datadir}/calamares/branding/default/
%dir %{_datadir}/calamares/branding/auto/
%ghost %{_datadir}/calamares/branding/auto/branding.desc
%{_datadir}/calamares/branding/auto/show.qml
%{_datadir}/calamares/branding/auto/lang/
%{_datadir}/calamares/modules/
%exclude %{_datadir}/calamares/modules/interactiveterminal.conf
%exclude %{_datadir}/calamares/modules/plasmalnf.conf
%{_datadir}/calamares/qml/
%{_datadir}/applications/calamares.desktop
%{_datadir}/icons/hicolor/scalable/apps/calamares.svg
%{_mandir}/man8/calamares.8*
%{_sysconfdir}/calamares/

%files libs
%{_libdir}/libcalamares.so.*
%{_libdir}/libcalamaresui.so.*
%{_libdir}/calamares/
%exclude %{_libdir}/calamares/modules/interactiveterminal/
%exclude %{_libdir}/calamares/modules/plasmalnf/

%files interactiveterminal
%{_datadir}/calamares/modules/interactiveterminal.conf
%{_libdir}/calamares/modules/interactiveterminal/

%files plasmalnf
%{_datadir}/calamares/modules/plasmalnf.conf
%{_libdir}/calamares/modules/plasmalnf/

%files devel
%{_includedir}/libcalamares/
%{_libdir}/libcalamares.so
%{_libdir}/libcalamaresui.so
%{_libdir}/cmake/Calamares/

%changelog
%autochangelog

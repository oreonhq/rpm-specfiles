
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kinfocenter
Version: 6.6.2
Release:	2%{?dist}
Summary: KDE Info Center

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND FSFAP AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0: http://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: http://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires:  qt6-qtbase-devel

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  libX11-devel
BuildRequires:  pciutils-devel
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libudev)
%ifnarch s390 s390x
BuildRequires:  libraw1394-devel
%endif

BuildRequires: cmake(KF6Kirigami2)
Requires: kf6-kirigami2%{?_isa}

# runtime query of usb.ids, oui.txt
Requires: hwdata

# Runtime dependencies
Requires: plasma-systemsettings
Requires: wayland-utils
%ifarch %{ix86} x86_64 aarch64
Requires: dmidecode
%endif
Requires: vulkan-tools
Requires: xdpyinfo
Requires: egl-utils
Requires: fwupd
Requires: aha
Requires: clinfo
Requires: pulseaudio-utils
Requires: libdisplay-info-tools

# When kinfocenter was split out from kde-workspace
Conflicts:      kde-workspace < 4.11.15-3

%description
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kinfocenter.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/kcm_about-distro.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/kcm_energyinfo.desktop
# commented out until upstream fixes a duplicate entries problem
#appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%{_datadir}/applications/kcm_energyinfo.desktop
%{_bindir}/kinfocenter
%{_kf6_libdir}/libKInfoCenterInternal.so
%{_kf6_qtplugindir}/plasma/kcms/*.so
%{_kf6_qtplugindir}/plasma/kcms/kinfocenter/*.so
%{_datadir}/metainfo/org.kde.kinfocenter.appdata.xml
%{_datadir}/applications/org.kde.kinfocenter.desktop
%{_datadir}/applications/kcm_about-distro.desktop
%{_kf6_datadir}/dbus-1/system-services/org.kde.kinfocenter.dmidecode.service
%{_kf6_datadir}/dbus-1/system.d/org.kde.kinfocenter.dmidecode.conf
%{_libexecdir}/kinfocenter-opengl-helper
%{_kf6_datadir}/kinfocenter/
%{_kf6_datadir}/polkit-1/actions/org.kde.kinfocenter.dmidecode.policy
%{_qt6_archdatadir}/qml/org/kde/kinfocenter/
%{_kf6_libexecdir}/kauth/kinfocenter-dmidecode-helper
%{_libexecdir}/kinfocenter-vulkan-helper

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)

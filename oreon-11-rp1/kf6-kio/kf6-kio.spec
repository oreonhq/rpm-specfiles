%global source1_hash 24ab28ac12dab8f74971e04312d858be5a037dec6f6af424329f8de1ed2ca9d2
%global source0_hash c19cbd4878347b67a9e05ee6541083f51dd90f9e58ee245b4d7634e09f9c04b2
%global framework kio
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:    kf6-%{framework}
Version: 6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 3 solution for filesystem abstraction
License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Patch0:  0001-Give-the-kuriikwsfiltereng_private-a-VERSION-and-SOV.patch
%if 0%{?flatpak}
Patch101: kio-no-help-protocol.patch
%endif
%if !0%{?flatpak}
%endif
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-file-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-gui%{?_isa} = %{version}-%{release}
Requires: kf6-kded
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KDED)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libacl-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  switcheroo-control
BuildRequires:  zlib-devel
# /oreon:deps
%description
KDE Frameworks 6 Tier 3 solution for filesystem abstraction

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       kf6-kbookmarks-devel
Requires:       cmake(KF6Completion)
Requires:       cmake(KF6Config)
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KF6ItemViews)
Requires:       cmake(KF6JobWidgets)
Requires:       cmake(KF6Service)
Requires:       cmake(KF6Solid)
Requires:       cmake(KF6XmlGui)
Requires:       cmake(KF6WindowSystem)
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Requires:       %{name}-core = %{version}-%{release}
BuildArch:      noarch
%description    doc
Documentation for %{name}.

%package        core
Summary:        Core components of the KIO Framework
%{?kf6_kinit_requires}
Requires:       %{name}-core-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-doc = %{version}-%{release}
Requires:       kf6-filesystem
Requires:       libxslt%{?_isa}
Recommends:     switcheroo-control
%description    core
KIOCore library provides core non-GUI components for working with KIO.

%package        core-libs
Summary:        Runtime libraries for KIO Core
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
%description    core-libs
%{summary}.

%package        widgets
Summary:        Widgets for KIO Framework
%{?kf6_kinit_requires}
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
%description    widgets
KIOWidgets contains classes that provide generic job control, progress
reporting, etc.

%package        widgets-libs
Summary:        Runtime libraries for KIO Widgets library
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
%description    widgets-libs
%{summary}.

%package        file-widgets
Summary:        Widgets for file-handling for KIO Framework
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
%description    file-widgets
The KIOFileWidgets library provides the file selection dialog and
its components.

%package        gui
Summary:        Gui components for the KIO Framework
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
%description    gui
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang %{name} --all-name --with-man --with-html
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-kio-devel -f %{oreon_filedir}/kf6-kio-devel.list
%files -n kf6-kio-doc -f %{oreon_filedir}/kf6-kio-doc.list
%files -n kf6-kio-core -f %{oreon_filedir}/kf6-kio-core.list
%files -n kf6-kio-core-libs -f %{oreon_filedir}/kf6-kio-core-libs.list
%files -n kf6-kio-widgets -f %{oreon_filedir}/kf6-kio-widgets.list
%files -n kf6-kio-widgets-libs -f %{oreon_filedir}/kf6-kio-widgets-libs.list
%files -n kf6-kio-file-widgets -f %{oreon_filedir}/kf6-kio-file-widgets.list
%files -n kf6-kio-gui -f %{oreon_filedir}/kf6-kio-gui.list

%changelog

%autochangelog

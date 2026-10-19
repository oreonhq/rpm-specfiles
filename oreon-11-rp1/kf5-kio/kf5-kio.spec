%global source0_hash efb719d6659c39a03b165dca3b6c84f729a833290fc44e7e1f99625690b6115a
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%global framework kio
%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]
%bcond_with bootstrap
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 solution for filesystem abstraction
License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
%if 0%{?flatpak}
Patch101: kio-no-help-protocol.patch
%endif
%global __provides_exclude_from ^(%{_kf5_qtplugindir}/.*\\.so)$
%if !0%{?flatpak}
%endif
%if %{without bootstrap}
%endif
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-file-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-ntlm%{?_isa} = %{version}-%{release}
Requires:       %{name}-gui%{?_isa} = %{version}-%{release}
Requires: kf5-kded
# oreon:deps
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-karchive-devel
BuildRequires:  kf5-kbookmarks-devel
BuildRequires:  kf5-kcompletion-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kguiaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kitemviews-devel
BuildRequires:  kf5-kjobwidgets-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-solid-devel
BuildRequires:  krb5-devel
BuildRequires:  libacl-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(mount)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  switcheroo-control
BuildRequires:  zlib-devel
# /oreon:deps
%description
KDE Frameworks 5 Tier 3 solution for filesystem abstraction

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kbookmarks-devel >= %{majmin}
Requires:       kf5-kcompletion-devel >= %{majmin}
Requires:       kf5-kconfig-devel >= %{majmin}
Requires:       kf5-kcoreaddons-devel >= %{majmin}
Requires:       kf5-kitemviews-devel >= %{majmin}
Requires:       kf5-kjobwidgets-devel >= %{majmin}
Requires:       kf5-kservice-devel >= %{majmin}
Requires:       kf5-solid-devel >= %{majmin}
Requires:       kf5-kxmlgui-devel >= %{majmin}
Requires:       kf5-kwindowsystem-devel >= %{majmin}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Requires:       %{name}-core = %{version}-%{release}
Obsoletes:      kf5-kio-doc < 5.11.0-3
BuildArch:      noarch
%description    doc
Documentation for %{name}.

%package        core
Summary:        Core components of the KIO Framework
%{?kf5_kinit_requires}
Requires:       %{name}-core-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-doc = %{version}-%{release}
Recommends:     switcheroo-control
%description    core
KIOCore library provides core non-GUI components for working with KIO.

%package        core-libs
Summary:        Runtime libraries for KIO Core
Requires:       %{name}-core = %{version}-%{release}
%description    core-libs
%{summary}.

%package        widgets
Summary:        Widgets for KIO Framework
%{?kf5_kinit_requires}
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
%description    widgets
KIOWidgets contains classes that provide generic job control, progress
reporting, etc.

%package        widgets-libs
Summary:        Runtime libraries for KIO Widgets library
Requires:       %{name}-widgets = %{version}-%{release}
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
Recommends:     switcheroo-control
%description    gui
%{summary}.

%package        ntlm
Summary:        NTLM support for KIO Framework
%description    ntlm
KIONTLM provides support for NTLM authentication mechanism in KIO

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-man --with-html
%if %{with kf6_compat}
rm %{buildroot}%{_datadir}/applications/kcm_trash.desktop
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n kf5-kio-devel -f %{oreon_filedir}/kf5-kio-devel.list
%files -n kf5-kio-doc -f %{oreon_filedir}/kf5-kio-doc.list
%files -n kf5-kio-core -f %{oreon_filedir}/kf5-kio-core.list
%files -n kf5-kio-core-libs -f %{oreon_filedir}/kf5-kio-core-libs.list
%files -n kf5-kio-widgets -f %{oreon_filedir}/kf5-kio-widgets.list
%files -n kf5-kio-widgets-libs -f %{oreon_filedir}/kf5-kio-widgets-libs.list
%files -n kf5-kio-file-widgets -f %{oreon_filedir}/kf5-kio-file-widgets.list
%files -n kf5-kio-gui -f %{oreon_filedir}/kf5-kio-gui.list
%files -n kf5-kio-ntlm -f %{oreon_filedir}/kf5-kio-ntlm.list

%changelog

%autochangelog

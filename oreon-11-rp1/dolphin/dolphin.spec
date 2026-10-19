%global source0_hash f5635feff84e7070d35342d6defb46e9b42ff1c44e3896635f4bd9f43da947c1
%global stable_kf6 stable
%global maj_ver_kf6 26
%global min_ver_kf6 04
%global bug_ver_kf6 3
%global tests 1
Name:           dolphin
Summary:        KDE File Manager
Version:        26.08.1
Release:        1%{?dist}
License:        BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/system/dolphin
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if 0%{?tests}
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Recommends:     konsole-part%{?_isa}
Recommends:     kio-fuse%{?_isa}
Recommends:     kio-extras%{?_isa}
Recommends:     %{name}-plugins
Recommends:     kf6-kimageformats%{?_isa}
Recommends:     qt6-qtimageformats%{?_isa}
Recommends:     ffmpegthumbs%{?_isa}
# oreon:deps
BuildRequires:  cmake(KF6Baloo)
BuildRequires:  cmake(KF6BalooWidgets)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6UserFeedback)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(packagekitqt6)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-static
BuildRequires:  rubygem(test-unit)
BuildRequires:  systemd-rpm-macros
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
%{summary}.

%package        libs
Summary:        Dolphin runtime libraries
%description    libs
%{summary}.

%package        devel
Summary:        Developer files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel%{?_isa}
Requires:       kf6-kio-devel%{?_isa}
%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6 \
  %{?flatpak:-DFLATPAK:BOOL=ON} \
  -DKDE_INSTALL_SYSTEMDUSERUNITDIR=%{_userunitdir} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}
%cmake_build
%install
%cmake_install
%find_lang dolphin --all-name --with-html
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%if 0%{?tests}
xvfb-run -a bash -c "%ctest" || :
%endif
%files -f %{oreon_filedir}/main.list
%files -n dolphin-libs -f %{oreon_filedir}/dolphin-libs.list
%files -n dolphin-devel -f %{oreon_filedir}/dolphin-devel.list

%changelog

%autochangelog

%global source0_hash 7828ab25937d4dc5364f815d0fff3df29e731a74e3f2a2eaf32a016a53e1e381
%global repo dde-application-manager
Name:           deepin-application-manager
Version:        1.2.62
Release:        1%{?dist}
Summary:        App manager of Deepin Desktop Environment
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-application-manager
Source0:        https://github.com/linuxdeepin/%{repo}/archive/%{version}/%{repo}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(TreelandProtocols)
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libsystemd)
# /oreon:deps
%description
DDE Application Manager is the app manager of Deepin Desktop Environment.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{repo}-%{version}

%build

%cmake -GNinja -DBUILD_TESTING=ON
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_libexecdir}/deepin/application-manager/app-update-notifier
rm %{buildroot}%{_datadir}/dbus-1/system-services/org.desktopspec.ApplicationUpdateNotifier1.service
rm %{buildroot}%{_datadir}/dbus-1/system.d/org.desktopspec.ApplicationUpdateNotifier1.conf
rm %{buildroot}%{_unitdir}/org.desktopspec.ApplicationUpdateNotifier1.service
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n deepin-application-manager-devel -f %{oreon_filedir}/deepin-application-manager-devel.list

%changelog

%autochangelog

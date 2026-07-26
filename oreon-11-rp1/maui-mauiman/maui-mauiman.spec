%global source0_hash da9b4353c595e91dc3311591d8cac090e325531877067794902659a884df9843

Name:           maui-mauiman
Version:        4.0.2
Release:        1%{?dist}
License:        LGPL-3.0-or-later
Summary:        Maui Manager Library
Url:            https://invent.kde.org/maui/mauiman
Source:         %{url}/-/archive/v%{version}/mauiman-v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  dbus-common

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)

# Make sure there is an owner for /usr/share/dbus-1
# and /usr/share/dbus-1/services
Requires: dbus-common

%description
MauiMan stands for Maui Manager, and exists for setting,
saving, and syncing the configuration preferences for the
Maui Apps & Shell ecosystem.

%package devel
Summary:        MauiMan development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Required headers to build components using
MauiMan.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n mauiman-v%{version} -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6=ON -DBUILD_WITH_QT5=OFF
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/LGPL-3.0.txt
%{_bindir}/MauiManServer4
%{_datadir}/dbus-1/services/org.mauiman.Manager4.service
%{_libdir}/libMauiMan4.so.4*

%files devel
%{_libdir}/libMauiMan4.so
%dir %{_includedir}/MauiMan4
%{_includedir}/MauiMan4/settingsstore.h
%{_includedir}/MauiMan4/backgroundmanager.h
%{_includedir}/MauiMan4/thememanager.h
%{_includedir}/MauiMan4/screenmanager.h
%{_includedir}/MauiMan4/formfactormanager.h
%{_includedir}/MauiMan4/accessibilitymanager.h
%{_includedir}/MauiMan4/inputdevicesmanager.h
%{_includedir}/MauiMan4/mauimanutils.h
%{_includedir}/MauiMan4/mauiman_export.h
%dir %{_libdir}/cmake/MauiMan4
%{_libdir}/cmake/MauiMan4/*.cmake

%changelog
%autochangelog

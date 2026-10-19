%global source0_hash 4c50c448622dc9c5041ed10da7d87b3e4e71ccb49d4831a849211d423c5f5d33
%bcond qt5 0
%bcond qt6 1
Name:    qaccessibilityclient
Summary:        Accessibility client library for Qt5 and Qt6
Version: 0.6.0
Release:        1%{?dist}
License: CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://cgit.kde.org/libkdeaccessibilityclient.git/
Source0:        https://download.kde.org/stable/libqaccessibilityclient/libqaccessibilityclient-%{version}.tar.xz
%if %{with qt5}
%endif
%if %{with qt6}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
# /oreon:deps
%description
%{summary}.

%if %{with qt5}
%package qt5
Summary: Accessibility client library for Qt5
Provides: libqaccessibilityclient = %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
%description  qt5
%{summary}.

%package qt5-devel
Summary: Development files for %{name}-qt5
Provides: libqaccessibilityclient-devel = %{version}-%{release}
Obsoletes: %{name}-devel < %{version}-%{release}
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel
%description  qt5-devel
%{summary}.

%package qt6
Summary: Accessibility client library for Qt6
Obsoletes: %{name} < %{version}-%{release}
%description qt6
%{summary}.

%package qt6-devel
Summary: Development files for %{name}-qt6
Obsoletes: %{name}-devel < %{version}-%{release}
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel
%description  qt6-devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libqaccessibilityclient-%{version}
%oreon_prep
%build

%if %{with qt5}
mkdir qt5
pushd qt5
%cmake_kf5 -S ..
%cmake_build
popd
%endif
%if %{with qt6}
mkdir qt6
pushd qt6
%cmake_kf6 -S .. \
	-DQT_MAJOR_VERSION=6
%cmake_build
popd
%endif
%install
%if %{with qt5}
pushd qt5
%cmake_install
popd
%endif
%if %{with qt6}
pushd qt6
%cmake_install
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n qaccessibilityclient-qt5 -f %{oreon_filedir}/qaccessibilityclient-qt5.list
%files -n qaccessibilityclient-qt5-devel -f %{oreon_filedir}/qaccessibilityclient-qt5-devel.list
%files -n qaccessibilityclient-qt6 -f %{oreon_filedir}/qaccessibilityclient-qt6.list
%files -n qaccessibilityclient-qt6-devel -f %{oreon_filedir}/qaccessibilityclient-qt6-devel.list

%changelog

%autochangelog
%endif

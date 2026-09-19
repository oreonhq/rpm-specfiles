%global source0_hash 4c50c448622dc9c5041ed10da7d87b3e4e71ccb49d4831a849211d423c5f5d33

%if (0%{?fedora} && 0%{?fedora} < 40) || (0%{?rhel} && 0%{?rhel} < 10)
%bcond qt5 1
%bcond qt6 0
%else
%bcond qt5 0
%bcond qt6 1
%endif

Name:    qaccessibilityclient
Summary: Accessibility client library for Qt5 and Qt6
Version: 0.6.0
Release: 5%{?dist}

License: CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://cgit.kde.org/libkdeaccessibilityclient.git/
Source0: https://download.kde.org/stable/libqaccessibilityclient/libqaccessibilityclient-%{version}.tar.xz

## upstream patches

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
%if %{with qt5}
BuildRequires: cmake(Qt5)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: kf5-rpm-macros
%endif
%if %{with qt6}
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: kf6-rpm-macros
%endif
BuildRequires: pkgconfig(xkbcommon)

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

%files qt5
%doc AUTHORS README.md
%license LICENSES/*
%{_libdir}/libqaccessibilityclient-qt5.so.0*
%{_datadir}/qlogging-categories5/libqaccessibilityclient.categories

%files qt5-devel
%{_includedir}/QAccessibilityClient/
%{_libdir}/cmake/QAccessibilityClient/
%{_libdir}/libqaccessibilityclient-qt5.so
%endif

%if %{with qt6}
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

%files qt6
%doc AUTHORS README.md
%license LICENSES/*
%{_libdir}/libqaccessibilityclient-qt6.so.0*
%{_datadir}/qlogging-categories6/libqaccessibilityclient.categories

%files qt6-devel
%{_includedir}/QAccessibilityClient6/
%{_libdir}/cmake/QAccessibilityClient6/
%{_libdir}/libqaccessibilityclient-qt6.so
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n libqaccessibilityclient-%{version} -p1

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
%endif

%changelog
%autochangelog

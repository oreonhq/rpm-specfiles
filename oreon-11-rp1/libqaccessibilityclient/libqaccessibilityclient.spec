%global source0_hash 4c50c448622dc9c5041ed10da7d87b3e4e71ccb49d4831a849211d423c5f5d33
%undefine __cmake_in_source_build
Name:           libqaccessibilityclient
Version:        0.6.0
Release:        1%{?dist}
Summary:        Accessibility client library for Qt
License:        LGPL-2.0-or-later
URL:            https://invent.kde.org/library/libqaccessibilityclient
Source0:        https://download.kde.org/stable/libqaccessibilityclient/libqaccessibilityclient-0.6.0.tar.xz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
Qt library used by assistive technologies and screen readers.

%package -n libqaccessibilityclient-qt6
Summary:        Qt 6 accessibility client library
%description -n libqaccessibilityclient-qt6
%{summary}.

%package -n libqaccessibilityclient-qt6-devel
Summary:        Development files for libqaccessibilityclient Qt 6
Requires:       libqaccessibilityclient-qt6%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description -n libqaccessibilityclient-qt6-devel
Headers and CMake files for the Qt 6 build.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libqaccessibilityclient-%{version}
%oreon_prep
%build

%cmake \
  -DQT_MAJOR_VERSION=6 \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_TESTING=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles libqaccessibilityclient-qt6 usr/*/lib*.so.*
%oreon_autofiles libqaccessibilityclient-qt6-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libqaccessibilityclient-qt6 -f %{oreon_filedir}/libqaccessibilityclient-qt6.list
%files -n libqaccessibilityclient-qt6-devel -f %{oreon_filedir}/libqaccessibilityclient-qt6-devel.list

%changelog

* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.0-2
- Add libqaccessibilityclient Qt 6 stack

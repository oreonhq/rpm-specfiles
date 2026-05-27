%global source0_hash 4c50c448622dc9c5041ed10da7d87b3e4e71ccb49d4831a849211d423c5f5d33

%undefine __cmake_in_source_build

Name:           libqaccessibilityclient
Version:        0.6.0
Release:        5%{?dist}
Summary:        Accessibility client library for Qt
License:        LGPL-2.0-or-later
URL:            https://invent.kde.org/library/libqaccessibilityclient
Source0:        https://download.kde.org/stable/libqaccessibilityclient/libqaccessibilityclient-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-qtbase-devel

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n libqaccessibilityclient-%{version} -p1


%build
%cmake \
  -DQT_MAJOR_VERSION=6 \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_TESTING=OFF
%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%doc README*

%files -n libqaccessibilityclient-qt6
%{_datadir}/qlogging-categories6/libqaccessibilityclient.categories
%{_libdir}/libqaccessibilityclient-qt6.so.0*

%files -n libqaccessibilityclient-qt6-devel
%{_includedir}/QAccessibilityClient6
%{_libdir}/libqaccessibilityclient-qt6.so
%{_libdir}/cmake/QAccessibilityClient6
# Upstream 0.6.0 ships CMake config only (no pkg-config file)


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.0-2
- Add libqaccessibilityclient Qt 6 stack

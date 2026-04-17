%undefine __cmake_in_source_build

Name:           libqaccessibilityclient
Version:        0.6.0
Release:        1%{?dist}
Summary:        Accessibility client library for Qt
License:        LGPL-2.0-or-later
URL:            https://invent.kde.org/library/libqaccessibilityclient
Source0:        https://invent.kde.org/library/libqaccessibilityclient/-/archive/v%{version}/libqaccessibilityclient-v%{version}.tar.bz2

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
%autosetup -n libqaccessibilityclient-v%{version} -p1


%build
%cmake \
  -DQT_MAJOR_VERSION=6 \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_TESTING=OFF
%cmake_build


%install
%cmake_install


%files
%license COPYING*
%doc README*
%{_bindir}/dumper

%files -n libqaccessibilityclient-qt6
%{_datadir}/qlogging-categories6/libqaccessibilityclient.categories
%{_libdir}/libqaccessibilityclient-qt6.so.0*

%files -n libqaccessibilityclient-qt6-devel
%{_includedir}/QAccessibilityClient6
%{_libdir}/libqaccessibilityclient-qt6.so
%{_libdir}/cmake/QAccessibilityClient6
%{_libdir}/pkgconfig/QAccessibilityClient6.pc


%changelog
* Thu Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.0-1
- Add libqaccessibilityclient Qt 6 stack

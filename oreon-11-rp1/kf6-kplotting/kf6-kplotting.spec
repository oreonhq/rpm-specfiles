%undefine __cmake_in_source_build

%global framework kplotting
%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:           kf6-%{framework}
Version:        6.24.0
Release:	2%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon for plotting
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# Fedora
BuildRequires:  kf6-rpm-macros
Requires:       kf6-filesystem

# KDE Frameworks
BuildRequires:  extra-cmake-modules >= %{version}

# Other
BuildRequires:  pcre2-devel
BuildRequires:  perl-interpreter

# Qt
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6UiPlugin)

%description
KPlotting provides classes to do plotting.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6 \
    -DQDOC_BIN=/bin/true
%cmake_build_kf6

%install
%cmake_install_kf6

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6Plotting.so.*

%files devel
%{_kf6_includedir}/KPlotting/
%{_kf6_libdir}/libKF6Plotting.so
%{_kf6_libdir}/cmake/KF6Plotting/
%{_kf6_qtplugindir}/designer/kplotting6widgets.so

%changelog
* Fri Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Pass -DQDOC_BIN=/bin/true to work around qdoc segfault until kf6-rpm-macros is deployed

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

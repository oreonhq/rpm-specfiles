%global source0_hash dd77529a93ac3f9aefe571961e8f7ab14c416f3164a524c6588284bcc1ac817b

# enable tests
%global tests 1

Name:    libkomparediff2
Summary: Library to compare files and strings
Version: 26.04.3
Release: 1%{?dist}

# Library: GPLv2+ (some files LGPLv2+), CMake scripts: BSD
License: GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause
URL:     https://invent.kde.org/sdk/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)

Requires:       diffutils

%description
A shared library to compare files and strings using KDE Frameworks 6 and GNU
diff, used in Kompare and KDevelop.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake
Requires: cmake(Qt6Core)
Requires: cmake(Qt6Widgets)
Requires: cmake(KF6Config)
Requires: cmake(KF6XmlGui)

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup


%build
%cmake_kf6 \
  -DBUILD_TESTING:BOOL=%{?tests}%{!?tests:0}

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name


%check
%if 0%{?tests}
%ctest
%endif


%files -f %{name}.lang
%license COPYING*
%{_kf6_datadir}/qlogging-categories6/libkomparediff2.categories
%{_libdir}/libkomparediff2.so.6*

%files devel
%{_includedir}/KompareDiff2/
%{_libdir}/libkomparediff2.so
%{_libdir}/cmake/KompareDiff2/


%changelog
%autochangelog


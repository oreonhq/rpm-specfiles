%global source0_hash 3b85c3929034b0a99da777130c34d99f006fcd3a9d56564159399a33fee0e504
%bcond_without qt5
%bcond_without qt6
Name:           qtkeychain
Version:        0.17.0
Release:        2%{?dist}
Summary:        A password store library
License:        BSD-3-Clause
Url:            https://github.com/frankosterfeld/qtkeychain
Source0:        https://github.com/frankosterfeld/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libsecret-1)
# /oreon:deps
%description
The qtkeychain library allows you to store passwords easily and securely.

%if %{with qt5}
%package qt5
Summary:        %{summary}
%description qt5
The qt5keychain library allows you to store passwords easily and securely.

%package qt5-devel
Summary:        Development files for %{name}-qt5
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5LinguistTools)
Requires:       %{name}-qt5%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       qt5-qtbase-devel%{?_isa}
Requires:       pkgconfig(libsecret-1)
%description qt5-devel
This package contains development files for qt5keychain.
%endif

%if %{with qt6}
%package qt6
Summary:        %{summary}
%description qt6
The qt6keychain library allows you to store passwords easily and securely.

%package qt6-devel
Summary:        Development files for %{name}-qt6
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
Requires:       %{name}-qt6%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       qt6-qtbase-devel%{?_isa}
Requires:       pkgconfig(libsecret-1)
%description qt6-devel
This package contains development files for qt6keychain.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if %{with qt5}
%define _vpath_builddir %{_target_platform}-qt5
%cmake \
  -DBUILD_WITH_QT5:BOOL=ON \
  -DECM_MKSPECS_INSTALL_DIR=%{_qt5_archdatadir}/mkspecs/modules \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build
%endif
%if %{with qt6}
%define _vpath_builddir %{_target_platform}-qt6
%cmake \
  -DBUILD_WITH_QT6:BOOL=ON \
  -DECM_MKSPECS_INSTALL_DIR=%{_qt6_archdatadir}/mkspecs/modules \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build
%endif
%install
%if %{with qt5}
%define _vpath_builddir %{_target_platform}-qt5
%cmake_install
%endif
%if %{with qt6}
%define _vpath_builddir %{_target_platform}-qt6
%cmake_install
%endif
%find_lang %{name} --with-qt
grep %{_datadir}/qt5keychain/translations %{name}.lang > %{name}-qt5.lang
grep %{_datadir}/qt6keychain/translations %{name}.lang > %{name}-qt6.lang
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with qt5}
%files -f %{oreon_filedir}/main.list
%files -n qtkeychain-qt5 -f %{oreon_filedir}/qtkeychain-qt5.list
%files -n qtkeychain-qt5-devel -f %{oreon_filedir}/qtkeychain-qt5-devel.list
%files -n qtkeychain-qt6 -f %{oreon_filedir}/qtkeychain-qt6.list
%files -n qtkeychain-qt6-devel -f %{oreon_filedir}/qtkeychain-qt6-devel.list

%changelog

%autochangelog
%endif

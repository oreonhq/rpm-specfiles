%global source0_hash e812617477f3c2bb990561767a4cd8b1d3803a52018d4878da302529552610d4

#global snap0 20150318
#global commit0 d0f62e65f0b79fb7724d8d551dc9ff11d085127b
#global gittag0 GIT-TAG
#global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Always build out-of-source
%undefine __cmake_in_source_build

# define to support qjson-qt5(-devel)
%if 0%{?fedora} || 0%{?rhel} > 6
%global qt5 1
%endif

Name:           qjson
Version:        0.9.0
Release:        24%{?dist}
Summary:        A qt-based library that maps JSON data to QVariant objects

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/flavio/qjson
%if 0%{?commit0:1}
Source0:        https://github.com/flavio/qjson/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%else
Source0:        https://github.com/flavio/qjson/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

## upstream patches

## upstreamable patches
Patch100: qjson-0.9.0-static.patch

BuildRequires: make
BuildRequires:  cmake >= 2.8.8
BuildRequires:  doxygen
BuildRequires:  pkgconfig(QtCore)
%if 0%{?qt5}
BuildRequires:  pkgconfig(Qt5Core)
%endif

# %%check
BuildRequires: xorg-x11-server-Xvfb

%description
JSON is a lightweight data-interchange format. It can represents integer, real
number, string, an ordered sequence of value, and a collection of
name/value pairs.QJson is a qt-based library that maps JSON data to
QVariant objects.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package qt5
Summary: A Qt5-based library that maps JSON data to QVariant objects
%description qt5
%{summary}.

%package qt5-devel
Summary: Development files for %{name}-qt5
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q %{?commit0:-n %{name}-%{commit0}}

%patch -P100 -p1 -b .static

%build
%global _vpath_builddir %{_target_platform}
%{cmake} .. \
  -DQJSON_BUILD_TESTS:BOOL=ON \
  -DQT4_BUILD:BOOL=ON

%cmake_build

%if 0%{?qt5}
%global _vpath_builddir %{_target_platform}-qt5
%{cmake} .. \
  -DQJSON_BUILD_TESTS:BOOL=ON \
  -DQT4_BUILD:BOOL=OFF

%cmake_build
%endif

# build docs
pushd doc
doxygen
popd

%install
%if 0%{?qt5}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-qt5
%endif
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion QJson)" = "%{version}"
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a make test -C %{_target_platform} ||:
%if 0%{?qt5}
test "$(pkg-config --modversion QJson-qt5)" = "%{version}"
xvfb-run -a make test -C %{_target_platform}-qt5 ||:
%endif

%ldconfig_scriptlets

%files
%license COPYING.lib
%doc README.md README.license
%{_libdir}/libqjson.so.%{version}
%{_libdir}/libqjson.so.0*

%files devel
%doc doc/html
%{_includedir}/qjson/
%{_libdir}/libqjson.so
%{_libdir}/pkgconfig/QJson.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/qjson/

%if 0%{?qt5}
%files qt5
%license COPYING.lib
%doc README.md README.license
%{_libdir}/libqjson-qt5.so.%{version}
%{_libdir}/libqjson-qt5.so.0*

%files qt5-devel
%doc doc/html
%{_includedir}/qjson-qt5/
%{_libdir}/libqjson-qt5.so
%{_libdir}/pkgconfig/QJson-qt5.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/qjson-qt5/
%endif

%changelog
%autochangelog

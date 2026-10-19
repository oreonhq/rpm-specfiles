%global source0_hash e812617477f3c2bb990561767a4cd8b1d3803a52018d4878da302529552610d4
%undefine __cmake_in_source_build
Name:           qjson
Version:        0.9.0
Release:        24%{?dist}
Summary:        A qt-based library that maps JSON data to QVariant objects
License:        GPL-2.0-or-later
URL:            https://github.com/flavio/qjson
%if 0%{?commit0:1}
Source0:        https://github.com/flavio/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
%endif
Patch100: qjson-0.9.0-static.patch
%if 0%{?qt5}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
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
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DQJSON_BUILD_TESTS:BOOL=ON \
  -DQT4_BUILD:BOOL=ON
%cmake_build
%if 0%{?qt5}
%global _vpath_builddir %{_target_platform}-qt5
%{cmake} .. \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DQJSON_BUILD_TESTS:BOOL=ON \
  -DQT4_BUILD:BOOL=OFF
%cmake_build
%endif
pushd doc
doxygen
popd
%install
%if 0%{?qt5}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-qt5
%endif
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

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
%files -f %{oreon_filedir}/main.list
%files -n qjson-devel -f %{oreon_filedir}/qjson-devel.list
%files -n qjson-qt5 -f %{oreon_filedir}/qjson-qt5.list
%files -n qjson-qt5-devel -f %{oreon_filedir}/qjson-qt5-devel.list

%changelog

%autochangelog

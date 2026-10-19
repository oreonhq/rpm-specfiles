%global source0_hash 025bf3d5e4edebae86851d3a5d66ba4596a2c3a49f861f7c49d99b421dadf102
ExcludeArch:    %{ix86}
%global build_qt_client 1
%bcond_with system_libs
%global build_tests 1
%ifarch ppc64le
%global fix_warnings OFF
%else
%global fix_warnings ON
%endif
Name:       libindi
Version:    2.2.4.2
Release:        1%{?dist}
Summary:        Instrument Neutral Distributed Interface
License:    GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later and BSD-3-Clause AND ISC AND MIT AND CFITSIO
URL:        http://www.indilib.org
Source0:        https://github.com/indilib/indi/archive/v%{version}/indi-%{version}.tar.gz
%if %{with system_libs}
%global system_httplib ON
%global system_jsonlib ON
%global system_hidlib ON
%else
%global system_httplib OFF
%global system_jsonlib OFF
%global system_hidlib OFF
%endif
%if 0%{?build_qt_client}
%global qt_client ON
%else
%global qt_client OFF
%endif
%if 0%{?build_tests}
%global tests ON
%else
%global tests OFF
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: bundled(fpack) = 1.7.0
%if %{without system_libs}
Provides: bundled(httplib) = 0.12.4
Provides: bundled(json) = 3.10.5
Provides: bundled(hidapi)
%endif
Obsoletes:  indi-3rdparty-drivers < 2.1.5
Obsoletes:  indi-3rdparty-libraries < 2.1.5
# oreon:deps
BuildRequires:  cmake
BuildRequires:  libXISF-devel
BuildRequires:  libev-devel
BuildRequires:  libnova-devel
BuildRequires:  libogg-devel
BuildRequires:  libtheora-devel
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
INDI is a distributed control protocol designed to operate
astronomical instrumentation. INDI is small, flexible, easy to parse,
and scalable. It supports common DCS functions such as remote control,
data acquisition, monitoring, and a lot more.

%package devel
Summary: Libraries, includes, etc. used to develop an application with %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-static%{?_isa} = %{version}-%{release}
%description devel
These are the header files needed to develop a %{name} application

%package libs
Summary: INDI shared libraries
%description libs
These are the shared libraries of INDI.

%if 0%{?build_qt_client}
%package qt
Summary: INDI QT client libraries
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description qt
These are the QT client libraries of INDI.
%endif

%package static
Summary: Static libraries, includes, etc. used to develop an application with %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description static
Static library needed to develop a %{name} application

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n indi-%{version}

# For Fedora we want to put udev rules in %%{_udevrulesdir}
sed -i 's|/lib/udev/rules.d|%{_udevrulesdir}|g' CMakeLists.txt
chmod -x drivers/telescope/pmc8driver.h
chmod -x drivers/telescope/pmc8driver.cpp

%if %{with system_libs}
# Remove bundled httplib-headers and license file
rm -rf libs/httplib
# Remove bundled json library
rm -rf libs/nlohmann
# Remove bundled hidapi library
rm -rf libs/hid
%endif

%build

%cmake \
    -DINDI_BUILD_QT_CLIENT="%{qt_client}" \
    -DINDI_BUILD_UNITTESTS="%{tests}" \
    -DINDI_SYSTEM_HTTPLIB="%{system_httplib}" \
    -DINDI_SYSTEM_JSONLIB="%{system_jsonlib}" \
    -DINDI_SYSTEM_HIDAPILIB="%{system_hidlib}" \
    -DFIX_WARNINGS=%{fix_warnings}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.*

%check

%if 0%{?build_tests}
%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n libindi-devel -f %{oreon_filedir}/libindi-devel.list
%files -n libindi-libs -f %{oreon_filedir}/libindi-libs.list
%files -n libindi-qt -f %{oreon_filedir}/libindi-qt.list
%files -n libindi-static -f %{oreon_filedir}/libindi-static.list

%changelog

%autochangelog


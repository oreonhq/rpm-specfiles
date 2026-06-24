%global source0_hash none

%global major   1

Name:           wslay
Version:        1.1.1
Release:        8%{?dist}
Summary:        Lightweight WebSocket library in C
License:        MIT
URL:            https://tatsuhiro-t.github.io/wslay
Source0:        https://github.com/tatsuhiro-t/wslay/archive/release-%{version}/%{name}-release-%{version}.tar.gz
# Patch from Debian: https://salsa.debian.org/debian/wslay
Patch0:         10_update_cmake.patch
# Fix build with cmake 4.0. Could be upstreamed but project unmaintained.
Patch1:         wslay-cmake4.0-compat.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
# For tests
BuildRequires:  pkgconfig(cunit)

%description
Wslay is a WebSocket library written in C. It implements the protocol
version 13 described in RFC 6455. This library offers 2 levels of API:
event-based API and frame-based low-level API.

For event-based API, it is suitable for non-blocking reactor pattern
style. You can set callbacks in various events.
For frame-based API, you can send WebSocket frame directly. Wslay only
supports data transfer part of WebSocket protocol and does not perform
opening handshake in HTTP.

%package devel
Summary:        Development headers and library for Wslay
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and library for the Wslay C WebSocket library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-release-%{version}

%build
%cmake -DWSLAY_EXAMPLES=NO
%cmake_build

%install
%cmake_install

# Create and install pkgconfig file
install -d %{buildroot}%{_libdir}/pkgconfig
cat << EOF > %{buildroot}%{_libdir}/pkgconfig/lib%{name}.pc
prefix=%{_prefix}
exec_prefix=\${prefix}
libdir=\${prefix}/%{_lib}
includedir=\${prefix}/include

Name: %{name}
Description: Lightweight WebSocket library in C
URL: %{url}
Version: %{version}
Libs: -L\${libdir} -l%{name}
Cflags: -I\${includedir}
EOF

%check
%{_vpath_builddir}/tests/wslay_tests

%files
%license AUTHORS COPYING
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{version}

%files devel
%doc NEWS README.rst
%license AUTHORS COPYING
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
%autochangelog


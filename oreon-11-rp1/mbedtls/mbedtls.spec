%global source0_hash 2bed9d713b4668f76553b097e72b8aa30bc8f112a940d7ae228d524bbde6ffea
Name: mbedtls
Version: 4.2.0
Release:        1%{?dist}
Summary:        Light-weight cryptographic and SSL/TLS library
License: Apache-2.0 OR GPL-2.0-or-later
URL: https://www.trustedfirmware.org/projects/mbed-tls
Source0:        https://github.com/Mbed-TLS/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  python3
# /oreon:deps
%description
Mbed TLS is a light-weight open source cryptographic and SSL/TLS
library written in C. Mbed TLS makes it easy for developers to include
cryptographic and SSL/TLS capabilities in their (embedded)
applications with as little hassle as possible.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains documentation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

sed -i 's|//\(#define MBEDTLS_THREADING_C\)|\1|' include/mbedtls/mbedtls_config.h
sed -i 's|//\(#define MBEDTLS_THREADING_PTHREAD\)|\1|' include/mbedtls/mbedtls_config.h

%build

export CFLAGS="%{optflags} -Wno-stringop-overflow -Wno-maybe-uninitialized -Wno-error=unterminated-string-initialization -fzero-init-padding-bits=unions"
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DLINK_WITH_PTHREAD=ON \
	-DINSTALL_MBEDTLS_HEADERS=ON \
	-DENABLE_PROGRAMS=OFF \
	-DUSE_SHARED_MBEDTLS_LIBRARY=ON \
	-DUSE_STATIC_MBEDTLS_LIBRARY=OFF \
	-DGEN_FILES=OFF
%cmake_build
make apidoc
%install
%cmake_install
chmod 755 %{buildroot}%{_libdir}/*.so.*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest --output-on-failure --force-new-ctest-process --parallel 1
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n mbedtls-devel -f %{oreon_filedir}/mbedtls-devel.list
%files -n mbedtls-doc -f %{oreon_filedir}/mbedtls-doc.list

%changelog

%autochangelog


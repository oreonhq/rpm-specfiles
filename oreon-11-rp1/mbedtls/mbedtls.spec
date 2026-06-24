%global source0_hash none

Name: mbedtls
Version: 3.6.6
Release: 2%{?dist}
Summary: Light-weight cryptographic and SSL/TLS library
License: Apache-2.0 OR GPL-2.0-or-later
URL: https://www.trustedfirmware.org/projects/mbed-tls
Source0: https://github.com/Mbed-TLS/%{name}/archive/refs/tags/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: perl-interpreter
BuildRequires: python3

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
%if 0%{?fedora}
export CFLAGS="%{optflags} -Wno-stringop-overflow -Wno-maybe-uninitialized -Wno-error=unterminated-string-initialization -fzero-init-padding-bits=unions"
%endif

%if 0%{?rhel} <= 10
export CFLAGS="%{optflags} -Wno-stringop-overflow -Wno-maybe-uninitialized"
%endif

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

# Library files aren't supposed to be executable, but RPM requires this historically
# for automatic per-file level automatic dependency generation at ELF binaries; see:
# - https://github.com/ARMmbed/mbedtls/commit/280165c9b39091c7c7ffe031430c7cf93ebc4dec
# - https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/PDD6RNQMII472HXM4XAUUWWZKKBGHPTO/
chmod 755 %{buildroot}%{_libdir}/*.so.*

%check
%ctest --output-on-failure --force-new-ctest-process --parallel 1

%ldconfig_scriptlets

%files
%doc ChangeLog
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/mbedtls/
%{_includedir}/psa/
%{_includedir}/everest/
%{_libdir}/cmake/MbedTLS/
%{_libdir}/pkgconfig/
%{_libdir}/*.so

%files doc
%doc apidoc/*

%changelog
%autochangelog


%global source0_hash b483a5f77e548964553f54a0ec5f0c810cc6c0629c5ac5a03610bcced150e7be
Name:           libjwt
Version:        3.6.1
Release:        1%{?dist}
Summary:        A Javascript Web Token library in C
License:        MPL-2.0
URL:            https://github.com/benmcollins/libjwt
Source0:        https://github.com/benmcollins/libjwt/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  jansson-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
# /oreon:deps
%description
A Javascript Web Token library in C (JWT, JWK and JWKS support).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        Command line tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tools
Command line utilities (jwt-generate, jwt-verify, jwe-encrypt, jwe-decrypt,
jwk2key, key2jwk) built
on %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
# do not build with -Werror in distro builds
sed -i 's/ -Werror / /' CMakeLists.txt

%build

%cmake \
    -DWITH_GNUTLS=OFF \
    -DWITH_MBEDTLS=OFF \
    -DWITH_LIBCURL=OFF \
    -DWITH_TESTS=OFF \
    -DWITH_OPENSSL=ON
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_libdir}/libjwt.a %{buildroot}%{_libdir}/libjwt_static.a
rm -rf %{buildroot}%{_libdir}/cmake/LibJWT/LibJWTStaticTargets*.cmake
rm -rf %{buildroot}%{_docdir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libjwt-devel -f %{oreon_filedir}/libjwt-devel.list
%files -n libjwt-tools -f %{oreon_filedir}/libjwt-tools.list

%changelog

%autochangelog

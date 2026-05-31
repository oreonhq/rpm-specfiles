%global source0_hash be81ef08baa2516ecda76a77adf7def7bc3227eeb578b9a33b45f7b41dc064e6

# Major version
%define major 1

Name:           libserf
Version:        1.3.10
Release:        13%{?dist}
Summary:        High-Performance Asynchronous HTTP Client Library
License:        Apache-2.0
URL:            https://serf.apache.org/
Source0:        https://archive.apache.org/dist/serf/serf-%{version}.tar.bz2
BuildRequires:  gcc, pkgconfig
BuildRequires:  apr-devel, apr-util-devel, krb5-devel, openssl-devel
BuildRequires:  zlib-devel, cmake
%ifnarch %ix86
BuildRequires: openssl, libfaketime
%endif
Patch0:         %{name}-norpath.patch
Patch1:         %{name}-1.3.9-errgetfunc.patch
Patch2:		%{name}-1.3.9-multihome.patch
Patch3:		%{name}-1.3.9-cmake.patch
Patch4:		%{name}-1.3.10-gssapi.patch

%description
The serf library is a C-based HTTP client library built upon the Apache 
Portable Runtime (APR) library. It multiplexes connections, running the
read/write communication asynchronously. Memory copies and transformations are
kept to a minimum to provide high performance operation.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       apr-devel%{?_isa}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n serf-%{version} -p1
%ifnarch %ix86
pushd test/server
openssl req -x509 -newkey rsa:2048 -keyout serfrootcacert.pem -out serfrootcacert.pem -sha256 -days 3650 -nodes -subj "/C=BE/ST=Antwerp/L=Mechelen/O=In Serf we trust, Inc./OU=Test Suite Root CA/CN=Serf Root CA/emailAddress=serfrootca@example.com"
openssl req -x509 -newkey rsa:2048 -keyout serfcacert.pem -out serfcacert.pem -sha256 -days 3650 -nodes -subj "/C=BE/ST=Antwerp/L=Mechelen/O=In Serf we trust, Inc./OU=Test Suite CA/CN=Serf CA/emailAddress=serfca@example.com" -CA serfrootcacert.pem -CAkey serfrootcacert.pem
openssl req -x509 -newkey rsa:2048 -keyout serfserverkey.pem -out serfservercert.pem -sha256 -days 3650 -subj "/C=BE/ST=Antwerp/L=Mechelen/O=In Serf we trust, Inc./OU=Test Suite Server/CN=localhost/emailAddress=serfserver@example.com" -CA serfcacert.pem -CAkey serfcacert.pem -passout pass:serftest
faketime '2050-12-24 08:15:42' openssl req -x509 -out serfserver_future_cert.pem -subj "/C=BE/ST=Antwerp/L=Mechelen/O=In Serf we trust, Inc./OU=Test Suite Server/CN=localhost/emailAddress=serfserver@example.com" -CA serfcacert.pem -CAkey serfcacert.pem -key serfserverkey.pem -days 30 -passout pass:serftest -passin pass:serftest
faketime '1990-12-24 08:15:42' openssl req -x509 -out serfserver_expired_cert.pem -subj "/C=BE/ST=Antwerp/L=Mechelen/O=In Serf we trust, Inc./OU=Test Suite Server/CN=localhost/emailAddress=serfserver@example.com" -CA serfcacert.pem -CAkey serfcacert.pem -key serfserverkey.pem -days 30 -passout pass:serftest -passin pass:serftest
openssl req -x509 -newkey rsa:2048 -keyout serfclientkey.pem -out serfclientcert.pem -sha256 -days 3650 --CA serfcacert.pem --CAkey serfcacert.pem -subj "/C=BE/ST=Antwerp/L=Mechelen/O=In Serf we trust, Inc./OU=Test Suite Client/CN=Serf Client/emailAddress=serfclient@example.com" --nodes
openssl pkcs12 -export -in serfclientcert.pem -inkey serfclientkey.pem -out serfclientcert.p12 -passout pass:serftest
popd
%endif

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} -DGSSAPI=ON -DSKIP_STATIC=ON
%cmake_build

%install
%cmake_install

%if %{major} == 1
# Create compat stub library for cross-distro compatibility, since
# upstream unintentionally bumped the soname from libserf-1.so.0 to
# libserf-1.so.1 in 1.3.0. This can be deleted once major is 2.
# See: https://lists.apache.org/thread/o1vvpbv6pvw0bh8x5zqwyzbsqk4ntj7c
%define compatso libserf-1.so.1
%{__cc} %{optflags} -shared -o %{buildroot}%{_libdir}/%{compatso} \
       -Wl,-soname,%{compatso} -L%{buildroot}%{_libdir} -lserf-1
%endif

%check
%ifnarch %ix86
%ctest 
%else
true
%endif
grep '^Version: %{version}' %{buildroot}%{_libdir}/pkgconfig/serf-%{major}.pc

%ldconfig_scriptlets

%files
%license LICENSE NOTICE
%{_libdir}/*.so.*

%files devel
%doc CHANGES README design-guide.txt
%{_includedir}/serf-%{major}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/serf*.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.10-13
- Import

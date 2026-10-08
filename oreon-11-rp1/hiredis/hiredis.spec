%global source0_hash ca3180359a8b1275838a45415851f8cd5c411e27bdbf18f4823012e45507d2e4

Name:           hiredis
Version:        1.4.1
Release:        1%{?dist}
Summary:        Minimalistic C client library for Redis
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/redis/hiredis
Source0:        https://github.com/redis/hiredis/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
%ifnarch %{ix86}
BuildRequires:  valkey
%endif

%description 
Hiredis is a minimalistic C client library for the Redis database.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%make_build PREFIX="%{_prefix}" LIBRARY_PATH="%{_lib}" \
            LDFLAGS="%{?__global_ldflags}" USE_SSL=1

%install
%make_install PREFIX="%{_prefix}" LIBRARY_PATH="%{_lib}" USE_SSL=1

find %{buildroot} -name '*.a' -delete -print

%ifnarch %{ix86}
%check
make check REDIS_SERVER=valkey-server
%endif

%files
%doc COPYING
%{_libdir}/libhiredis.so.1
%{_libdir}/libhiredis.so.1.*
%{_libdir}/libhiredis_ssl.so.1
%{_libdir}/libhiredis_ssl.so.1.*

%files devel
%doc CHANGELOG.md README.md
%{_includedir}/%{name}/
%{_libdir}/libhiredis.so
%{_libdir}/libhiredis_ssl.so
%{_libdir}/pkgconfig/hiredis.pc
%{_libdir}/pkgconfig/hiredis_ssl.pc

%changelog
%autochangelog

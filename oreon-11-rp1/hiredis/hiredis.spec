%global source0_hash 82ad632d31ee05da13b537c124f819eb88e18851d9cb0c30ae0552084811588c
%global __oreon_hwcaps_post_install %{nil}
%global _distro_extra_cflags %{nil}
%global _distro_extra_cxxflags %{nil}
%global _distro_extra_ldflags %{nil}

Name:           hiredis
Version:        1.2.0
Release:        9%{?dist}
Summary:        Minimalistic C client library for Redis
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/redis/hiredis
Source0:        https://github.com/redis/hiredis/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         hiredis-envvar.patch
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
%{_libdir}/libhiredis.so.1.1.0
%{_libdir}/libhiredis_ssl.so.1
%{_libdir}/libhiredis_ssl.so.1.1.0

%files devel
%doc CHANGELOG.md README.md
%{_includedir}/%{name}/
%{_libdir}/libhiredis.so
%{_libdir}/libhiredis_ssl.so
%{_libdir}/pkgconfig/hiredis.pc
%{_libdir}/pkgconfig/hiredis_ssl.pc

%changelog
* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-9
- Import for Oreon 11

%global source0_hash ca3180359a8b1275838a45415851f8cd5c411e27bdbf18f4823012e45507d2e4
Name:           hiredis
Version:        1.4.1
Release:        1%{?dist}
Summary:        Minimalistic C client library for Redis
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/redis/hiredis
Source0:        https://github.com/redis/hiredis/archive/v%{version}/%{name}-%{version}.tar.gz
%ifnarch %{ix86}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  valkey
# /oreon:deps
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
%oreon_prep
%build

%make_build PREFIX="%{_prefix}" LIBRARY_PATH="%{_lib}" \
            LDFLAGS="%{?__global_ldflags}" USE_SSL=1
%install
%make_install PREFIX="%{_prefix}" LIBRARY_PATH="%{_lib}" USE_SSL=1
find %{buildroot} -name '*.a' -delete -print
%ifnarch %{ix86}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check REDIS_SERVER=valkey-server
%endif
%files -f %{oreon_filedir}/main.list
%files -n hiredis-devel -f %{oreon_filedir}/hiredis-devel.list

%changelog

%autochangelog
